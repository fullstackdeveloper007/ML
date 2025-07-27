# Model Evaluation: Accuracy, Precision, and Recall

## 1. Accuracy

- **What it means:** How many predictions your model got right out of all predictions.
- **Formula:**
Accuracy = (Correct Predictions) / (Total Predictions)

 

- **Example:**  
If your model made 100 predictions and got 90 correct, the accuracy is 90%.

- **Use when:**  
The data is balanced (roughly equal number of 0s and 1s).

---

## 2. Precision (Total Prediction / Total Right)

- **What it means:** Of all the times your model predicted "Yes" (or 1), how many were actually correct?
- **Formula:**
Precision = True Positives / (True Positives + False Positives)

- **Example:**  
If your model said 30 people own cars and only 20 actually do, precision = 20/30 = 66.7%

- **Use when:**  
You want to **minimize false positives**.  
For example, in spam detection, you don't want to mark good emails as spam.

---

## 3. Recall (Total Truth/How many you correctly predicted)

- **What it means:** Of all the people who actually own cars, how many did your model correctly predict?
- **Formula:**
Recall = True Positives / (True Positives + False Negatives)
- 
- **Example:**  
If 40 people own cars, and your model correctly found 30 of them, recall = 30/40 = 75%

- **Use when:**  
You want to **minimize false negatives**.  
For example, in medical tests, missing a disease (false negative) can be dangerous.


