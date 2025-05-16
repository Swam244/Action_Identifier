from evaluation_plots import evaluate_model
import csv
import os

labels = ['hello', 'thanks', 'iloveyou']

y_true = []
y_pred = []

# Optional: load from CSV
filename = "prediction_log.csv"

if os.path.exists(filename):
    print(f"Loading predictions from {filename}...")
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            y_true.append(row[0])
            y_pred.append(row[1])
else:
    print("No prediction log found — using dummy values for test.")
    y_true = ['hello', 'thanks', 'thanks', 'iloveyou', 'hello']
    y_pred = ['hello', 'thanks', 'hello', 'iloveyou', 'iloveyou']

evaluate_model(y_true, y_pred, labels)
