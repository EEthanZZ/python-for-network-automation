from random import choice
import string

from tabulate import tabulate


def create_devices(num_device=1, num_subnets=1):
    created_devices = list()
    if num_device > 254 or num_subnets > 254:
        print("wrong")
        return created_devices

    for i in range(1, num_subnets+1):
        for x in range(1, num_device+1):
            device = dict()
            device["name"] = (
                    choice(["r2", "r3", "r4", "r6", "r10"])
                    + choice(["L", "U"])
                    + choice(string.ascii_letters)
            )
            device["vendor"] = choice(["cisco", "juniper", "asista"])
            if device["vendor"] == "cisco":
                device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
                device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).101"])
            elif device["vendor"] == "juniper":
                device["os"] = "junos"
                device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
            elif device["vendor"] == "asista":
                device["os"] = "eos"
                device["version"] = choice(["a", "b", "c"])
            device["ip"] = "10.0." + str(i) + "." + str(x)
            created_devices.append(device)

    return created_devices
    # devices = create_devices(5, 4)
    # print(tabulate(devices, headers="keys"))
