device1_str = "  r3-L-n7, cisco, catalyst 2960, ios  "

# SPLIT
device1 = device1_str.split(",")
print("device1 using split:")
print("    ", device1)

# STRIP
device1 = device1_str.strip().split(",")
print("device1 using strip() and split")
print("    ", device1)

# REPLACE, REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 using replace() to replace all blanks: \n    ", device1)

# REMOVE BLANKS, REPLACE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", "").replace(",", " : ")
print("device 1 replaced blanks, comma to colon:")
print("    ",  device1_str_colon)


# USING FOR lOOP to remove blanks
device_list = []
for i in device1_str.split(","):
    x = i.strip()
    device_list.append(x)
print("    ", device_list)