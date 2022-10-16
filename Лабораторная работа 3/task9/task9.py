salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение


def long_life(sal, sp, m, inc):
    money = 0
    for i in range(0, m):
        money += (sp * pow(1 + inc, i)) - sal  # сколько денег надо дополнительно каждый месяц
    return money


need_money = long_life(salary, spend, months, increase)
print(round(need_money))
