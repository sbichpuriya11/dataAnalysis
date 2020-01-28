import pandas as pd 
import matplotlib.pyplot as plt 
DF = pd.read_csv("C:\\Users\\Sagar\\Downloads\\data-set.csv") 
y = list(DF.X4s) 
plt.boxplot(y) 
plt.show() 
