# Практическое занятие 5
import random


def one():
    spisok = [random.randint(1, 3) for x in range(5)]
    print(spisok)
    number = int(input("Введите число: "))

    if number in spisok:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


def two():
    spisok = [random.randint(1, 100) for x in range(5)]

    print(spisok)

    for x in range(5):
        for i in range(x + 1, 5):
            if spisok[x] == spisok[i]:
                return print(spisok[x])

    print("В списке нет повторяющихся элементов")


def three():
    days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    i = 0
    zpt = ", "

    while not (1 <= i <= 6):
        i = int(input("Сколько выходных дней вы хотите: "))

        if not (1 <= i <= 6):
            print("Ошибка")

    print("Ваши выходные дни: ", zpt.join(days[-i::]))
    print("Ваши рабочие дни: ", zpt.join(days[:7 - i:]))


def four():
    group1 = ["Давлетов", "Выдровский", "Лащёв", "Федорова", "Хавалиц", "Юринов", "Семёнов", "Долмацын", "Москвитина",
              "Сергеев"]
    group2 = ["Иванова", "Нимаев", "Хомяков", "Родионов", "Иванов", "Хертухеев", "Попов", "Васильев", "Аюшеев",
              "Перфильева"]

    sport = ()

    while len(sport) < 2:
        name = random.choice(group1)

        if not (name in sport):
            sport += (name,)

    while len(sport) < 5:
        name = random.choice(group2)

        if not (name in sport):
            sport += (name,)

    times = sport.count("Иванов")
    zpt = ", "

    print("Изначальный спискок: \n", zpt.join(group1), "\n", zpt.join(group2), "\n Спортивная команда: ",
          zpt.join(sport),
          "\n Его длина: ", len(sport), "\n Алфавитный порядок: ", zpt.join(sorted(sport)),
          "\n Фамилия Иванов встречается: ", times, " раз")

# one()
# two()
# three()
# four()