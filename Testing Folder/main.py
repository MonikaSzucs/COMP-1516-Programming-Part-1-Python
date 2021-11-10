

def main():
    with open('books.txt') as file:
        lines = [line.rstrip() for line in file]
    for i, word in enumerate(lines):
        lines[i] = word.upper()
    print(lines)


if __name__ == "__main__":
    main()
