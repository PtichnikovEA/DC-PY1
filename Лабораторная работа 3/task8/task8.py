money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


# TODO Оформить решение
def how_long(cap, sal, sp, inc):
    m = 0
    while cap > 0:
        m += 1  # новый месяц
        cap = cap + salary - sp  # считаем оставшиеся деньги
        sp = sp * (1 + inc)  # считаем расходы на следующий месяц
    return m - 1


month = how_long(money_capital, salary, spend, increase)
print(month)
