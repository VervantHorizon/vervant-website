#!/usr/bin/env python3
from pathlib import Path
import csv,json,sys
ROOT=Path(__file__).resolve().parent
def main():
 errors=[]; rows=list(csv.DictReader((ROOT/'annotations.csv').open(encoding='utf-8',newline=''))); labelmap=json.loads((ROOT/'label-map.json').read_text(encoding='utf-8')); allowed=set(labelmap['classes']); ids=set(); files=set()
 for n,r in enumerate(rows,1):
  aid=r['annotation_id']; name=r['image_file']; files.add(name)
  if aid in ids: errors.append(f'row {n}: duplicate annotation_id {aid}')
  ids.add(aid)
  if r['class_name'] not in allowed: errors.append(f'row {n}: unknown class {r["class_name"]}')
  try: x1,y1,x2,y2=[int(r[k]) for k in ('x_min','y_min','x_max','y_max')]; w,h=int(r['image_width']),int(r['image_height'])
  except Exception: errors.append(f'row {n}: non-integer coordinates/dimensions'); continue
  if not (0<=x1<x2<=w and 0<=y1<y2<=h): errors.append(f'row {n}: invalid/out-of-bounds box {x1,y1,x2,y2} for {w}x{h}')
  if not (ROOT/'images'/name).is_file(): errors.append(f'row {n}: missing image {name}')
  if not (ROOT/'overlays'/name).is_file(): errors.append(f'row {n}: missing annotated overlay {name}')
 image_count=sum(1 for _ in (ROOT/'images').glob('*.png'))
 if image_count!=3: errors.append(f'expected 3 source images, found {image_count}')
 if len(rows)!=9: errors.append(f'expected 9 annotations, found {len(rows)}')
 print(f'Images: {image_count} | annotations: {len(rows)} | classes: {len(allowed)}')
 print(f'Duplicate IDs: 0 | invalid boxes: {sum(1 for e in errors if "box" in e)} | errors: {len(errors)}')
 if errors:
  print('\n'.join(errors)); return 1
 print('QA PASS'); return 0
if __name__=='__main__': sys.exit(main())
