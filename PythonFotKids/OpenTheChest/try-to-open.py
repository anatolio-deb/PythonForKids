import random
# Список предметов
items = ['500 Золотых', 'Зелье Здоровья', 'Помидор', 'Зелье Манны', 'Волшебный Свиток']
password = []
# Закрываем сундук
for i in range(2):
    password.append(str(random.randint(1,5)))
# Количество отмычек
master_keys = 3
# Показать пароль (чит)
# print(password)
while master_keys > 0:
    password_match = []
    for k in input('Сундук закрыт, попробуй взломать:\n'):
        password_match.append(k)

    if password == password_match:
        # Ложим в сундук случайный предмет
        item = random.choice(items)
        print("Ты подобрал", item, ", поздравляем!")
        break
    else:
        master_keys -= 1
        print('Ой! Осталось', master_keys, 'отмычек.')
else:
    print('Кончились отмычки!')
