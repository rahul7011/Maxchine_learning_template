# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#where X is independent i.e, Yoe whereas y is dependent i.e, salary
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# =============================================================================
 #To check the accuracy and the rootmeansquare error
# =============================================================================
# =============================================================================
#  from sklearn.metrics import mean_squared_error,r2_score
#  lie_mse1=mean_squared_error(y_train,regressor.predict(X_train))
#  line_rmse1=np.sqrt(lie_mse1)
#  print(line_rmse1)
#  r2_score(y_train,regressor.predict(X_train))
#  
#  
#  from sklearn.metrics import mean_squared_error,r2_score
#  lie_mse2=mean_squared_error(y_test,y_pred)
#  line_rmse2=np.sqrt(lie_mse2)
#  print(line_rmse2)
#  r2_score(y_test,y_pred)
# =============================================================================
# 
# =============================================================================

 
# =============================================================================
# =============================================================================
# 
# plt.title('Simple linear regression with FD')
# plt.xlabel('random number')
# plt.ylabel('value of theta')
# plt.scatter(X_train,y_train,c='red')
# plt.plot(X_test,y_pred,c='purple')
# plt.show()
# 
# 
# =============================================================================
# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()