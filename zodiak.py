years = [
    "Дракон",
    "Змея",
    "Лошадь",
    "Овца",
    "Обезьяна",
    "Петух",
    "Собака",
    "Свинья",
    "Крыса",
    "Бык",
    "Тигр",
    "Заяц",
]
year = int(input())


def is_years(year):
    if year % 12 == 0:
        res = 12 - 8
    else:
        res = (year % 12) - 8
    # if res < 0:
    # res -= 1
    return years[res] # проверка


print(is_years(year))
