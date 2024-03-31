shoes = ["L", "R", "R", "R", "L", "R", "L", "L", "R", "L", "R", "R", "R"]
left_shoes = []
right_shoes = []
for word in shoes:
    if word == "R":
        right_shoes.append(word)
    else:
        left_shoes.append(word)

# print(right_shoes)
# print(left_shoes)

pairs = min(len(right_shoes), len(left_shoes))
unmatched_pairs = abs(len(right_shoes) - len(left_shoes))

print(f"The number of matched shoes is {pairs}")
print(f"The number of Unmatched shoes is {unmatched_pairs}")
