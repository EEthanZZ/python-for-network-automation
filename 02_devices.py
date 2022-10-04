from random import choice
import string


devices = []

for i in range(1, 5):
    devices = dict()
    devices["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )
    devices["vendor"] = choice(["cisco", "juniper", "asista"])
    if devices["vendor"] == "cisco":
        devices["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        devices["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).101"])
    elif devices["vendor"] == "juniper":
        devices["os"] = "junos"
        devices["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    elif devices["vendor"] == "asista":
        devices["os"] = "eos"
        devices["version"] = choice(["a", "b", "c"])
    devices["ip"] = "10.0.0." + str(i)
    print(devices)
