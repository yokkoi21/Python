# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
print("please input:")
input_lines = input()
input_split = input_lines.split()
input_number = {}
for num in range(3):
    input_number[num] = float(input_split[num])

leftovers = input_number[0] * ((100 - input_number[1]) / 100)
print(leftovers)
answer = 0
if(leftovers != 0 and input_number[2] != 0):
    answer = leftovers * ((100 - input_number[2]) / 100)
print(answer)
