import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([[35],[45],[55],[65],[80]])

# Ridge Regression
ridge = Ridge()
ridge.fit(x,y)

y_predict_ridge = ridge.predict([[8]])
print(y_predict_ridge)

#Lasso Regression
lasso= Lasso()
lasso.fit(x,y)
y_predict_lasso = lasso.predict([[6.5]])
print(y_predict_lasso)

test_data =([6.5])
test_data_new =([[6.5],[7.6],[8.9],[11.4],[34.7]])
y_predict_ridge_new = ridge.predict(test_data_new)
y_predict_lasso_new = lasso.predict(test_data_new)

plt.figure(figsize=(12,6))
plt.scatter(x,y,label='Orginal data')
plt.plot(test_data,y_predict_ridge, label= 'Ridge Regression')
plt.plot(test_data,y_predict_lasso, label= 'Lasso Regression')

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(12,6))
plt.scatter(x,y,label='Orginal data')
#plt.plot(test_data,y_predict_ridge, label= 'Ridge Regression')
#plt.plot(test_data,y_predict_lasso, label= 'Lasso Regression')
plt.plot(test_data_new,y_predict_ridge_new,'r--', label= 'Ridge Regression')
plt.plot(test_data_new,y_predict_lasso_new,'g--', label= 'Lasso Regression')

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()