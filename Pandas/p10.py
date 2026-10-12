import pandas as pd
data = {101: 45,102: 65,103: 30,104: 72,105: 58}

s = pd.Series(data)

print("Patient Ages:")
print(s)

print("Average Age:", s.mean())

print("Oldest Patient:")
print(s.idxmax(), s.max())

print("Youngest Patient:")
print(s.idxmin(), s.min())

print("Patients above 60 years:")
print(s[s > 60])
