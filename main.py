#a, b = map(int, input().split())
#if a < b:
#    print('b is better')
#elif a > b:
#    print('a is better')
#else:
#    print('equal')


#def find_occurrences(first_lst: list, second_lst: list)
#    result= []
#   for el in second_lst:
#        if el in first_lst:
#            result.append(el)

#    return result


#def list_filter_string(given_list: list)


#A.
#A, B = input().split(" ")
#A_digit, A_float = A.split(".")
#B_digit, B_float = B.split(".")
#if A_digit != B_digit:
#    print("Draw")
#else:
#    if len(A_float) > len(B_float):
#        print("Petay won")
#    elif len(A_float) < len(B_float):
#        print("Vasya won")
#    elif len(A_float) == len(B_float):
#        print("Draw")


#B.
#n, m = map(int, input().split())
#counter = 0
#for _ in range(n):
#    counter += input().count('5')
#print("Yes", counter, sep = "/n") if counter else print("No")


#C.
#n = int(input())
#if n == 0:
#    print("Broken")
#else:
#   start = 12
#   while start % n:
#       start += 1

#   print(*range(start, 457, n))


#for number in range(12, 457):
    #    if number % n == o:
    #       print(number, end=' ')


#D.
#number = input()


#F.
#esse = input()[::-1]
#words = esse.split(" ")
#words_reverse = words[::-1]
#print(*words_reverse)


def main():
    main_menu()
    pass


def main_menu():
    choice = input("Игра угадай-ка\n"
                   "1. Запуск игры\n"
                   "2. Выход из игры\n"
                   "Выбор: ")

    if choice == '1':
        game_menu()
    elif choice == '2':
        exit(0)
    else:
        print("Некорректный ввод. Попробуйте еще раз\n")
        main_menu()


def game_menu():
    choice = input("Диапазон чисел:\n"
                   "1. От 1 до 100\n"
                   "2. Задать свой\n"
                   "Выбор: ")

    if choice == '1':
        core(1, 100)
    elif choice == '2':
        core(*take_numbers())
    else:
        print("Некорректный ввод. Попробуйте еще раз\n")
        game_menu()


def take_numbers():
    first = input()
    second = input()

    if first.isdigit() and second.isdigit():
        if first < second:
            return first, second

    print("Числа не подходят условия (быть целыми положительными, первое меньше второго")


def bin_search(left: int, right: int):
    attempts = 0

    while left + 1 < right:
        mid = (left + right) // 2
        choice = input(f"{mid}: ")

        if choice == "меньше":
            left = mid + 1
        elif choice == "больше":
            right = mid
        elif choice == "угадано":
            return mid, attempts + 1
        else:
            continue

        attempts += 1

    return left, attempts


def core():
    number, attempts = bin_search()
    print(f"Я отгадал ваше число: \{number}\ за {attempts} попыток")
    main_menu()
