fruit_infos = [
    ("apple", "Appy"),
    ("mango", "Frooti"),
    ("Grapes", "Wine"),
    ("orange", "Tropicana"),
]
fruit_list = ["apple", "mango", "litchi", "apple", "Grapes", "Guava"]
new_mapped_dict = {}

# for fruit in fruit_list:
#     if fruit.lower() in fruit_infos:
#         new_mapped_dict[fruit] = fruit_infos[fruit.lower()]
#     else:
#         new_mapped_dict[fruit] = "unknown"

for fruit in fruit_list:
    is_there = False
    for infos in fruit_infos:
        if infos[0].lower() == fruit.lower():
            new_mapped_dict[fruit] = infos[1]
            is_there = True
            break
        if not is_there:
            new_mapped_dict[fruit] = "unknown"


print(new_mapped_dict)
