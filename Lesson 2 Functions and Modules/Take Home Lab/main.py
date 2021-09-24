"""
Second Lab by Monika Szucs
"""
import utilities


def main():
    radius_circle = input("enter the radius of a circle in cm:",)
    utilities.calculate_circle_area(radius_circle)
    radius_sphere = input("enter the radius of a sphere in cm:",)
    utilities.calculate_sphere_volume(radius_sphere)
    utilities.calculate_BMI()
    utilities.calculate_hypotenuse()


if __name__ == "__main__":
    main()