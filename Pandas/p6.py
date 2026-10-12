import pandas as pd

data = {
    "Student_ID" : [1,2,3,4,5],
    "Name" : ["Soham","Nisarg","Nikhil","Ritesh","Chetan"],
    "Department" : ["CSE","CSE", "AIML", "ENTC","CIVIL"],
    "Total_class" : [200,200,250,200,150],
    "Attended" : [180,175,150,150,125]
}

df = pd.DataFrame(data)

df["Percentage"] = (df["Attended"]/df["Total_class"]) * 100

print("Studets having attendance below 75: ")
print(df[df["Percentage"] < 75])