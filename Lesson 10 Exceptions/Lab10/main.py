from book_order_utils import validate_book_order_details


def main():
    validate_book_order_details("0021", "The title here", "author", "12345458346", "2012", "10", "20.0")


if __name__ == "__main__":
    main()
