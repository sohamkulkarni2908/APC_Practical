import pandas as pd
data = {"Soham": 80,"Nisarg": 95,"Nikhil": 65,"Shubham": 92,"Chetan": 70}

s = pd.Series(data)

print("Student Attendance:")
print(s)

print("Average Attendance:", s.mean())

print("\nAttendance below 75%:")
print(s[s < 75])

print("\nAttendance above 90%:")
print(s[s > 90])

print("\nHighest Attendance:", s.max())
