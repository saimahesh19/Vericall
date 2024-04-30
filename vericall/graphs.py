# import matplotlib.pyplot as plt

# # Data
# labels = ['Real Audio', 'Deepfaked Audio']
# sizes = [10000, 10000]  # Sample sizes
# colors = ['skyblue', 'lightcoral']
# explode = (0, 0.1)  # Explode only the second slice (Deepfaked Audio)

# # Plot
# plt.figure(figsize=(8, 6))
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
# plt.title('Distribution of Audio Samples')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()

# import matplotlib.pyplot as plt

# # Data
# classifiers = ['Random Forest', 'KNN', 'Logistic Regression']
# accuracies = [97.12, 71.43, 92.65]  # Accuracies in percentage

# # Plot
# plt.figure(figsize=(8, 6))
# plt.bar(classifiers, accuracies, color=['skyblue', 'lightcoral', 'lightgreen'])
# plt.ylim(0, 100)  # Set y-axis limit from 0 to 100%
# plt.title('Accuracy of Different Classifiers in Deepfake Audio Detection')
# plt.xlabel('Classifier')
# plt.ylabel('Accuracy (%)')

# # Add text labels
# for i in range(len(classifiers)):
#     plt.text(i, accuracies[i] + 1, f"{accuracies[i]:.2f}%", ha='center')

# plt.show()

# import matplotlib.pyplot as plt

# # Data
# classifiers = ['Random Forest', 'KNN', 'Logistic Regression']
# precisions = [95.07, 63.5 , 94.34]  # Precision in percentage

# # Plot
# plt.figure(figsize=(8, 6))
# plt.bar(classifiers, precisions, color=['skyblue', 'lightcoral', 'lightgreen'])
# plt.ylim(0, 100)  # Set y-axis limit from 0 to 100%
# plt.title('Precision of Different Classifiers in Deepfake Audio Detection')
# plt.xlabel('Classifier')
# plt.ylabel('Precision (%)')

# # Add text labels
# for i in range(len(classifiers)):
#     plt.text(i, precisions[i] + 1, f"{precisions[i]:.2f}%", ha='center')

# plt.show()


# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Given parameters
# true_negatives = 9803
# false_positives = 197
# false_negatives = 112
# true_positives = 9888

# # Construct confusion matrix
# conf_matrix = np.array([[true_negatives, false_positives],
#                         [false_negatives, true_positives]])

# # Plot confusion matrix
# plt.figure(figsize=(8, 6))
# sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='Blues', 
#             xticklabels=['Real', 'Deepfake'], yticklabels=['Real', 'Deepfake'])
# plt.title('Confusion Matrix for Random Forest')
# plt.xlabel('Predicted Labels')
# plt.ylabel('True Labels')
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt

# # Given values
# TP = 9742
# FP = 4320
# FN = 5758
# TN = 12320

# # Construct confusion matrix
# conf_matrix = np.array([[TN, FP], [FN, TP]])

# # Plot confusion matrix
# plt.figure(figsize=(8, 6))
# plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
# plt.title('Confusion Matrix for KNN Algorithm')
# plt.colorbar()
# tick_marks = np.arange(2)
# plt.xticks(tick_marks, ['Predicted Negative', 'Predicted Positive'])
# plt.yticks(tick_marks, ['Actual Negative', 'Actual Positive'])
# plt.tight_layout()
# plt.ylabel('True label')
# plt.xlabel('Predicted label')

# # Add text annotations
# for i in range(2):
#     for j in range(2):
#         plt.text(j, i, str(conf_matrix[i, j]), ha='center', va='center', color='black')

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# # Given values
# TP = 9265
# FP = 735
# FN = 543
# TN = 9457

# # Construct confusion matrix
# conf_matrix = np.array([[TN, FP], [FN, TP]])

# # Plot confusion matrix
# plt.figure(figsize=(8, 6))
# plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
# plt.title('Confusion Matrix for Logistic Regression')
# plt.colorbar()
# tick_marks = np.arange(2)
# plt.xticks(tick_marks, ['Real', 'Deepfake'])
# plt.yticks(tick_marks, ['Real', 'Deepfake'])
# plt.tight_layout()
# plt.ylabel('Actual Label')
# plt.xlabel('Predicted Label')

# # Add text annotations
# for i in range(2):
#     for j in range(2):
#         plt.text(j, i, str(conf_matrix[i, j]), ha='center', va='center', color='black')

# plt.show()


# import matplotlib.pyplot as plt

# # Data
# classifiers = ['Random Forest', 'KNN', 'Logistic Regression']
# recall_values = [98.01, 91.04, 81.32]  # Recall values in percentage

# # Plot
# plt.figure(figsize=(8, 6))
# plt.bar(classifiers, recall_values, color=['skyblue', 'lightcoral', 'lightgreen'])
# plt.ylim(0, 100)  # Set y-axis limit from 0 to 100%
# plt.title('Recall of Different Classifiers  in Deepfake Audio Detection')
# plt.xlabel('Classifier')
# plt.ylabel('Recall (%)')

# # Add text labels
# for i in range(len(classifiers)):
#     plt.text(i, recall_values[i] + 1, f"{recall_values[i]:.2f}%", ha='center')

# plt.show()



import matplotlib.pyplot as plt

# Data
classifiers = ['Random Forest', 'KNN', 'Logistic Regression']
f1_scores = [96.47, 68.69, 89.47]  # F1 score values in percentage

# Plot
plt.figure(figsize=(8, 6))
plt.bar(classifiers, f1_scores, color=['skyblue', 'lightcoral', 'lightgreen'])
plt.ylim(0, 100)  # Set y-axis limit from 0 to 100%
plt.title('F1 Score of Different Classifiers in Deepfake Audio Detection')
plt.xlabel('Classifier')
plt.ylabel('F1 Score (%)')

# Add text labels
for i in range(len(classifiers)):
    plt.text(i, f1_scores[i] + 1, f"{f1_scores[i]:.2f}%", ha='center')

plt.show()
