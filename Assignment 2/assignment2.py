from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(file):
    print(type(file))
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


def save_capitals(file):
    print("CHECKING save capitals")
    print(file)
    file_created = open(file, "w")
    position = 0
    print()
    for capital_found in capitals:
        if (re.search(r"[aeiouAEIOU]{3}", capital_found)) and file == "vowel_vowel_vowel.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
        elif (re.search(r"[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z]{3}", capital_found)) and file == "cons_cons_cons.txt":
            print(capital_found)
            if position == 0:
                file_created.write(capital_found.lower())
                position += 1
            else:
                file_created.write("\n" + capital_found.lower())
        elif (re.search("i.+e|i+e", capital_found)) and file == "i_before_e.txt":
            print(capital_found)
    file_created.close()


def main():
    print("I should not be called")


if __name__ == '__main__':
    main()
