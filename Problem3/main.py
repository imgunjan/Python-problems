import re

random_string = "69358 6fg5a 2077-12-2 2077/12/15 9806006350 9849990099 78956232223"
mapped_dict = {"date": [], "phone_num": [], "zip_code": [], "unknown": []}
elements = random_string.split()

for word in elements:
    if re.match(r"[0-9]{1,4}[\-\.\,\/ ][0-9]{1,2}[\-\.\,\/ ][0-9]{1,4}", word):
        mapped_dict["date"].append(word)
    elif re.match(r"\b98\d{8}\b", word):
        mapped_dict["phone_num"].append(word)
    elif re.match(r"\b\d{5}\b", word):
        mapped_dict["zip_code"].append(word)
    else:
        mapped_dict["unknown"].append(word)

print(mapped_dict)
