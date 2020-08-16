from cs50 import get_int


def main():

    number = make_string()
    luhn = luhn1(number) + luhn2(number)
    luhn = str(luhn)

    if luhn.endswith("0"):
        if number.startswith(('34', '37')) and len(number) == 15:
            print("AMEX")
        elif number.startswith(('51', '52', '53', '54', '55')) and len(number) == 16:
            print("MASTERCARD")
        elif number.startswith('4') and (len(number) == 13 or len(number) == 16):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


def make_string():
    string_number = str(get_number())
    return string_number


def get_number():
    while True:
        number = get_int("What's the number of credit card?\n")
        if number > 0:
            break
    return number


def luhn1(string_number):
    all_even_chars = string_number[-2::-2]
    luhn1 = 0
    for n in all_even_chars:
        multiplied_number = int(n) * 2
        first_digit = multiplied_number % 10
        second_digit = multiplied_number // 10
        luhn1 += first_digit + second_digit
    return luhn1


def luhn2(string_number):
    all_odd_chars = string_number[-1::-2]
    luhn2 = 0
    for n in all_odd_chars:
        number = int(n)
        luhn2 += number
    return luhn2


main()


# ILGASIS BUDAS, PERRASYTAS IS C KALBOS
# def main():
#     number = get_number()
#     k = number
#     first_sum = 0
#     second_sum = 0
#     while k > 0:
#         l = k // 10
#         m = l % 10
#         k = k // 100
#         m = m * 2
#         m1 = m % 10
#         m2 = m // 10
#         first_sum = first_sum + m1 + m2

#     k = number
#     while k > 0:
#         y = k % 10
#         k = k // 100
#         second_sum = second_sum + y

#     final_sum = first_sum + second_sum

#     k = number
#     if final_sum % 10 == 0:
#         if 349999999999999 >= k and k >= 340000000000000:
#             print("AMEX")
#         elif 379999999999999 >= k and k >= 370000000000000:
#             print("AMEX")
#         elif 5599999999999999 >= k and k >= 5100000000000000:
#             print("MASTERCARD")
#         elif 4999999999999 >= k and k >= 4000000000000:
#             print("VISA")
#         elif 4999999999999999 >= k and k >= 4000000000000000:
#             print("VISA")
#         else:
#             print("INVALID")
#     else:
#         print("INVALID")


# def get_number():
#     while True:
#         number = get_int("What's the number of credit card?\n")
#         if number > 0:
#             break
#     return number


# main()