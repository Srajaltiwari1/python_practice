import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# # Load the Excel file using the second row as headers
# df = pd.read_excel(
#     r"C:\Users\srajal\Desktop\vsTutorial\pythonPractice\machine_learning\tips.xlsx",
#     header=1  # Use the second row as column names
# )

# # Print DataFrame to verify columns
# print(df.head())

# # Prepare features and target variable
# X = df[["total_bill"]]  # Independent variable
# y = df["tip"]           # Dependent variable

# # Create and train the linear regression model
# model = LinearRegression()
# model.fit(X, y)

# # Predict tip for a total bill of $35
# predicted_tip = model.predict(np.array([[35]]))
# print(f"Predicted tip for $35 bill: {predicted_tip[0]:.2f}")
df=sns.load_dataset("tips")
print(df.head())
X=df[["total_bill"]]
y=df["tip"]

model=LinearRegression()
model.fit(X,y)

p=model.predict([[50]])
print(p)