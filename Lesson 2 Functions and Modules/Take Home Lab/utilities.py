"""
Second Lab by Monika Szucs
A script that will run: calculate_circle_area(radius_circle),
                        calculate_sphere_volume(radius_sphere),
                        calculate_BMI(),
                        calculate_hypotenuse()
date: Sept 26 2021
"""
import math


def calculate_circle_area(radius_circle):
    """
    This is a function that will calculate the radius of the circle calculated by the formula area = pi*(r**2)
    First Variant, parameters, and return
    :param radius_circle: the radius of the circle to be calculated
    :return: The area of the circles radius, area = pi*(r**2)
    """
    area = math.pi * (int(radius_circle)**2)
    return area
    # return the area of the circles radius calculated by area = pi*(r**2)


def calculate_sphere_volume(radius_sphere):
    """
    This is a function that will calculate the radius of a sphere calculated by
    the formula (4/3) * math.pi * (int(radius_sphere)**3)
    Second Variant, parameters, and return
    :param radius_sphere: the radius of a sphere to be calculated
    :return: The volume of the radius sphere
    """
    volume = (4/3) * math.pi * (int(radius_sphere)**3)
    return volume
    # return that volume of the sphere's radius


def calculate_BMI():
    """
    This is a function that will calculate the BMI
    Third Variant, parameters, and return
    :return: The Body Mass Index
    """
    weight = input("enter the weight in kilograms:")
    height = input("enter the height in meters:")
    body_mass_index = float(weight) / (float(height) * float(height))
    return body_mass_index
    # return the Body Mass Index by calculating the BMI


def calculate_hypotenuse():
    """
    This is a function that will calculate teh hypotenuse
    Fourth Variant, parameters, and return
    :return: The Hypotenuse Length
    """
    side_a = input("enter the length of side A in cm:")
    side_b = input("enter the  length of side B in cm:")
    hypotenuse_length = math.hypot(float(side_a), float(side_b))
    return hypotenuse_length
    # return the Hypotenuse Length
