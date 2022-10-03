# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 3, 2022
# This program calculates the, volume, surface area, base area, and face area
# of a pentagonal pyramid

# imports math library
import math


def main():
    # set variables from user input
    units = input("What units are you using? ")
    height = float(input("What is the height of your pentagonal pyramid? "))
    base_length = float(
        input("What is the length of one base segment of your pentagonal pyramid? ")
    )

    # calculate volume, surface area, base area, and face area
    volume = (5 / 12) * math.tan(54 * (math.pi / 180)) * height * base_length**2
    face_area = (base_length / 2) * math.sqrt(
        height**2 + ((base_length * math.tan(54 * (math.pi / 180)) / 2) ** 2)
    )
    base_area = (5 / 4) * math.tan(54 * (math.pi / 180)) * base_length**2
    surface_area = base_area + 5 * face_area

    # adds extra line
    print("")

    # displays above information
    print(f"The volume of your pentagonal pyramid is {str(volume) + units}³")
    print(
        f"The surface area of your pentagonal pyramid is {str(surface_area) + units}²"
    )
    print(f"The face area of your pentagonal pyramid is {str(face_area) + units}²")
    print(f"The base area of your pentagonal pyramid is {str(base_area) + units}²")


if __name__ == "__main__":
    main()
