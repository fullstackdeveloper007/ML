### **A. AdaBoost (Adaptive Boosting)**
- **Base learners**: Usually decision stumps (1-split trees).
- After each learner:
  - Calculate **total error** (weighted).
  - Calculate **amount of say** (α) → weight of the learner in final prediction.
  - Increase weights of misclassified samples.
- Combine learners via weighted voting.

**Example:**
Dataset of animals:
- Tree 1: Splits on "Has feathers?" → misses penguins.
- Tree 2: Focuses on penguins → splits on "Can swim?".
- Tree 3: Corrects remaining mistakes.

✅ **Pros:** Simple, interpretable, handles moderate noise.  
❌ **Cons:** Sensitive to extreme noise.

# AdaBoost: Total Error and Amount of Say (α)

## 1. Total Error (ε)
Think of it as:

> **"The sum of the weights of the samples my model got wrong."**

**Formula (normalized weights):**
<img width="202" height="70" alt="image" src="https://github.com/user-attachments/assets/2af32962-56bd-46ba-8254-d1aef7863ad0" />

​
Where:
- \( w_i \) = weight of the \( i^{th} \) training sample.
- Only **misclassified** samples are included in the sum.

---

### Example:
We have 5 samples:

| Sample | Prediction | Actual | Weight |
|--------|------------|--------|--------|
| 1      | ✔          | ✔      | 0.2    |
| 2      | ✔          | ✔      | 0.2    |
| 3      | ❌         | ✔      | 0.2    |
| 4      | ❌         | ✔      | 0.2    |
| 5      | ✔          | ✔      | 0.2    |

**Wrong ones** = sample 3 and 4.

- ϵ=0.2+0.2=0.4  

---

## 2. Amount of Say (α)
Think of it as:

> **"How loud this weak model's vote should be in the final decision."**

**Formula:**
<img width="178" height="60" alt="image" src="https://github.com/user-attachments/assets/27fef89c-4db5-45c3-acb4-937b698abf39" />

Where:
- Lower ε → larger α (model is trusted more).
- Higher ε → smaller α (model is trusted less).

---

### Using the example:
<img width="495" height="156" alt="image" src="https://github.com/user-attachments/assets/bb8475fa-7984-405a-af18-cc759f29c599" />


---

## 3. Key Takeaways
- **Lower error** → bigger α → model gets **more say**.
- **Higher error** → smaller α → model gets **less say**.
- If **error = 0.5** (random guessing): α = 0 (model has no say).

---

## 4. Intuition
Think of each weak learner as a **juror**:
- Total error = how often this juror is wrong (weighted by case importance).
- Amount of say = how loud their voice is in the final verdict.
- Weak jurors (high error) get a softer voice. Strong jurors (low error) get a louder voice.

# Notes
<img width="920" height="550" alt="image" src="https://github.com/user-attachments/assets/2f2c7585-0685-4eb4-9935-6f713699e0b3" />

<img width="896" height="621" alt="image" src="https://github.com/user-attachments/assets/1a2dcca3-53ef-4943-be2b-e474073b029d" />
