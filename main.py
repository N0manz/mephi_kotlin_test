import random
# В тз не указано, что у юзера есть другие валюты,но думаю это подразумевается
userBalance = {
    "RUB": 1_000_000,
    "USD": 0,
    "EUR":0,
    "USDT": 0,
    "BTC": 0
}

terminalBalance = {
    "RUB": 10_000,
    "USD": 1_000,
    "EUR": 1_000,
    "USDT": 1_000,
    "BTC": 1.5
}

# В тз не прописано какие курсы валют брать поэтому накидал текущие
exchangeRates = {
    "RUB/USD": 0.011,
    "RUB/EUR": 0.01,
    "USD/EUR": 0.91,
    "USD/USDT": 0.99,
    "USD/BTC": 0.000017,
    "USD/RUB": 90.90909,
    "EUR/RUB": 100.0,
    "EUR/USD": 1.0989,
    "USDT/USD": 1.0101,
    "BTC/USD": 58823.52941
}

# Обновляем все курсы валют после оппераций
def updateMoney():
    for pair in exchangeRates:
        exchangeRates[pair] *= round(1 + random.uniform(-0.05, 0.05), 5)


def Exchange(pair, value):
    if pair not in exchangeRates:
        print("Такое мы не меняем")
        return

    fromCurrency, toCurrency = pair.split('/')
    
    if value > userBalance[fromCurrency]:
        print("Не хватает денег? Переходи по ссылке ниже к нашему спонсору 1Хребет")
        return

    rate = exchangeRates[pair]
    convertedAmount = round(value * rate, 6)

    if convertedAmount > terminalBalance[toCurrency]:
        print("У нас нет таких денег")
        return

    userBalance[fromCurrency] -= value
    userBalance[toCurrency] += convertedAmount
    terminalBalance[fromCurrency] += value
    terminalBalance[toCurrency] -= convertedAmount

    updateMoney()
    print(f"Обмен завершен: {value} {fromCurrency} на {convertedAmount} {toCurrency}")
    print(f"Текущие курсы: {exchangeRates}")

def main():
    while True:
        comand = input("Введите комнанду exchange/exit/balance/terminal ")
        if comand == "exit":
            break
        elif comand == "balance":
            print(userBalance)
        elif comand == "terminal":
            print(terminalBalance)
        elif comand == "exchange":
            print("Доступные обмененный курсы:")
            print(*exchangeRates.keys())
            pair = input("Введи пару для обмена в формате RUB/USD(привденно в качестве примера) ")
            try:
                value = float(input("Введите сумму для обмена: "))
                Exchange(pair, value)
            except ValueError:
                print("Некорректная сумма. Попробуйте снова.")
        else:
            print("Неизвестная команда")
            
if __name__ == "__main__":
    main()