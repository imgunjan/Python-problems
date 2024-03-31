shoes = ["L", "R", "R", "R", "L", "R", "L", "L", "R", "L", "R", "R", "R"]
shoe_dict = {"L": 0, "R": 0}
for word in shoes:
    shoe_dict[word] += 1

# print(shoe_dict)

pairs = min(shoe_dict["R"], shoe_dict["L"])
unmatched_pairs = abs(shoe_dict["R"] - shoe_dict["L"])

print(f"The number of matched shoes is {pairs}")
print(f"The number of Unmatched shoes is {unmatched_pairs}")
