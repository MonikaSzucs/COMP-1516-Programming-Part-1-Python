from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(file):
    while True:
        if re.search(r"^[a-zA-Z0-9]{1,8}.txt$", file):
            file_script = open(file, "w")
            position = 0
            for country, capital in countries_capitals_dictionary.items():
                if position == 0:
                    file_script.write("The capital of %s is %s." % (country, capital))
                    position += 1
                else:
                    file_script.write("\nThe capital of %s is %s." % (country, capital))
            file_script.close()
            break
        else:
            file = input("Must be of length 1-8 characters, plus a “.txt” file extension. Please enter a file name: ")


def save_capitals():
    print("CHECKING save capitals")
    for capital_found in capitals:
        if re.search("^[aeiouAEIOU][A-Za-z0-9]*", capitals):
            print(capital_found)


def main():
    print("I should not be called")

if __name__ == '__main__':
    main()
