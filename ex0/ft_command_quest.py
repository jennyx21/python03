import sys


def ft_command_quest():
    print("=== Comand Quest ===")
    if len(sys.argv) < 2:
        print("No arguments Provided!")
    else:
        print(f"Arguments recived: {len(sys.argv) - 1}")
    print(f"program name: {sys.argv[0]}")
    i = 0
    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {sys.argv[i + 1]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
