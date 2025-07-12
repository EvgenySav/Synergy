import random


def find_sum_negative_between_max_min(arr):
    """
    Находит сумму отрицательных элементов массива, расположенных между
    максимальным и минимальным элементами.

    Args:
        arr (list): Одномерный массив чисел

    Returns:
        tuple: (сумма отрицательных элементов, индекс максимума, индекс минимума)
    """
    if not arr:
        return 0, -1, -1

    if len(arr) == 1:
        return 0, 0, 0

    # Находим индексы максимального и минимального элементов
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    # Определяем границы интервала (не включая сами максимум и минимум)
    start_index = min(max_index, min_index)
    end_index = max(max_index, min_index)

    # Если максимум и минимум соседние или совпадают, то между ними нет элементов
    if end_index - start_index <= 1:
        return 0, max_index, min_index

    # Вычисляем сумму отрицательных элементов между максимумом и минимумом
    negative_sum = 0
    for i in range(start_index + 1, end_index):
        if arr[i] < 0:
            negative_sum += arr[i]

    return negative_sum, max_index, min_index


def print_array_analysis(arr):
    """
    Выводит подробный анализ массива и решение задачи

    Args:
        arr (list): Массив для анализа
    """
    print(f"Массив: {arr}")
    print(f"Размер массива: {len(arr)}")

    if not arr:
        print("Массив пуст!")
        return

    # Находим результат
    negative_sum, max_index, min_index = find_sum_negative_between_max_min(arr)

    # Выводим информацию об элементах
    print(f"Максимальный элемент: {arr[max_index]} (индекс: {max_index})")
    print(f"Минимальный элемент: {arr[min_index]} (индекс: {min_index})")

    # Определяем границы
    start_index = min(max_index, min_index)
    end_index = max(max_index, min_index)

    print(f"Интервал между максимумом и минимумом: индексы {start_index + 1} - {end_index - 1}")

    # Показываем элементы между максимумом и минимумом
    if end_index - start_index > 1:
        elements_between = arr[start_index + 1:end_index]
        print(f"Элементы между максимумом и минимумом: {elements_between}")

        # Показываем отрицательные элементы
        negative_elements = [x for x in elements_between if x < 0]
        if negative_elements:
            print(f"Отрицательные элементы: {negative_elements}")
            print(f"Сумма отрицательных элементов: {negative_sum}")
        else:
            print("Отрицательных элементов между максимумом и минимумом нет")
    else:
        print("Между максимумом и минимумом нет элементов")

    print(f"ОТВЕТ: {negative_sum}")
    print("-" * 50)


def generate_test_array(size, min_val=-10, max_val=10):
    """
    Генерирует тестовый массив случайных чисел

    Args:
        size (int): Размер массива
        min_val (int): Минимальное значение
        max_val (int): Максимальное значение

    Returns:
        list: Сгенерированный массив
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def run_tests():
    """
    Запускает набор тестов для проверки корректности работы программы
    """
    print("=== ТЕСТИРОВАНИЕ ПРОГРАММЫ ===\n")

    # Тест 1: Обычный случай
    print("Тест 1: Обычный случай")
    test_array1 = [3, -2, 8, -5, 1, -3, 9, -1, 2]
    print_array_analysis(test_array1)

    # Тест 2: Нет отрицательных элементов между максимумом и минимумом
    print("Тест 2: Нет отрицательных элементов")
    test_array2 = [1, 5, 2, 8, 3, 4]
    print_array_analysis(test_array2)

    # Тест 3: Максимум и минимум рядом
    print("Тест 3: Максимум и минимум рядом")
    test_array3 = [5, 9, 1, 3, 7]
    print_array_analysis(test_array3)

    # Тест 4: Массив из одного элемента
    print("Тест 4: Массив из одного элемента")
    test_array4 = [5]
    print_array_analysis(test_array4)

    # Тест 5: Массив из двух элементов
    print("Тест 5: Массив из двух элементов")
    test_array5 = [3, -2]
    print_array_analysis(test_array5)

    # Тест 6: Все элементы отрицательные
    print("Тест 6: Все элементы отрицательные")
    test_array6 = [-5, -2, -8, -1, -3]
    print_array_analysis(test_array6)


def main():
    """
    Главная функция программы
    """
    print("=== КЕЙС-ЗАДАЧА №3 ===")
    print("Поиск суммы отрицательных элементов между максимальным и минимальным")
    print()

    while True:
        print("Выберите режим работы:")
        print("1. Ввести массив вручную")
        print("2. Сгенерировать случайный массив")
        print("3. Запустить тесты")
        print("4. Выход")

        choice = input("\nВаш выбор (1-4): ").strip()

        if choice == "1":
            try:
                print("\nВведите элементы массива через пробел:")
                user_input = input().strip()
                if not user_input:
                    print("Массив не может быть пустым!")
                    continue

                arr = list(map(int, user_input.split()))
                print()
                print_array_analysis(arr)

            except ValueError:
                print("Ошибка: введите только целые числа через пробел!")

        elif choice == "2":
            try:
                size = int(input("Введите размер массива: "))
                if size <= 0:
                    print("Размер массива должен быть положительным!")
                    continue

                min_val = int(input("Минимальное значение элементов: "))
                max_val = int(input("Максимальное значение элементов: "))

                if min_val > max_val:
                    print("Минимальное значение не может быть больше максимального!")
                    continue

                arr = generate_test_array(size, min_val, max_val)
                print()
                print_array_analysis(arr)

            except ValueError:
                print("Ошибка: введите корректные числа!")

        elif choice == "3":
            run_tests()

        elif choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор! Попробуйте еще раз.")

        print()


if __name__ == "__main__":
    main()