def get_strip(item):
    item = item.strip()
    return item

def to_csv_format():
    pass

def get_book_info():
    book_title = input("enter book title: ")
    book_title = get_strip(book_title)
    print(book_title)

    book_isbn = input("enter book ISBN: ")
    book_isbn = get_strip(book_isbn)
    print(book_isbn)

    book_author_last_name = input("enter author last name: ")
    book_author_last_name = get_strip(book_author_last_name)
    print(book_author_last_name)

    book_publisher = input("enter book publisher: ")
    year_published = input("enter year published: ")
    book_price = input("enter price: ")


def main():
    get_book_info()


if __name__ == "__main__":
    main()

    