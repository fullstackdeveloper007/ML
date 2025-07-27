# Gradient Discent 

```python
def gradient_descent(x,y,lr=0.01,epochs=3000):
    m,b=0.0,0.0
    
    for epoch in range(epochs):
        y_pred= m*x + b
        error= y- y_pred
        cost = np.mean(error**2)
        
        dm=-2 * np.mean(x * error) #derivate Of M
        db=-2 * np.mean(error) #derivate Of B
        
        b= b - (lr * db) #update b
        m= m - (lr * dm) #update m
        
        print(f'Epoch {epoch}, Cost: {cost}, m: {m}, b: {b}')
        

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5,7,9,11,13])
    gradient_descent(x, y)

```

# Gradient Discent using Scikit Learn
```python
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv("home_prices_mv.csv")
df.sample(5)

model=LinearRegression()
model.fit(df[["area_sqr_ft","bedrooms"]],df["price_lakhs"]) # Training the model

model.predict([[1500,2]])
```
### Passing dataframe for training the model 
```python
test=pd.DataFrame([
    {'area_sqr_ft':1500,"bedrooms":2},
    {'area_sqr_ft':2000,"bedrooms":2}
])

model.predict(test) O/s array([75.78971293, 89.13769907]) #If we will pass the dataframe the warning message will not come
model.coef_,model.intercept_ O/S: (array([2.66959723e-02, 3.10399604e+01]), -26.334166207939006)

```
