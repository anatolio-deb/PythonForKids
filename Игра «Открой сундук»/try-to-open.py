import random

items = ['500 Золотых', 'Зелье Здоровья', 'Помидор', 'Зелье Манны', 'Волшебный Свиток']
master_keys = 3 # Количество отмычек
password = []
password_match = []

for i in range(2):
    password.append(str(random.randint(1,5))) # Запираем сундук случайным поролем
print(password) # показать пароль (чит)
'''
# Если не понятно, сгенерируем пароль по-другому:
a = str(random.randint(0,5))
b = str(random.randint(0,5))
password = a + b
# В итоге получим строку из двух значений.
'''
while master_keys > 0 and password != password_match:
    password_match = []
    for k in input('Сундук закрыт, попробуй взломать:\n'):
        password_match.append(k)
    '''
    # Если не понятно, примем ввод по-другому:
    a = str(input("Введите первую цифру пароля: ))
    b = str(input("Введите вторую цифру пароля: ))
    password_match = a + b
    # В итоге получим строку из двух значений.
    '''
    master_keys -= 1
    print('Ой! Осталось', master_keys, 'отмычек.')
else:
    if password == password_match:
        item = random.choice(items) # Ложим случайный предмет в сундук
        print("Ты подобрал", item, ", поздравляем!")
    else:
        print('Приходи с новыми отмычками!')
