# Throw the dice: throw-the-dice.py

# From the course: "Python programming for kids"
# written by Anatoly Nikiforov and his students, Kodium, 2020
# https://kodium.online/

import random
import time
# Два пустых списка для хранения очков игроков
player1, player2 = [],[]
# Счетчик бросков первого игрока - без него игроки "бросают" поочереди
count = 0
# Три броска на каждого игрока
for i in range(3):
	# Пока первый игрок не бросит три раза, не переходить ко второму игроку
	while count < 3:
		print('Первый игрок бросает...')
		shot1 = int(random.randint(1,6))
		player1.append(shot1)
		# Пауза для реалистичности броска кубика
		time.sleep(3)
		print('Выпало:', shot1)
		count += 1
	print('Второй игрок бросает...')
	shot2 = int(random.randint(1,6))
	player2.append(shot2)
	time.sleep(3)
	print('Выпало:', shot2)
# Подсчет суммы очков в списках
player1 = player1[0] + player1[1] + player1[2]
player2 = player2[0] + player2[1] + player2[2]

print('Первый игрок набрал:', player1, 'очков')
print('Второй игрок набрал:', player2, 'очков')

if player1 > player2:
	print('Победил первый игрок.')
elif player1 < player2:
	print('Победил второй игрок.')
else:
	print('Ничья!')
