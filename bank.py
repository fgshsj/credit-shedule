from datetime import datetime, timedelta

def print_next_month(date):
    # Преобразуем строку с датой в объект datetime
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    # прибавляем месяц
    next_month = date_obj + timedelta(days=31)
    
    return next_month.strftime("%Y-%m-%d")


def payment(summ, percent, period, i):
# считаем ежемесячный платеж
    montlyPayment = (summ / period) + ((summ - (summ / period) * (i - 1)) / 100) * (percent / 12)
    
    return montlyPayment



# вводим данные о кредите
summ = float(input("enter summ:"))
percent = float(input("enter percent:"))
period = int(input("enter period:"))
date = str(input("enter date:"))

# создаем словарь
enterDict = {}

# вводим данные в словарь
for i in range(1, period+1):
  enterDict[print_next_month(date)] = payment(summ, percent, period, i)
  date = print_next_month(date)
  
print(enterDict)