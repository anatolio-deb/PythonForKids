import random

MEAT = 20
GRASS = 20
Day = ['day', 'night']

Herbivores = {
              'rabbit'  : 1,
              'sheep'   : 5,
              'koala'   : 1,
              'goat'    : 10,
              'elephant': 20,
              'horse'   : 15
              }

Predators = {
              'tiger'      : 4,
              'crocodile'  : 6 ,
              'eagle'      : 1,
              'hippopotam' : 20,
              'lion'       : 11
             }
             

def feed_the_herbivores():
  global GRASS
  global Hebivores
  
  print('The  herbivorse are:')
  for key, value in Herbivores.items():
    print(key)
  
  herbivore = input('Which animal do you want to feed?\n')
  print(herbivore,'ate', Herbivores[herbivore],'kg of grass')
  GRASS = GRASS - Herbivores[herbivore]
#  print('Grass left:', GRASS)

def feed_the_predators():
  global MEAT
  global Predators
  
  print('The predators are:')
  for key, value in Predators.items():
    print(key)
  
  predator = input('Which animal do you want to feed?\n')
  
  print(predator,'ate', Predators[predator],'kg of meat')
  
  MEAT = MEAT - Predators[predator]
  
#  print('Meat left:', MEAT)

# Главный цикл, который выключает нашу игру
while GRASS or MEAT > 0:
  Now = random.choice(Day)
  print('\t\t\t\tGrass left:', GRASS, '\n\t\t\t\t', 'Meat left:', MEAT)

# Циклы, которые не выключают игру, а только функции
  if GRASS > 0 and Now == 'day':
    print("It's", 'a', Now + '.', 'Time to feed the herbivores in your zoo!')
    feed_the_herbivores() # вызов функции
  else:
    if GRASS <= 0:
      print('No grass left, herbivores hugry!')

  if MEAT > 0 and Now == 'night':
    print("It's", 'a', Now + '.', 'Predators are awake and hungry!')
    feed_the_predators()
  else:
    if MEAT <= 0:
      print('No meat left, predators are hugry!')
else:
  print('No grass and meat left, animals are hungry!')
