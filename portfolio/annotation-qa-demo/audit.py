#!/usr/bin/env python3
from pathlib import Path
import csv, json, sys
from PIL import Image
ROOT = Path(__file__).resolve().parent

def main():
    errors = []
    box_ids = set()
    box_duplicates = 0
    rows = list(csv.DictReader((ROOT / 'annotations.csv').open(encoding='utf-8', newline='')))
    labelmap = json.loads((ROOT / 'label-map.json').read_text(encoding='utf-8'))
    allowed = set(labelmap['classes'])

    for n, row in enumerate(rows, 1):
        aid, name = row['annotation_id'], row['image_file']
        if aid in box_ids:
            box_duplicates += 1
            errors.append(f'box row {n}: duplicate annotation ID {aid}')
        box_ids.add(aid)
        if row['class_name'] not in allowed:
            errors.append(f'box row {n}: unknown class {row["class_name"]}')
        try:
            x1, y1, x2, y2 = [int(row[k]) for k in ('x_min','y_min','x_max','y_max')]
            w, h = int(row['image_width']), int(row['image_height'])
        except Exception:
            errors.append(f'box row {n}: non-integer coordinates/dimensions')
            continue
        if not (0 <= x1 < x2 <= w and 0 <= y1 < y2 <= h):
            errors.append(f'box row {n}: invalid/out-of-bounds box {x1,y1,x2,y2} for {w}x{h}')
        if not (ROOT/'images'/name).is_file():
            errors.append(f'box row {n}: missing source image {name}')
        if not (ROOT/'overlays'/name).is_file():
            errors.append(f'box row {n}: missing bounding-box overlay {name}')

    image_count = sum(1 for _ in (ROOT/'images').glob('*.png'))
    if image_count != 3:
        errors.append(f'expected 3 source images, found {image_count}')
    if len(rows) != 9:
        errors.append(f'expected 9 bounding boxes, found {len(rows)}')

    data = json.loads((ROOT/'segmentation.json').read_text(encoding='utf-8'))
    items = data.get('items', [])
    seg_ids = set()
    seg_duplicates = 0
    for n, item in enumerate(items, 1):
        sid = item.get('segmentation_id') or item.get('id')
        if not sid:
            sid = f'{item.get("image_file")}:{item.get("class_name")}'
        if sid in seg_ids:
            seg_duplicates += 1
            errors.append(f'segmentation item {n}: duplicate ID {sid}')
        seg_ids.add(sid)
        image_file, mask_file = item.get('image_file',''), item.get('mask_file','')
        if not (ROOT/'images'/image_file).is_file():
            errors.append(f'segmentation item {n}: missing source image {image_file}')
        mask_path = ROOT/'masks'/mask_file
        if not mask_path.is_file():
            errors.append(f'segmentation item {n}: missing mask {mask_file}')
        polygon = item.get('polygon', [])
        if len(polygon) < 3:
            errors.append(f'segmentation item {n}: polygon has fewer than 3 points')
        points = []
        for point in polygon:
            try:
                x, y = int(point['x']), int(point['y'])
            except Exception:
                errors.append(f'segmentation item {n}: invalid point {point}')
                continue
            if not (0 <= x < int(item.get('image_width',0)) and 0 <= y < int(item.get('image_height',0))):
                errors.append(f'segmentation item {n}: out-of-bounds point {x,y}')
            points.append((x,y))
        area = abs(sum(points[i][0]*points[(i+1)%len(points)][1] - points[(i+1)%len(points)][0]*points[i][1] for i in range(len(points))))/2 if len(points) >= 3 else 0
        if area <= 0:
            errors.append(f'segmentation item {n}: polygon has zero area')
        if mask_path.is_file():
            mask = Image.open(mask_path).convert('L')
            expected_size = (int(item.get('image_width',0)), int(item.get('image_height',0)))
            if mask.size != expected_size:
                errors.append(f'segmentation item {n}: mask dimensions {mask.size} != {expected_size}')
            colors = mask.getcolors(maxcolors=2)
            values = {value for count, value in colors} if colors else set()
            if 255 not in values or not values.issubset({0,255}):
                errors.append(f'segmentation item {n}: mask must be non-empty and binary 0/255')
        preview_name = f"segmentation-{sid.replace('seg-','')}.png"
        if not (ROOT/'overlays'/preview_name).is_file():
            errors.append(f'segmentation item {n}: missing preview overlay {preview_name}')

    if len(items) != 3:
        errors.append(f'expected 3 segmentation masks, found {len(items)}')
    print(f'Images: {image_count} | bounding boxes: {len(rows)} | segmentation masks: {len(items)}')
    print(f'Duplicate IDs: {box_duplicates + seg_duplicates} | validation errors: {len(errors)}')
    if errors:
        print('\n'.join(errors))
        return 1
    print('QA PASS')
    return 0

if __name__ == '__main__':
    sys.exit(main())
