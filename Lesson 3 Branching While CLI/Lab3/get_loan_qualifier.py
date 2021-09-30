def loan_qualifier():
    print(" running load qualifier")
    monthly_salary = int(input("enter your monthly salary: "))
    number_of_years_employed = int(input("enter the number of years employed: "))
    annual_income = (float(monthly_salary) * 12)

    if annual_income >= 50000 and number_of_years_employed >= 3:
        print("you qualify for a loan")

    elif annual_income <= 50000 and number_of_years_employed >= 3:
        print(" your annual income must be 50000  or more you don\'t qualify for a loan")

    elif number_of_years_employed < 3:
        print(" you must be employed for 3 years or more you don\'t qualify for a loan")
