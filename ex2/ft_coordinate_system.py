#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        cords_str = input("Enter new coordinates as floats "
                          "in format 'x,y,z': ")
        cords = cords_str.split(",")
        try:
            x_str, y_str, z_str = cords
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            x = float(x_str)
        except ValueError:
            print(f"Error on parameter '{x_str}': "
                  f"could not convert string to float: '{x_str}'")
            continue
        try:
            y = float(y_str)
        except ValueError:
            print(f"Error on parameter '{y_str}': "
                  f"could not convert string to float: '{y_str}'")
            continue
        try:
            z = float(z_str)
            return (x, y, z)
        except ValueError:
            print(f"Error on parameter '{z_str}': "
                  f"could not convert string to float: '{z_str}'")
            continue


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    cords1 = get_player_pos()
    print(f"Got a first tuple: ({cords1[0]}, {cords1[1]}, {cords1[2]})")
    print(f"It includes: X={cords1[0]}, Y={cords1[1]}, Z={cords1[2]}")
    dtc = math.sqrt(cords1[0]**2 + cords1[1]**2 + cords1[2]**2)
    print(f"Distance to center: {round(dtc, 4)}")
    print("Get a second set of coordinates")
    cords2 = get_player_pos()
    temp = (cords1[0] - cords2[0])**2 + (cords1[1] - cords2[1])**2
    dbc = math.sqrt(temp + (cords1[2] - cords2[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(dbc, 4)}")
