def get_tax_rate():
    while True:
        try:
            tax_rate = float(input("enter tax:"))
            if tax_rate < 1:
                return tax_rate
            else:
                print("Make sure the tax rate has been converted out of percentage format!")
        except ValueError as e:
            print("not a proper integer! Try again")