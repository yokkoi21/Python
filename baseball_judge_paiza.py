# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

count = int(input())
strike_count = 0
ball_count = 0
for num in range(count):
    result = input()
    if(result == "ball" and ball_count < 3):
        print("ball!")
        ball_count+=1
    elif(result == "ball" and ball_count == 3):
        print("fourball!")
        ball_count = 0
    elif(result == "strike" and strike_count < 2):
        print("strike!")
        strike_count+=1
    elif(result == "strike" and strike_count == 2):
        print("out!")
        strike_count = 0
