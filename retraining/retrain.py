import subprocess
import sys

def retrain_model():
    print("Starting automated retraining process...")

    result = subprocess.run(
        [sys.executable, "src/train.py"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("Retraining failed.")
        print(result.stderr)
    else:
        print("Retraining completed successfully.")

if __name__ == "__main__":
    retrain_model()