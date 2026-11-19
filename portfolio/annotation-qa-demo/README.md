# Synthetic object annotation & QA sample

This is a small, fully synthetic portfolio exercise created to demonstrate a basic object-detection annotation workflow. It is not paid client work, not a production dataset, and not a claim of employment or certification.

## Contents
- `images/`: three original synthetic scenes (800 × 600).
- `overlays/`: the same scenes with reviewed bounding boxes and annotation IDs.
- `annotations.csv`: one row per object, with pixel bounding boxes.
- `label-map.json`: classes and coordinate convention.
- `audit.py`: deterministic validation of file existence, class IDs, box bounds, dimensions and duplicate IDs.

## Annotation rules used
1. Draw a tight axis-aligned box around the visible object.
2. Include the whole visible object, not cast shadows.
3. Keep separate object instances as separate rows, even when they share a class.
4. Use only the classes in `label-map.json`; flag uncertainty rather than guessing.
5. Coordinates use the image's original pixel dimensions and a top-left origin.

## Reproduce QA
Run: `python3 audit.py`

Expected outcome: 9 annotations across 3 images, all valid, zero duplicate IDs, zero out-of-bounds boxes.
