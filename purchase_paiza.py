# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

purchase_count = int(input())
purchase  = ()
food = 0
book = 0
cloth = 0
other = 0
for num in range(purchase_count):
    tmp_purchase = input()
    purchase = tmp_purchase.split()
    if purchase[0] == "0":
        food += int(purchase[1])
    elif purchase[0] == "1":
        book += int(purchase[1])
    elif purchase[0] == "2":
        cloth += int(purchase[1])
    elif purchase[0] == "3":
        other += int(purchase[1])

answer = int(food /100) * 5 + int(book / 100) * 3 + int(cloth / 100) * 2 +int(other / 100) * 1
print(answer)
