from sklearn.metrics import log_loss

# 实际的类别标签
actual_labels = [0, 1, 0, 1, 1, 0, 0]
# 模型预测的概率
predicted_probabilities = [0.2, 0.8, 0.3, 0.7, 0.9, 0.1, 0.4]

# 计算Log Loss
logloss = log_loss(actual_labels, predicted_probabilities)

print("Log Loss：", logloss)
