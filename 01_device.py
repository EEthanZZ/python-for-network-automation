from pprint import pprint
# dictionary represents a device
device = {
    "name": "sbx-9nkv-ao",
    "vendor": "cisco",
    "model": "Nexus 9000 C9300c Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

# SIMPLE PRINT
print("\n----------------SIMPLE PRINT---------------")
print("device: ", device)
print("device name: ", device["name"])

# PRETTY PRINT
