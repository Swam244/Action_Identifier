from evaluation_plots import evaluate_model
import numpy as np

# Simulated true and predicted labels
y_true = ['hello', 'thanks', 'thanks', 'iloveyou', 'hello', 'thanks']
y_pred = ['hello', 'thanks', 'hello', 'iloveyou', 'hello', 'iloveyou']
labels = ['hello', 'thanks', 'iloveyou']

evaluate_model(y_true, y_pred, labels)
