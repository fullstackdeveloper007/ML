

import numpy as np
def gradient_descent(x, y):
    m_current=0
    b_current=0
    iterations=10
    n=len(x)
    learning_rate=0.08
    for i in range(iterations):
        y_predicted=m_current*x+b_current
        #print(f"y_predicted: {y_predicted},x: {x},y: {y}")    
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        
        # Vectorized form of cost function
        #cost1 = ((y-y_predicted) ** 2).mean()

        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)
        
        # Vectorized form of cost function        
        md1 = (2 / n) * np.dot((y-y_predicted), x)
        bd1 = (2 / n) * (y-y_predicted).sum()
    
        m_current-=learning_rate*md
        b_current-=learning_rate*bd
        print(f"m: {m_current}, b: {b_current}, cost: {cost}")

x=np.array([1,2,3,4,5]) 
y=np.array([5,7,9,11,13])
gradient_descent(x,y)   
`
