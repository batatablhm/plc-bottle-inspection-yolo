# PLC-Based Bottle Cap and Label Inspection using YOLO

## Overview

This project implements a real-time industrial inspection system for detecting bottle cap presence and label presence using Ultralytics YOLO and Siemens S7 PLC integration.

The system performs a two-stage verification:

1. Cap detection (cap / noCap)
2. If a cap is detected, label verification
3. Automatic PLC signal triggering for defective bottle ejection

The solution was developed as a practical computer vision + industrial automation system.

---

## Technical Stack

- Ultralytics YOLO (PyTorch-based)
- OpenCV + cvzone for visualization
- python-snap7 for Siemens S7-1200 PLC communication
- GPU training (NVIDIA GTX 1650 Ti)

---

## Dataset & Training

- Approximately 1000 manually captured images
- Train / Validation / Test split
- Fine-tuning of pretrained YOLO weights
- Data augmentation applied during training

### Evaluation Results

- mAP@0.5 approached 1.0
- mAP@0.5:0.95 ≈ 0.8

These results demonstrate strong localization and classification performance under controlled production conditions.

---

## System Workflow

Camera → YOLO Detection → Decision Logic → PLC Memory Bit → Bottle Ejection Actuator

---

## Limitations & Responsible AI Considerations

- Dataset collected under controlled lighting conditions
- Performance may vary in different environments
- Additional data collection may be required for domain adaptation

---

## Files

- cap.py – basic cap detection
- implementation.py – full pipeline with PLC control
- label.py – label detection logic
- snap.py – PLC communication functions
- Bachelor_Project_poster.pdf – project presentation poster

---

## License

MIT License
