from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
		guess_1= int(input('Введите число: '))

		if guess_1 < number:
			print('Число меньше загаданного!')
		
		elif guess_1 > number:
			print('Ваше число больше загаданного!')

		elif guess_1 == number:
			break

print('У вас отличная интуиция!')
     