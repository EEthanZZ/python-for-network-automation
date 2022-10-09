from tabulate import tabulate
from util.resouces import create_devices

# if __name__ == '__main__':
devices = create_devices(5, 4)
print(tabulate(devices, headers="keys"))
