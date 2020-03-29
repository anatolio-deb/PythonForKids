# Dungeons: dungeons.py

# From the course: "Python programming for kids"
# written by Anatoly Nikiforov and his students, Kodium, 2020
# https://kodium.online/

import random
import time

dungeons = ['Пустое подземелье','Подземелье с сокровищами', 'Подземелье с монстрами']
treasures = ['Зелье здоровья','Зелье маны','Серебряный клинок','Лук','Эксакалибур','Пламенные латы','Драконьи доспехи']
monsters = ['Лич','Ревенант','Минотавр','Орк','Гоблин']

def choose_the_room(): # Это функция для повтороного использования кода
  dungeon = random.choice(dungeons)
  if dungeon == 'Подземелье с сокровищами':
    print("Ты зашел в", dungeon, "и подобрал", random.choice(treasures))
  elif dungeon == 'Подземелье с монстрами':
    print("Ты зашел в", dungeon, "На тебя напал",random.choice(monsters))
  else:
    print("В подземелье пусто, а по полу бегают крысы...")
    time.sleep(3)
    choose_the_room() # Если пустое подземелье, выбирать подземелье

choose_the_room() # Это первый вызов функции
