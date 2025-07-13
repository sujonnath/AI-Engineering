import numpy as np

from sklearn.linear_model import LinearRegression

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([[35],[45],[55],[65],[80]])


model  = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)
print(y_pred)

# Depth MathmaticalExplanation
p = np.array([[1],[2],[3],[4],[5]])
q = np.array([[35],[45],[55],[65],[80]])

x_mean = np.mean(p)
y_mean = np.mean(q)
numerator = np.sum( (x-x_mean)*(y-y_mean))
denominator = np.sum((x-x_mean)**2)

m = numerator/denominator
b=y_mean-m*x_mean
print("\n")
print('slope(m)',m)
print("\n")
print('intercept(b)',b)

p_new = 7
q_pred = m*p_new+b
print('Predicted value: ',q_pred)

import matplotlib.pyplot as plt


plt.scatter(x,y,color='blue',label='original data')
plt.plot(x,y_pred,color='red',label ='fitted Line')

#plt.scatter(x,y,color='blue',label='original data')
#plt.plot(x,y_pred,color='red',label ='fitted Line')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

model.predict([[4.25]])