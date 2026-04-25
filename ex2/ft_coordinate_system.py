import math
# this python project is teaching us how to us tuples


def get_player_pos() -> tuple[float, float, float]:

    try:
        p_input = input("Enter new coordinate as floats int format 'x,y,z': ")
        i = 0
        coords = []
        coords = p_input.split(",")
        for coord in coords:
            float(coord)
            i += 1
        if i != 3:
            raise Exception
        else:
            player_coordinates = (float(coords[0]), float(coords[1]),
                                  float(coords[2]))
            return player_coordinates
    except ValueError as e:
        print(f"Invalid arguments: {e}")
        return get_player_pos()
    except Exception:
        print("invalid arguments: insert exact 3 arguments -> Format x,y,z")
        return get_player_pos()


def calc_distance(coord1: tuple, coord2: tuple) -> float:
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(distance, 4)


def ft_coordinates_system() -> None:
    print("=== Game Coordinate System ===")
    center = tuple([0, 0, 0])
    print("Get first set of coordinates")
    player1 = get_player_pos()
    print(f"got a first tuple:({player1[0]}, {player1[2]}, {player1[2]})")
    x1, y1, z1 = player1
    print(f"It incluedes: X={x1}, Y={y1}, Z={z1}")
    distance = calc_distance(player1, center)
    print(f"Distance to center: {distance}")
    print()
    print("Get a second set of coordinates")
    player2 = get_player_pos()
    distance2 = calc_distance(player1, player2)
    print(f"Distance between the 2 sets of coordinates: {distance2}")


if __name__ == "__main__":
    ft_coordinates_system()
