import matplotlib.pyplot as plt
import json
import os

def plot_training_results(results_path="runs/detect/train/results.png", save_path="results/figures/training_loss.png"):
    """Copy YOLO result plots to figures folder."""
    if os.path.exists(results_path):
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.figure(figsize=(10,6))
        img = plt.imread(results_path)
        plt.imshow(img)
        plt.axis('off')
        plt.savefig(save_path)
        plt.close()
        print(f"Saved training figure at {save_path}")
    else:
        print(f"Results image not found at {results_path}")

def read_metrics(json_file="runs/detect/train/metrics.json"):
    """Read YOLO metrics.json and return summary dict."""
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            metrics = json.load(f)
        return metrics
    else:
        print(f"Metrics file not found: {json_file}")
        return {}
