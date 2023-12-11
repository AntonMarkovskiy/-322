import numpy as np
def TriangleP(a, h):
    # Знайдемо довжину одного зі сторін трикутника (b) за теоремою Піфагора
    b = (a / 2) ** 2 + h ** 2
    b = b ** 0.5
    # Обчислюємо периметр трикутника
    perimeter = a + 2 * b
    return perimeter

# Функція для введення даних, виклику функції та виведення результатів
def proc20():
    for i in range(3):
        a = float(input(f"Введіть основу трикутника {i + 1}: "))
        h = float(input(f"Введіть висоту трикутника {i + 1}: "))
        perimeter = TriangleP(a, h)
        print(f"Периметр трикутника {i + 1}: {perimeter}")

# Зовнішня функція для знаходження максимального серед мінімальних елементів рядків
def outer_function(filename):
    # Зчитування матриці з файлу
    matrix = np.loadtxt(filename)

    # Знаходження мінімальних елементів в кожному рядку
    min_in_rows = np.min(matrix, axis=1)

    # Знаходження максимального серед мінімальних елементів
    max_among_min = np.max(min_in_rows)

    return max_among_min

# Внутрішня функція для сортування матриці по стовпцях по зростанню
def inner_function(input_filename, output_filename):
    # Зчитування матриці з файлу
    matrix = np.loadtxt(input_filename)

    # Сортування матриці по стовпцях по зростанню
    sorted_matrix = np.sort(matrix, axis=0)

    # Збереження відсортованої матриці в новому файлі
    np.savetxt(output_filename, sorted_matrix, fmt='%d', delimiter=' ')

    return sorted_matrix

def matrix11():
    # Виклик зовнішньої функції для знаходження максимального серед мінімальних елементів
    max_among_min = outer_function('matrix.txt')
    print("Максимальний серед мінімальних елементів рядків:", max_among_min)

    # Виклик внутрішньої функції для сортування матриці
    sorted_matrix = inner_function('matrix.txt', 'sorted_matrix.txt')
    print("Відсортована матриця:")
    print(sorted_matrix)

if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Proc 20")
        print("2. Matrix 11")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            proc20()
        elif choice == "2":
            matrix11()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")
