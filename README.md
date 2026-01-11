# Automatic Weld Defect Detection Using YOLO11s     
![YOLO](https://img.shields.io/badge/YOLO-111F68?style=for-the-badge&logo=yolo&logoColor=white)

This repository contains the official implementation of the research project
_**" Automatic Weld Defect Detection Using YOLO: A Deep Learning Approach to Industial Quality Assurance "**_, developed for academic
and reproducibility purposes.

The work proposes a deep learning–based computer vision system for detecting
and classifying welding defects from industrial weld images using a YOLO-based
object detection framework.

---

## Method Overview

This work presents a single-stage deep learning–based object detection
approach for automated welding defect identification.

A YOLO11s model is trained to directly detect and classify six common
welding defect types from input weld images in a single forward pass.
Each defect instance is localized and assigned one of the predefined
defect classes.

YOLO11s was selected due to its favorable trade-off between detection
accuracy, computational efficiency, and suitability for small-scale
industrial datasets.

---

## Dataset

The dataset used in this study consists of 299 annotated welding images.
Each image contains one or more instances of welding defects labeled
into six categories:

- Crack
- Porosity
- Lack of Fusion
- Slag Inclusion
- Undercut
- Spatter

The dataset size reflects real-world data scarcity commonly encountered
in industrial inspection scenarios.

Due to licensing restrictions, the dataset is not redistributed.
Dataset organization instructions are provided in [data/README.md](data/README.md).

---

## Repository Structure

automatic-weld-defect-detection-using-yolo11s/  
├── **_[configs/](configs)_** # Model and dataset configuration files  
├── **_[data/](data)_** # Dataset instructions and structure    
├── **_[experiments/](experiments)_** # Experiment logs and summaries  
├── **_[results/](results)_** # Generated figures and tables  
├── **_[src/](src)_** # Training, evaluation, and inference scripts  
├── **_[weights/](weights)_** # Trained model weights (or download links)  
├── [![Static Badge](https://img.shields.io/badge/README.md-darkgreen)
](README.md)  
├── **_[requirements.txt](requirements.txt)_**  
├── **_[LICENSE](LICENSE)_**  
└── **_[CITATION.cff](CITATION.cff)_**  

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/SrujanHrudhay/automatic-weld-defect-detection-using-yolo11s.git
cd automatic-weld-defect-detection-using-yolo11s
pip install -r requirements.txt
```
### Tested Environment
 + Python 3.10+
 + PyTorch 2.x
 + Ultralytics YOLO
 + CUDA 11.8 (GPU optional but recommended)

## Training
To train the YOLO11s model:

```bash
python src/train.py \
  --config configs/yolo11s.yaml \
  --data configs/dataset.yaml \
  --epochs 100 \
  --batch 16
```
## Evaluation
```bash
python src/evaluate.py --weights weights/best.pt`
```
Evaluation metrics include Precision, Recall, mAP@0.5, and confusion matrices.

## Inference
```bash
python src/infer.py --weights weights/best.pt --source sample_images/
```
## Reproducibility Statement

All experiments were conducted with fixed configurations, documented
hyperparameters, and consistent dataset splits to ensure reproducibility
of the reported results.

## Citation
If you use this work, please cite:

```bibtex
@article{hrudhay2026weld,
  title={Automatic Weld Defect Detection Using YOLO11s},
  author={Hrudhay, Srujan},
  year={2026}
}
```

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

