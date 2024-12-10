name = ["Jon","kelly", "kess", "PETER"]
lower_names = []
for item in name:
 assert type(item) == str, 'non-string items in the list'
 if item.islower():
  lower_names.append(item)
print(lower_names)