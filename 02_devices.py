from random import choice
import string


devices = []

for i in range(0, 5):
    devices = dict()
    devices["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )
    print(devices)
