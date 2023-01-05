import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('slr.csv')
a= dataset.iloc[:,:-1].values
b= dataset.iloc[:,[1,2]].values

#split the dataset into train nd test

from sklearn.model_selection import train_test_split
a_train,a_test,b_train,b_test = train_test_split(a,b,test_size=1/3,random_state=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

#fit the train
model.fit(a_train,b_train)
#predict the test
y_predict = model.predict(a_test)

plt.scatter(a_train,b_train,color='red')
plt.plot(a_train,model.predict(a_train),color='yellow')
plt.show()
plt.scatter(a_test,b_test,color='red')
plt.plot(a_test,model.predict(a_test),color='yellow')
plt.title('adv vs sales')
plt.xlabel('no.adv')
plt.ylabel('sales')
plt.show()

# performance evaluation
from sklearn import metrics
mae = metrics.mean_absolute_error(b_test,y_predict)
mse = metrics.mean_squared_error(b_test,y_predict)
print(mae)
print(mse)
