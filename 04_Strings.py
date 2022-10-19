device1_str = "  r3-L-n7, cisco, catalyst 2960, ios  "

# SPLIT
device1 = device1_str.split(",")
print("device1 using split:")
print("    ", device1)

# STRIP
device1 = device1_str.strip().split(",")
print("device1 using strip() and split")
print("    ", device1)