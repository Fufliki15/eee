import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Попробуй угадать число от 1 до 100.")

secret = random.randint(1, 100)  
attempt = 0 

while True:
    user_input = input("Введите ваше число: ") 
    attempt += 1

    try:
        user_guess = int(user_input)
    except ValueError:
        print("ошибка пожалуйста вводите только цифры   ")
        continue 


    if user_guess == secret:
        print(f"Поздравляем, вы угадали число! Всего вводов: {attempt}")
        break
    elif user_guess > secret:
        print("Ваше число больше загаданного.")
    elif user_guess < secret:
        print("Ваше число меньше загаданного.")
