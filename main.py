import math


def if12():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    c = int(input("Введіть третє число: "))
    if a < b and a < c:
        print(a)
    if b < a and b < c:
        print(b)
    if c < a and c < b:
        print(c)


def task2():
    it = 0
    r = int(input("Введіть r: "))
    n = int(input("Введіть кількість точок: "))
    for i in range(n):
        print(f"Введіть координати точки {i + 1}:")
        x = float(input("x: "))  # Введення координати x
        y = float(input("y: "))  # Введення координати y
        if (x - r) ** 2 + (y - r) ** 2 <= r * r and x > r and -y + (2 * r) > x:
            it = it + 1
        elif (x + r) ** 2 + (y + r) ** 2 <= r * r and x > -r and -y - (2 * r) > x:
            it = it + 1

    print(f"Точок потрапляє у фігуру:{it}")


def task27():
    E = 1e-5
    G = 1e5
    current_sum = 0
    n = 1
    u = 1
    x = int(input("Введіть x:"))
    while abs(u) >= E and abs(u) <= G:
        u = ((-1) ** n * x ** (n - 1) * math.sqrt(3 * n + 1)) / math.factorial(n)
        current_sum += u
        print(u)
        n += 1

    if abs(u) < E:
        print("Сума сходиться до заданої точності.")
    elif abs(u) > G:
        print("Ряд розходиться.")


if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Визначити мінімальне число")
        print("2. Попадання в фігуру")
        print("3. Дослідження ряду на збіжність або розбіжність ")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            if12()
        elif choice == "2":
            task2()
        elif choice == "3":
            task27()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")
