import math


def calculate_max_dragon_power(n):
    """
    Вычисляет максимальную силу драконьей стаи при заданном количестве голов.

    Алгоритм основан на том, что для максимизации произведения при фиксированной сумме
    нужно разбить число на части, близкие к числу e ≈ 2.718. Поскольку у нас целые числа
    и ограничение максимум 7 голов на дракона, оптимальными являются числа 2 и 3.

    Args:
        n (int): Общее количество голов в стае

    Returns:
        int: Максимальная сила стаи
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    # Базовые случаи
    if n <= 4:
        return n

    # Если n делится на 3, используем только тройки
    if n % 3 == 0:
        return 3 ** (n // 3)

    # Если остаток 1 при делении на 3, заменяем одну тройку на две двойки
    # (3 + 1 = 4 = 2 + 2, а 2*2 = 4 > 3*1 = 3)
    elif n % 3 == 1:
        return 3 ** (n // 3 - 1) * 4

    # Если остаток 2 при делении на 3, добавляем одну двойку
    else:  # n % 3 == 2
        return 3 ** (n // 3) * 2


def find_optimal_distribution(n):
    """
    Находит оптимальное распределение голов по драконам для максимальной силы.

    Args:
        n (int): Общее количество голов

    Returns:
        list: Список количества голов у каждого дракона
    """
    if n <= 0:
        return []

    if n == 1:
        return [1]

    if n <= 4:
        return [n]

    dragons = []

    if n % 3 == 0:
        # Используем только тройки
        dragons = [3] * (n // 3)
    elif n % 3 == 1:
        # Используем тройки и заменяем последнюю тройку на две двойки
        dragons = [3] * (n // 3 - 1) + [2, 2]
    else:  # n % 3 == 2
        # Используем тройки и добавляем одну двойку
        dragons = [3] * (n // 3) + [2]

    return sorted(dragons, reverse=True)


def verify_solution(dragons, n):
    """
    Проверяет правильность решения.

    Args:
        dragons (list): Список количества голов у каждого дракона
        n (int): Ожидаемое общее количество голов

    Returns:
        tuple: (корректность_суммы, произведение)
    """
    total_heads = sum(dragons)
    power = 1
    for heads in dragons:
        power *= heads

    return total_heads == n, power


def solve_dragon_power_problem(n):
    """
    Решает задачу о максимальной силе драконьей стаи.

    Args:
        n (int): Общее количество голов

    Returns:
        tuple: (максимальная_сила, распределение_голов)
    """
    max_power = calculate_max_dragon_power(n)
    distribution = find_optimal_distribution(n)

    return max_power, distribution


def print_detailed_solution(n):
    """
    Выводит подробное решение задачи.

    Args:
        n (int): Количество голов в стае
    """
    print(f"Задача: Найти максимальную силу стаи из {n} голов")
    print(f"Ограничения: максимум 7 голов у одного дракона")
    print()

    if n <= 0:
        print("Некорректное количество голов!")
        return

    max_power, distribution = solve_dragon_power_problem(n)

    print(f"Оптимальное распределение голов: {distribution}")
    print(f"Количество драконов в стае: {len(distribution)}")
    print(f"Проверка суммы голов: {' + '.join(map(str, distribution))} = {sum(distribution)}")
    print(f"Вычисление силы: {' × '.join(map(str, distribution))} = {max_power}")

    # Проверка
    is_correct, calculated_power = verify_solution(distribution, n)
    print(f"Проверка: сумма голов {'корректна' if is_correct else 'некорректна'}")
    print(f"Вычисленная сила: {calculated_power}")

    print(f"\nОТВЕТ: {max_power}")
    print("-" * 50)


def run_comprehensive_tests():
    """
    Запускает комплексные тесты для проверки корректности алгоритма.
    """
    print("=== КОМПЛЕКСНОЕ ТЕСТИРОВАНИЕ ===\n")

    # Тесты для малых значений
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 25, 30, 50, 99]

    for n in test_cases:
        print(f"Тест для N = {n}:")
        print_detailed_solution(n)

    # Проверка математического обоснования
    print("\n=== ПРОВЕРКА МАТЕМАТИЧЕСКОГО ОБОСНОВАНИЯ ===")
    print("Для больших N оптимальное разложение должно содержать в основном тройки:")

    for n in [21, 24, 27, 30]:
        max_power, distribution = solve_dragon_power_problem(n)
        count_2 = distribution.count(2)
        count_3 = distribution.count(3)
        print(f"N={n}: двойки={count_2}, тройки={count_3}, сила={max_power}")


def brute_force_verification(n, max_heads=7):
    """
    Проверяет решение методом перебора для малых N (для верификации алгоритма).

    Args:
        n (int): Количество голов
        max_heads (int): Максимальное количество голов у одного дракона

    Returns:
        tuple: (максимальная_сила, оптимальное_распределение)
    """
    if n <= 0:
        return 0, []

    if n == 1:
        return 1, [1]

    max_power = 0
    best_distribution = []

    def generate_partitions(remaining, current_partition, min_val=2):
        nonlocal max_power, best_distribution

        if remaining == 0:
            if current_partition:
                power = 1
                for val in current_partition:
                    power *= val
                if power > max_power:
                    max_power = power
                    best_distribution = current_partition.copy()
            return

        if remaining == 1:
            current_partition.append(1)
            power = 1
            for val in current_partition:
                power *= val
            if power > max_power:
                max_power = power
                best_distribution = current_partition.copy()
            current_partition.pop()
            return

        for val in range(min_val, min(remaining + 1, max_heads + 1)):
            current_partition.append(val)
            generate_partitions(remaining - val, current_partition, val)
            current_partition.pop()

    generate_partitions(n, [])
    return max_power, sorted(best_distribution, reverse=True)


def verify_algorithm_correctness():
    """
    Проверяет корректность быстрого алгоритма сравнением с методом перебора.
    """
    print("\n=== ВЕРИФИКАЦИЯ АЛГОРИТМА ===")

    for n in range(1, 21):  # Проверяем для небольших N
        fast_power, fast_dist = solve_dragon_power_problem(n)
        brute_power, brute_dist = brute_force_verification(n)

        is_correct = fast_power == brute_power
        status = "✓" if is_correct else "✗"

        print(f"N={n:2d}: Быстрый={fast_power:3d}, Перебор={brute_power:3d} {status}")

        if not is_correct:
            print(f"  Быстрый алгоритм: {fast_dist}")
            print(f"  Метод перебора:   {brute_dist}")


def main():
    """
    Главная функция программы.
    """
    print("=== КЕЙС-ЗАДАЧА №4: МАКСИМАЛЬНАЯ СИЛА ДРАКОНЬЕЙ СТАИ ===")
    print("Найти максимальную силу стаи драконов при известном общем количестве голов")
    print("Ограничение: максимум 7 голов у одного дракона")
    print()

    while True:
        print("Выберите режим:")
        print("1. Решить задачу для конкретного N")
        print("2. Запустить комплексные тесты")
        print("3. Верифицировать алгоритм")
        print("4. Выход")

        choice = input("\nВаш выбор (1-4): ").strip()

        if choice == "1":
            try:
                n = int(input("Введите количество голов в стае (1-99): "))
                if n <= 0 or n >= 100:
                    print("Количество голов должно быть от 1 до 99!")
                    continue

                print()
                print_detailed_solution(n)

            except ValueError:
                print("Ошибка: введите целое число!")

        elif choice == "2":
            run_comprehensive_tests()

        elif choice == "3":
            verify_algorithm_correctness()

        elif choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор!")

        print()


if __name__ == "__main__":
    main()