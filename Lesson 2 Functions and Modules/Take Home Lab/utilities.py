"""
Second Lab by Monika Szucs
"""
import math


def calculate_circle_area(radius_circle):
    """
    This is a function that will calculate the radius of the circle calculated by the formula area = pi*(r**2)
    First Variant, parameters, and return
    :param radius_circle: the radius of the circle entered in by the user
    :return: The area of the circles radius, area = pi*(r**2)
    """
    area = math.pi * (int(radius_circle)**2)
    print("the area of circle is", area)
    return area
    # return the area of the circles radius calculated by area = pi*(r**2)


def calculate_sphere_volume(radius_sphere):
    """
    This
    Second Variant, parameters, and return
    :param radius_sphere:
    :return:
    """
    volume = (4/3) * math.pi * (int(radius_sphere)**3)
    print("the volume of the sphere is:", volume)
    return volume


def calculate_BMI():
    """
    This
    Third Variant, parameters, and return
    :return:
    """
    weight = input("enter the weight in kilograms:")
    height = input("enter the height in meters:")
    body_mass_index = float(weight) / (float(height) * float(height))
    print("the Body Mass Index is", body_mass_index)
    return body_mass_index


def calculate_hypotenuse():
    """
    This
    Fourth Variant, parameters, and return
    :return:
    """
    side_a = input("enter the length of side A in cm:")
    side_b = input("enter the length of side B in cm:")
    hypotenuse_length = math.hypot(float(side_a), float(side_b))
    print("the hypotenuse length of the right triangle is:", hypotenuse_length)
    return hypotenuse_length

