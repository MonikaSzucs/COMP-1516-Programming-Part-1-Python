
def get_countries(substring):
    file_script = open("lab-week-8.txt", "w")
    print(len(substring))
    for country in substring:

            file_script.write(country + " \n")
    file_script.close()


def get_capitals(substring):
    pass


def get_file_data():
    pass

