import math


def get_player_pos() -> None:

    print("Get first set of coordinates")
    coordinates = (float(input("Enter new coordinate as float int format 'x,y,z:")))


def ft_coordinate_system() -> None: 
    print("=== Game Coordinate System ===")
    get_player_pos()


if __name__ == "__main__":
    ft_coordinate_system()
