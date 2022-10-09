from tabulate import tabulate

from resouces import create_devices

if __name__ == '__name__':
    device = create_devices(5, 4)
    print("\n", tabulate(device, headers="keys"))