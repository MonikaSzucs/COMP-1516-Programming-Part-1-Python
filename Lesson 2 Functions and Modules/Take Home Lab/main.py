"""
Second Lab by Monika Szucs
This file contains the main function
date: Sept 26 2021
"""
import utilities


def main():
    radius_circle = input("enter the radius of a circle in cm:",)
    calculated_circle_area = utilities.calculate_circle_area(radius_circle)
    print(" the area of circle is", calculated_circle_area)
    radius_sphere = input("enter the radius of a sphere in cm: ",)
    calculated_radius_sphere = utilities.calculate_sphere_volume(radius_sphere)
    print(" the volume of the sphere is:", calculated_radius_sphere)
    calculated_BMI = utilities.calculate_BMI()
    print(" the Body Mass Index is", calculated_BMI)
    calculated_hypotenuse = utilities.calculate_hypotenuse()
    print("the hypotenuse length of the right triangle is: ", calculated_hypotenuse)


if __name__ == "__main__":
    main()

