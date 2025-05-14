import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import os

def evaluate_model(y_true, y_pred, labels, save_dir="evaluation"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=labels, yticklabels=labels, cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")
    plt.savefig(os.path.join(save_dir, "confusion_matrix.png"))
    plt.close()

    # Classification Report
    report = classification_report(y_true, y_pred, target_names=labels, output_dict=False)
    print("Classification Report:\n")
    print(report)
    with open(os.path.join(save_dir, "classification_report.txt"), "w") as f:
        f.write(report)
