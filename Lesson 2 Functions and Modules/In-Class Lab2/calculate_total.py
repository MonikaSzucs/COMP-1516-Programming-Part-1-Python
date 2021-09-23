def calculate_total(subtotal, tax):
    # Takes subtotal and tax. Returns total amount
    amount_total = float(subtotal) + float(tax)
    amount_total = "{:.2f}".format(amount_total)
    return amount_total
