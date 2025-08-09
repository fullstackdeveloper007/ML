# Bagging = Bootstrap Aggregating

It’s an ensemble learning technique where:  
You randomly sample the training data with replacement (bootstrap sampling).  
Train multiple models on these different samples (often the same type of model, e.g., decision trees).  
Combine their predictions (averaging for regression, majority vote for classification).  

Why Bagging Works
Different models see slightly different data → they make different errors  
Combining them reduces variance and prevents overfitting  
Works best for unstable models (small data changes → big prediction changes), like decision trees  
We do randomsampling of data in bagging, create multiple dataset from same data and pass all the dataset to ssame model  

###📌 Think of it as:
“Instead of relying on one noisy opinion, ask a bunch of people who have seen slightly different parts of the story and take the average.”

### Steps in Bagging
Draw m bootstrap samples from the dataset (same size as the original, but with replacement).
Train m separate models (often in parallel).

Combine predictions:
Classification: Majority vote (hard voting) or probability averaging (soft voting)
Regression: Average predictions

### Key Points to Remember (Interview/Practice)
- Sampling with replacement = Some points are repeated, some are left out (called out-of-bag samples)
- Out-of-Bag (OOB) error can be used as a validation score without a separate test set
- Works best on high-variance, low-bias models (like decision trees)
- Random Forest = Bagging + feature randomness
- Bagging reduces variance, but doesn’t necessarily reduce bias
- Models are trained independently (parallelizable → faster on multiple CPUs)
- More models → better performance (until it plateaus)


```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Bagging with Decision Trees
base_model = DecisionTreeClassifier()
bagging = BaggingClassifier(base_estimator=base_model, n_estimators=10, random_state=42, oob_score=True)

bagging.fit(X_train, y_train)
print("Test Accuracy:", bagging.score(X_test, y_test))
print("OOB Score:", bagging.oob_score_)


```
# Notes 
<img width="695" height="628" alt="image" src="https://github.com/user-attachments/assets/2a795bcd-2257-4f50-8aec-4dcb15ccbbe4" />
<img width="768" height="605" alt="image" src="https://github.com/user-attachments/assets/6be3f35c-32aa-4d9a-89f3-31adbc705f93" />
