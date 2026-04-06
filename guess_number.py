import random

while True:
   n = int(input("最小値を入力してください:"))
   m = int(input("最大値を入力してください:"))

   if n <= m:
      break
   else:
      print("最小値は最大値以下でお願いします")

random_number = random.randint(n, m)

while True:
    guess = int(input("数字を予想してみてください:"))

    if random_number == guess:
        print("当たりです!")
        break
    elif guess < random_number:
        print("もっと大きな数を入力してください")
    else:
        print("もっと小さな数を入力してください")
    