from datetime import date
import json


def get_strip(item):
    # the strip() removes spaces at the front and end of a string
    item = item.strip()
    return item


def to_csv_format(book_title, book_isbn, book_author_last_name, book_publisher, year_published, book_price):
    csv_format = str(book_title) + ", " + str(book_isbn) + ", " + str(book_author_last_name) + ", " + \
                 str(book_publisher) + ", " + str(year_published) + ", " + str(book_price)
    print(csv_format)
    return csv_format


def to_JSON_format(csv_format):
    print(csv_format)

    data = csv_format
    count = 0
    number = data.count(",")
    array_position = []
    comma_position = 0
    print(number)
    while True:
        print(data.index(','))
        if count < number:
            comma_position = data.find(",", comma_position + 1)
            print(comma_position)
            array_position.append(comma_position)
            count = count + 1
            print(count)
        else:
            break

    object_converted = {
        "title": data[0:array_position[0]],
        "isbn": data[array_position[0]:array_position[1]],
        "author_last_name": data[array_position[1]:array_position[2]],
        "book publisher": data[array_position[2]:array_position[3]],
        "year_published": data[array_position[3]:array_position[4]],
        "price": data[array_position[4]:]
    }

    converted_to_json = json.dumps(object_converted)

    # the result is a JSON string:
    print(converted_to_json)

    print("The JSON Formatted String:")





def get_book_info():
    book_title = input("enter book title: ").title()
    book_title = get_strip(book_title)
    print(book_title)

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

    book_author_last_name = input("enter author last name: ")
    while True:
        if book_author_last_name.isalpha():
            book_author_last_name = get_strip(book_author_last_name).title()
            print(book_author_last_name)
            break
        else:
            book_author_last_name = input("Only enter alphabets for the author's last name: ")

    book_publisher = input("enter book publisher: ")
    book_publisher = get_strip(book_publisher)
    print(book_publisher)

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

    while True:
        try:
            book_price = "{:.2f}".format(float(input("enter price: ")))
            print(book_price)
            break
        except ValueError:
            print("Please try again. It must be a number")

    print(book_price)
    csv_format = to_csv_format(book_title, book_isbn, book_author_last_name, book_publisher, year_published, book_price)

    print(csv_format)

    to_JSON_format(csv_format)


def main():
    get_book_info()


if __name__ == "__main__":
    main()
