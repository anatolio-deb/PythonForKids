import random
import time

dungeons = ['Пустая комната','Комната с сокровищами', 'Комната с монстрами']
treasures = ['Зелье здоровья','Зелье маны','Серебряный клинок','Лук','Эксакалибур','Пламенные латы','Драконьи доспехи']
monsters = ['Лич','Ревенант','Минотавр','Орк','Гоблин']

def choose_the_room(): # Это функция для повтороного использования кода
  dungeon = random.choice(dungeons)
  if dungeon == 'Комната с сокровищами':
    print("Ты зашел в", dungeon, "и подобрал", random.choice(treasures))
  elif dungeon == 'Комната с монстром':
    print("Ты зашел в", dungeon, "На тебя напал",random.choice(monsters))
  else:
    print("Комната пуста, а по полу бегают крысы...")
    time.sleep(3)
    choose_the_room()

choose_the_room() # Это вызов фугкции
