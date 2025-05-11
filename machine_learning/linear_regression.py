import pandas as pd
import seaborn as sns
import numpy as np
import openpyxl as excel
from sklearn.linear_model import LinearRegression

# Load the Excel file into a DataFrame
df = pd.read_excel(r"C:\Users\srajal\Desktop\vsTutorial\pythonPractice\machine_learning\tips.xlsx")
ed = pd.read_excel(r"C:\Users\srajal\Desktop\vsTutorial\pythonPractice\machine_learning\weather_data.xlsx")
# Display the DataFrame
print(df)
print(ed)
