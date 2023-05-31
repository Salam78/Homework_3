usd_rate = 420
eur_rate = 510
rub_rate = 5.8

amount_kzt = float(input("Введите сумму в тенге: "))
currency_choice = int(input("Выберите валюту:\n[1] USD\n[2] EUR\n[3] RUB\n"))

if currency_choice == 1:
    converted_amount = amount_kzt / usd_rate
    currency_symbol = "USD"
elif currency_choice == 2:
    converted_amount = amount_kzt / eur_rate
    currency_symbol = "EUR"
elif currency_choice == 3:
    converted_amount = amount_kzt / rub_rate
    currency_symbol = "RUB"
else:
    print("Некорректный выбор валюты.")
    exit()

print(f"{converted_amount:.2f} {currency_symbol}")
input("press any key to close window")
