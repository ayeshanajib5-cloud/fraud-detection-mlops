import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

DATA_PATH = "data/creditcard.csv"
MODEL_PATH = "models/fraud_model.pkl"

def main():
    print("Loading dataset...")

    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("fraud-detection-experiment")

    df = pd.read_csv(DATA_PATH)

    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    with mlflow.start_run():

        print("Training model...")

        model = RandomForestClassifier(
            n_estimators=50,
            random_state=42,
            class_weight="balanced",
            n_jobs=-1
        )

        mlflow.log_param("model_type", "RandomForestClassifier")
        mlflow.log_param("n_estimators", 50)
        mlflow.log_param("class_weight", "balanced")

        model.fit(X_train, y_train)

        print("Evaluating model...")

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        print(classification_report(y_test, y_pred))

        joblib.dump(model, MODEL_PATH)

        mlflow.sklearn.log_model(model, "fraud_model")

        print(f"Model saved at {MODEL_PATH}")

if __name__ == "__main__":
    main()