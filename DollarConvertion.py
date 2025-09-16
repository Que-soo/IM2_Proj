# Seatwork

USD_TO_PESO = 57.17
USD_TO_YEN = 146.67


def convert_currency(dollars):
    peso = dollars * USD_TO_PESO
    yen = dollars * USD_TO_YEN
    return peso, yen  # return multiple values (tuple)

dollar_values = [59, 200, 500]

print("Dollar($)\tPeso(P)\t\tYen(Y)")
for d in dollar_values:
    peso, yen = convert_currency(d)
    print(f"{d}\t\t{peso:.3f}\t{yen:.2f}")