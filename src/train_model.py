import pandas as pd
from pathlib import Path
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "raw" / "helpdesk_tickets.csv"

    df = pd.read_csv(data_path)

    # Features (X) and target (y)
    X = df[["Department", "Device_Type", "Issue_Type", "Resolution_Time"]]
    y = df["Priority"]

    categorical_cols = ["Department", "Device_Type", "Issue_Type"]
    numeric_cols = ["Resolution_Time"]

    # Preprocess: One-hot encode categorical, pass numeric through
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols),
        ]
    )

    # Model: simple baseline (beginner-friendly)
    model = LogisticRegression(max_iter=1000)

    # Pipeline keeps it clean and professional
    clf = Pipeline(steps=[("preprocess", preprocessor), ("model", model)])

    # Train/test split (stratify keeps label proportions similar)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    clf.fit(X_train, y_train)

    # Save trained model
    model_dir = project_root / "models"
    model_dir.mkdir(exist_ok=True)

    model_path = model_dir / "priority_model.pkl"
    joblib.dump(clf, model_path)

    print("Model saved at:", model_path)

    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    print("\n--- Model Results ---")
    print(f"Accuracy: {acc:.3f}")

    # Confusion matrix in a fixed label order
    labels = ["Low", "Medium", "High"]
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    print("\nConfusion Matrix (rows=true, cols=pred) [Low, Medium, High]:")
    print(cm)

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()
