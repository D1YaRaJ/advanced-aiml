import pandas as pd
data={"Subject":["SE","IPCV","NLP","Big Data","Robotics","IPCV Lab","Blender","Major Project"],
      "Marks":[10,10,10,10,9,10,9,10]}
df=pd.DataFrame(data)
print(df)

from tabulate import tabulate
data=[["SE",10],["IPCV",10],["NLP",10],["Big Data",10],["Robotics",9],["IPCV Lab",10],["Blender",9],["Major Project",10]]
head=["Subject","Marks"]
print(tabulate(data,headers=head,tablefmt="grid"))
