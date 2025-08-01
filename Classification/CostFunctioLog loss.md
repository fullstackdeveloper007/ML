## 🧮 Cost Function: Log Loss

In Logistic Regression, the cost function used is called **Log Loss** (also known as **Binary Cross-Entropy**).

It measures the performance of a classification model whose output is a probability value between 0 and 1.

### 🔹 Formula for Log Loss (Binary Classification):

\[
\text{Log Loss} = - \frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
\]

- \( N \): Number of samples  
- \( y_i \): Actual label (0 or 1)  
- \( p_i \): Predicted probability for class 1  

### 🔸 Interpretation:
- Lower log loss = better model.
- A perfect model has a log loss of 0.
- Penalizes false predictions more harshly when the model is confident but wrong.

This cost function guides the optimization process during training to find the best parameters for minimizing classification error.
