from data import countries, capitals


def get_countries(substring):
    file_script = open("lab-week-8.txt", "w")
    initial = 0
    for country in countries:
        if substring.lower() in country.lower() and initial == 0:
            file_script.write(country)
            initial += 1
        elif substring.lower() in country.lower():
            file_script.write("\n" + country)
    file_script.close()


def get_capitals(substring):
    file_script = open("lab-week-8.txt", "a")
    for capital in capitals:
        if substring.lower() in capital.lower():
            file_script.write("\n" + capital)
    file_script.close()


def get_file_data():
    file_script = open("lab-week-8.txt", "r")
    for places in file_script:
        print(places.strip('\n'))

