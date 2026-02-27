import pandas as pd
import joblib
from pathlib import Path

def predict_priority(input_dict):
    """
    Predict the priority of a helpdesk ticket given its features.
    input_dict: dict with keys 'Department', 'Device_Type', 'Issue_Type', 'Resolution_Time'
    Returns: predicted priority (str)
    """
    project_root = Path(__file__).resolve().parents[1]
    model_path = project_root / "models" / "priority_model.pkl"
    clf = joblib.load(model_path)

    # Create a DataFrame for a single sample
    X_new = pd.DataFrame([input_dict])
    pred = clf.predict(X_new)[0]
    return pred

if __name__ == "__main__":
    # Example usage
    sample = {
        "Department": "Computer Lab",
        "Device_Type": "Desktop",
        "Issue_Type": "WiFi",
        "Resolution_Time": 30
    }
    result = predict_priority(sample)
    print(f"Predicted priority: {result}")
