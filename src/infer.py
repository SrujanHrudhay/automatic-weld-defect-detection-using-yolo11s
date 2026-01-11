from ultralytics import YOLO
import argparse

def main(args):
    model = YOLO(args.weights)
    model.predict(source=args.source, save=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", required=True)
    parser.add_argument("--source", required=True)
    args = parser.parse_args()
    main(args)
