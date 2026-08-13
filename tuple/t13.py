t = (10, 20, 30, 40, 50, 60)
temp_list = list(t)

temp_list[1] = 73

t = tuple(temp_list)
print("Modified tuple:", t)