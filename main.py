from sorts import *
import time


def generate_random_array(length, start, end):
    array = [random.randint(start, end) for _ in range(length)]
    return array


if __name__ == "__main__":
    flag = 0
    while flag == 0:
        start_time = 0
        end_time = 0
        arr = []
        # Ввод массива
        choose = int(input("1. Рандомный массив\n2. Вручную написанный массив"))
        if choose == 1:
            length = int(input("Введите длину массива: "))
            start = int(input("Введите начальное значение: "))
            end = int(input("Введите конечное значение: "))

            arr = generate_random_array(length, start, end)
            print("Сгенерированный массив:", arr)
        if choose == 2:
            arr = input("Введите элементы массива через пробел: ").split()
            arr = [int(num) for num in arr]

        # Выбор метода сортировки
        print("Выберите метод сортировки:")
        print("1. Пузырьковая сортировка")
        print("2. Сортировка выбором")
        print("3. Сортировка вставками")
        print("4. Пирамидальная сортировка")
        print("5. Сортировка слиянием")
        print("6. Быстрая сортировка")
        print("7. Сортировка Шелла")
        print("8. Выход")
        choice = int(input("Введите номер метода: "))

        if choice == 1:
            start_time = time.time()
            bubble_sort(arr)
            end_time = time.time()
        elif choice == 2:
            start_time = time.time()
            selection_sort(arr)
            end_time = time.time()
        elif choice == 3:
            start_time = time.time()
            insertion_sort(arr)
            end_time = time.time()
        elif choice == 4:
            start_time = time.time()
            heap_sort(arr)
            end_time = time.time()
        elif choice == 5:
            start_time = time.time()
            merge_sort(arr)
            end_time = time.time()
        elif choice == 6:
            start_time = time.time()
            quick_sort(arr)
            end_time = time.time()
            start_time = time.time()
            insertion_sort(arr)
            end_time = time.time()
        elif choice == 7:
            start_time = time.time()
            shell_sort(arr)
            end_time = time.time()
        elif choice == 8:
            flag = 1
            continue
        else:
            print("Неверный выбор метода.")

        # Вывод отсортированного массива
        print("Отсортированный массив:")
        print("Время выполнения: %.10f секунд" % (end_time - start_time))
        print(arr)

        a = int(input("\nВы хотите выйти?\n1. Да \n2. Нет"))
        if a == 1:
            flag = 1
