"""
A script containing get_strip(), to_csv_format(), to_JSON_format(), get_book_info() and main() functions
:author: Monika Szucs
:date: October 12, 2021
"""

#  Importing date and json to properly format information throughout the script
from datetime import date
import json


def get_strip(item):
    """
        A function that will remove white spaces before and after a string
        Second Variant, parameters, return
        :param item: contains a string
        :return: returns the string that has had the leading and ending spaces removed
    """
    # the strip() removes spaces at the front and end of a string
    item = item.strip()
    return item


def to_csv_format(information):
    """
        A function that will use the parameters to format them into a csv format which will contain commas (,)
        instead of a backslash (/)
        First Variant, parameters, return
        :param information: This is for the Book Title, Book ISBN, Book Author Last Name, Book Publisher,
        Year Published, and Book Price
        :return: returns the csv_format in a string
    """
    csv_format = information.replace("/", ",")
    print(csv_format)
    return csv_format


def to_json_format(csv_format):
    """
        A function that will use csv formatted string and convert it to JSON formatting
        First Variant, parameters, return
        :param csv_format: This contains the Book Title, Book ISBN, Book Author Last Name, Book Publisher,
        Year Published, and Book Price
        :return: returns the converted_to_json in JSON format
    """
    data = csv_format
    count = 0

    # counts how many commas there are
    number = data.count(",")

    # create an array
    array_position = []
    comma_position = 0

    # appends the information into an array
    while True:
        if count < number:
            comma_position = data.find(",", comma_position + 1)
            array_position.append(comma_position)
            count = count + 1
        else:
            break

    # converted the array into an object by grabbing its positions within the arrays the information was stored
    object_converted = {
        "title": data[0:array_position[0]],
        "isbn": data[array_position[0]:array_position[1]],
        "author_last_name": data[array_position[1]:array_position[2]],
        "book publisher": data[array_position[2]:array_position[3]],
        "year_published": data[array_position[3]:array_position[4]],
        "price": data[array_position[4]:]
    }

    # converted the object to a json
    converted_to_json = json.dumps(object_converted)

    # the result is a JSON string:
    print("The JSON Formatted String:")
    print(converted_to_json)


def get_book_info():
    """
        A function that will get the books information such as the title, ISBN< author last name, publisher, published
        and book price
        Second Variant
    """
    # Grabs the Book Title
    book_title = input("enter book title: ").title()
    book_title = get_strip(book_title)
    print(book_title)

    # Grabs the Book ISBN but checks to make sure it is 10 digits
    book_isbn = input("enter book ISBN: ")
    while True:
        if book_isbn.isnumeric():
            if len(str(book_isbn)) == 10:
                book_isbn = get_strip(book_isbn)
                print(book_isbn)
                break
            else:
                book_isbn = input("The book ISBN must be 10 digits: ")
        else:
            book_isbn = input("Only enter numerics for the book ISBN: ")

    # Grabs the Authors Last Name. Checks to make sure it is only one word in alphabets.
    # Then puts it into its proper formatting.
    book_author_last_name = input("enter author last name: ")
    while True:
        if book_author_last_name.isalpha():
            book_author_last_name = get_strip(book_author_last_name).title()
            print(book_author_last_name)
            break
        else:
            book_author_last_name = input("Only enter alphabets for the author's last name: ")

    # Grabs the Book Publisher
    book_publisher = input("enter book publisher: ")
    book_publisher = get_strip(book_publisher)
    print(book_publisher)

    # Grabs the year published. Makes sure it is numeric, only 4 digits and is less than or equal to
    # today's current year
    year_published = input("enter year published: ")
    todays_date = date.today()

    while True:
        if year_published.isnumeric():
            if len(str(year_published)) == 4 and int(year_published) <= int(todays_date.year):
                print(year_published)
                break
            else:
                year_published = input("enter year published in 4 digits and less than or equal to current year: ")
        else:
            year_published = input("Only enter in 4 digits: ")

    # Grabs the Price of the Book. Then converts it to two decimal places.
    while True:
        try:
            book_price = "{:.2f}".format(float(input("enter price: ")))
            print(book_price)
            break
        except ValueError:
            print("Please try again. It must be a number")

    print(book_price)

    information = book_title + "/" + book_isbn + "/" + book_author_last_name + "/" + book_publisher + "/" + \
                  year_published + "/" + book_price
    return information


def main():
    information = get_book_info()
    print(information)

    # sends the Book Title, Book ISBN, Book Author Last Name, Book Publisher, Year Published and Book Price to the
    # function csv_format()
    csv_format = to_csv_format(information)

    # Sends the csv_formatted information to convert it to JSON formatting
    to_json_format(csv_format)


if __name__ == "__main__":
    main()
