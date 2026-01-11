from ultralytics import YOLO
import argparse

def main(args):
    model = YOLO(args.config)
    model.train(
        data=args.data,
        epochs=args.epochs,
        batch=args.batch
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch", type=int, default=16)
    args = parser.parse_args()
    main(args)
