from AIEvaluation.aievaluation.bl.ModelEvaluationHandler import ModelEvaluationHandler
from AIEvaluation.aievaluation.driver.AIModelEvaluationService import AIModelEvaluationService
import numpy as np
import time




evaluation_service= AIModelEvaluationService()


evaluation_metric_list = ["Precision", "Recall", "Fmeasure", "Accuracy","True_Positives", "True_Negatives", "False_Positives", "False_Negatives"]

predicted_target = np.random.randint(2, size=1000000)
actual_target = np.random.randint(2, size=1000000)

print(evaluation_service.evaluate_model(evaluation_metric_list, predicted_target, actual_target))










