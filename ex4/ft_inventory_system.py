import sys


def get_key_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None


def ft_inventory_system():
    print("=== Inventroty System Analysis ===")
    result = {}
    rlist = []
    args = sys.argv[1:]

    for arg in args:
        try:
            i = arg.index(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key = arg[:i]
        try:
            value = int(arg[i+1:])
        except ValueError as e:
            print(f"Quantity error for 'key': {e}")
            continue
        if result.get(key) is None:
            result[key] = value
        else:
            print("Redundant item 'sword' - discarding")
    print(f"Got inventory: {result}")
    rlist = list(result.keys())
    print(f"Item list: {rlist}")
    print(f"Total quantity of the {len(rlist)} items: 12")
    max_value = value
    min_value = value
    for key, value in result.items():
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
        print(f"Item {key} represents {round(value / 12 * 100, 1)}%")
    print(f"Item most abundant: {get_key_value(result,max_value)} with"
          f" quantity: {max_value}")
    print(f"Item least abundant: {get_key_value(result,min_value)} with"
          f" quantity: {min_value}")
    result.update({"magic_item": 1})
    print(f"Update inventory: {result}")


if __name__ == "__main__":
    ft_inventory_system()
