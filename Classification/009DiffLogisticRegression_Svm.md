# 📌 SVM with Linear Kernel vs Logistic Regression

## ❓ Question
**If data is linearly separable, why use SVM with linear kernel instead of logistic regression?**

---

## ✅ Short Answer

Both can work well on linearly separable data, **but SVM and logistic regression optimize different things**, which leads to different **decision boundaries** and **generalization behavior**.

---

## 🔍 Key Differences

| Feature             | Logistic Regression                        | SVM (Linear Kernel)                             |
|---------------------|---------------------------------------------|-------------------------------------------------|
| **Objective**       | Maximize likelihood (probability-based)     | Maximize margin (geometry-based)                |
| **Decision boundary**| Fits boundary using log-odds               | Finds **widest margin** separating classes      |
| **Outlier handling**| Sensitive to outliers                       | More robust due to margin                       |
| **Output**          | Probabilities                               | Class labels (distance from hyperplane)         |
| **Use case**        | Probabilistic interpretation                | Strong generalization with limited data         |

---

## 🧪 Simple Visual Understanding

- **Logistic Regression** may place the boundary closer to the points to maximize class probabilities.
- **SVM** pushes the boundary as far as possible from both classes to create a large margin.

> 💡 **SVM aims for the most "confident" separation line.**

---

## 🧑‍💻 Example Code

```python
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Linear SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
