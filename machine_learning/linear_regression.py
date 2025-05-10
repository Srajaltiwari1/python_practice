import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
data= {
    'salary_before':[5000,6000,7000,4000,5500,6500,4500,7500,5800,4800],
    'salary_inc':[50000,60000,70000,40000,55000,65000,45000,75000,58000,48000],
    'height':[175,160,180,165,170,168,178,162,172,166]
}
df=pd.DataFrame(data)
print(df)
X=df[['salary_before']]
y=df['salary_inc']
model=LinearRegression()
model.fit(X,y)
model.predict[['salary_before']]