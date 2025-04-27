def read_and_trasform_numbers():
    """
    Читает введённые цифры и преобразует их в список

    Для дальнейшей обработки
    """
    s = input()
    s = s.split()
    return [int(x) for x in s]

def filter_evens(numbers):
    """ Возвращает список с только чётными числами """
    evens = []
    for x in numbers:
        if x % 2 == 0:
            evens.append(x)
    return evens

def find_max_and_min(numbers):
    """ Находит в списке наибольшее и наименьшее число """
    max_number = max(numbers)
    min_number = min(numbers)
    return max_number, min_number

def sorted_numbers(numbers):
    """ Сортирует список от наименьше к наибольшему без использования функции sorted() """
    spisok = []
    copy_list = numbers.copy()
    for x in range(len(numbers)):
        n = min(copy_list)
        spisok.append(n)
        copy_list.remove(n)
    return spisok

def main():
    """ Реализует поставленные задачи и выводит их в консоль """
    numbers = read_and_trasform_numbers()
    even_numbers = filter_evens(numbers)
    maximum, minimum = find_max_and_min(numbers)
    sort_without_sorted = sorted_numbers(numbers)

    print(f"Четные числа: {even_numbers}")
    print(f"Максимальное число: {maximum}")
    print(f"Минимальное число: {minimum}")
    print(f"Отсортированный список: {sort_without_sorted}")


if __name__ == "__main__":
    main()