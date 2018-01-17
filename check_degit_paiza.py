# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_times = int(input())
input_number = [[0 for i in range(16)] for j in range(input_times)]
for num1 in range(input_times):
    for num2 in range(16):
        input_number[num1][num2] = input()


def calc_even(input_number,i):

    for num4 in range(0,15,2):
        if input_number[i][num4] >= 5:
            add_even += 1 + ((input_number[i][num4] * 2) % 10)
        elif input_number[i][num4] < 5:
            add_even += input_number[i][num4] * 2

    return add_even


def calc_odd(input_number,i):
    for num4 in range(1,16,2):
        add_odd += input_number[i][num4]

    return add_odd

for i in range(input_times):
    answer = 10 - ((calc_even(input_number,i) + calc_odd(input_number,i)) * 10)
    print(answer)
