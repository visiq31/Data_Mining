# -*- coding: utf-8 -*-
"""ModelEvaluator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rbaxePKizlLo475DvckUwLFoXESeZE3F
"""

from sklearn.metrics import confusion_matrix

class ModelEvaluator:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test

    def evaluate_model(self):
        # ModelEvaluator
        y_pred = self.model.predict(self.X_test)
        confusion_matrix_result = confusion_matrix(self.y_test, y_pred)
        return confusion_matrix_result