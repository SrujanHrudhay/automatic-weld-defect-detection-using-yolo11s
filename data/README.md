# Dataset Information

## Dataset Source

The dataset used in this project was created, managed, and exported using **Roboflow**, an online platform for dataset hosting, annotation, preprocessing, and versioning for computer vision applications.

The dataset resides within the author’s Roboflow workspace and was exported using Roboflow’s dataset management tools in **YOLO format**.

> Roboflow Platform: [https://roboflow.com](https://roboflow.com)

---

## Dataset Access

The dataset can be accessed and downloaded directly from Roboflow using the badge below:

[![Download Dataset from Roboflow](https://app.roboflow.com/images/download-dataset-badge.svg)](https://universe.roboflow.com/srujan-hrudhay/welding-with-weld-qtope-vlx73)

---

## Dataset Description

The dataset consists of **299 annotated welding images**, prepared for the task of automated welding defect detection using object detection models.

Each image contains one or more welding defect instances labeled into **six defect categories** commonly observed in industrial welding processes.

### Defect Classes

1. Crack
2. Porosity
3. Lack of Fusion
4. Slag Inclusion
5. Undercut
6. Spatter

---

## Annotation Format

Annotations follow the **YOLO bounding box format**:

```
<class_id> <x_center> <y_center> <width> <height>
```

All bounding box coordinates are normalized with respect to the image dimensions.

---

## Dataset Split

The dataset was split using Roboflow’s built-in dataset versioning and export mechanism:

* Training set: 70%
* Validation set: 20%
* Test set: 10%

The splits are mutually exclusive and remain consistent across all experiments conducted in this project.

---

## Expected Directory Structure

After exporting the dataset from Roboflow in YOLO format, the directory structure should be organized as follows:

```
data/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
```

---

## Dataset Usage and Reproducibility

The dataset images are **not directly included** in this repository to keep the repository lightweight and to follow standard dataset distribution practices.

To reproduce the experiments reported in this project:

1. Access the dataset via the Roboflow link provided above
2. Export the dataset in **YOLO format**
3. Place the exported files according to the directory structure shown

---

## License Notice

The dataset is governed by Roboflow’s platform terms and dataset usage policies.
This repository provides **source code, configuration files, and documentation only**, and does not redistribute dataset contents directly.
