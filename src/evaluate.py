# Evaluation script
from ultralytics import YOLO
import argparse

def main(args):
    model = YOLO(args.weights)
    model.val()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", required=True)
    args = parser.parse_args()
    main(args)
