#intermediate machine learning by sk_learn
#multi_linear_regression
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
df=sns.load_dataset('tips')
# X=df[['total_bill','size']]#for better data more variable are needed
# y=df['tip']
# model=LinearRegression()
# model.fit(X,y)
# pred=model.predict([[35.257,2]])
# print(pred)

#lets add smoker as new variable
# as ML only take numeric value and smoker is not,so encode it
df['smoker_num']=df['smoker'].map({'Yes':1,"No":0})
X=df[['total_bill','size','smoker_num']]
y=df['tip']

model=LinearRegression()
model.fit(X,y)
pre_1=model.predict([[35.527,2,1]])
print("smoke",pre_1)

pre_2=model.predict([[35.527,2,0]])
print("do not",pre_2)