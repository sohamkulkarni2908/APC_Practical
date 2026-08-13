tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)

merged_tuple = tuple1 + tuple2
result = []

for item in merged_tuple:
    if item not in result:
        result.append(item)

print("Merged tuple with duplicates removed:", tuple(result))