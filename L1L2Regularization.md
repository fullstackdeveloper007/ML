# L1 and L2 Regularization in Machine Learning

Regularization is a technique used in machine learning to prevent **overfitting** by discouraging overly complex models. It does this by **adding a penalty** to the loss function based on the size of the model's coefficients.

---

## 🔢 Standard Loss Function (Without Regularization)

Most models optimize the **Mean Squared Error (MSE)**:

```
Loss = MSE = (1/n) * Σ (y_true - y_pred)^2
```

Where:

* `y_true` is the actual target value
* `y_pred` is the predicted value
* `n` is the number of data points

---

## 🧮 L2 Regularization (Ridge Regression)

```
Loss = MSE + λ * Σ (β_i)^2
```

* Adds the **sum of squared coefficients** to the MSE.
* Penalizes large weights.
* Shrinks coefficients **toward 0**, but **not exactly 0**.
* Encourages **all features** to contribute a little.

### ✅ Use when:

* All features are useful.
* Multicollinearity is present.

---

## 🧮 L1 Regularization (Lasso Regression)

```
Loss = MSE + λ * Σ |β_i|
```

* Adds the **sum of absolute values** of coefficients.
* Can shrink some coefficients **exactly to 0**.
* Performs **feature selection**.
* Creates **sparse models**.

### ✅ Use when:

* You believe **only a few features** are important.
* You want automatic feature selection.

---

## 🔍 Key Concept: Why Add Penalty?

Adding a penalty to MSE:

* **Increases the loss**.
* Forces the model to balance accuracy with simplicity.
* Encourages **smaller coefficient values**, reducing model complexity.

> "It adds to MSE but somehow forces model to choose lesser value of coefficient" — Exactly! That's the point of regularization.

---

## 🔁 Comparison Summary

| Feature            | L1 (Lasso)                   | L2 (Ridge)                      |
| ------------------ | ---------------------------- | ------------------------------- |
| Penalty            | Sum of absolute values       | Sum of squares                  |
| Coefficient effect | Some become **0**            | Shrinks but not 0               |
| Feature selection  | Yes                          | No                              |
| Use case           | Sparse model, fewer features | Stable model with many features |

---

## 📌 Final Thoughts

Regularization is a **bias-variance tradeoff** tool. It encourages models to **generalize better** by reducing reliance on noisy or unimportant features.

* L1 = simpler model (automatic feature selection)
* L2 = more stable model (reduces large coefficients)

Tune `λ` (lambda) carefully to find the right balance between underfitting and overfitting.

---
