import math


def task20_int():
    """
    Знайти кількість повних годин, що минули з початку останньої години
    """

    # Введіть кількість секунд
    N = int(input("Введіть кількість секунд: "))

    # Знайдемо кількість годин, що минуло з початку останньої години
    minutes = (N // 3600)
    print("Кількість повних хвилин з початку останньої години:", minutes)


def task29():
    """
    Функція для розрахунку прикладу.
    """
    try:
        x = float(input("Введіть x: "))
        num = math.cbrt(math.fabs(((x ** 3) / 4) - (math.sin(x ** 3) * math.sin(x ** 3)) * 2)) * math.log(math.fabs(x),
                                                                                                          5)
        denum = (2 ** x) * math.sqrt(math.fabs(3 * x + 2.5 * math.fabs(math.tan(x))))
        if denum == 0:
            print("Ділення на нуль неможливе.")
        else:
            y = num / denum
            print(f"Значення y при x={x}: {y}")
    except ValueError:
        print("Помилка: Введіть коректне числове значення для x.")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе.")


def task4_bool():
    """
Перевірити істинність висловлювання: «Справедливі нерівності A> 2 і B ≤ 3»
"""
    try:
        a = int(input("Введіть число A: "))
        b = int(input("Введіть число B: "))
        res = a > 2 and b <= 3

        print(res)
    except ValueError:
        print("Помилка:Введіть ціле число для a, b ")


if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Кількість повних годин, що минули з початку останньої години")
        print("2. Обрахувати приклад")
        print("3. Перевірити істинність висловлювання")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            task20_int()
        elif choice == "2":
            task29()
        elif choice == "3":
            task4_bool()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")
