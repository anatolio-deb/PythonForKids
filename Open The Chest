import random

items = ['500 Золотых', 'Зелье Здоровья', 'Помидор', 'Зелье Манны', 'Волшебный Свиток']
master_keys = 3
password = []
password_match = []

for i in range(2):
  password.append(str(random.randint(0,5)))
#print(password) # показать пароль (чит)

while master_keys != 0:
  for k in input('Сундук закрыт, попробуй взломать:\n'):
    password_match.append(k)
 
  if password == password_match:
    item = random.choice(items)
    print("Ты подобрал", item, ", поздравляем!")
    break
  else:
    master_keys = master_keys-1
    print('Облом! Осталось', master_keys, 'отмычек.')
    if master_keys == 0:
      print('Приходи с новыми отмычками!')
