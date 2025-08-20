import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title="6th sem Marks"
head=["Subject", "Marks"]
data= [
    ["SE",10],
    ["IPCV",10],
    ["NLP",10],
    ["Big Data",10],
    ["Robotics",9],
    ["IPCV Lab",10],
    ["Blender",9],
    ["Major Project",10]
]
sheet.append(head)
for row in data:
    sheet.append(row)
wb.save("marks.xlsx")
print("Excel sheet created")
