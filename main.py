import random


class Tamagochi_Puppy():
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.weight = 3
        self.age = 0.1
        self.happiness = 50
        self.sadness = 50
        self.full = 50
        self.thirst = 50

    def menu(self):
        print(f"--------------------\n"
              f"Выберите действие:\n"
              f"1. покормить собаку\n"
              f"2. напоить водичкой\n"
              f"3. пойти погулять с собакой\n"
              f"4. почесать за ушком\n"
              f"5. поиграть")

    def info(self):
        print(f"Возраст: {self.age} лет\n"
              f"Здоровье: {self.health} %\n"
              f"Вес: {self.weight} кг\n"
              f"Уровень счастья: {self.happiness} %\n"
              f"Уровень печали: {self.sadness} %\n"
              f"Сытость: {self.full} %\n"
              f"Жажда: {self.thirst} %")

    def feed(self):
        dog_food = {"1": "сухой корм",
                    "2": "паштет",
                    "3": "косточка",
                    "4": "лакомство"}
        choise_of_food = input(f"~~~Выберите, чем хотите покормить {self.name} {dog_food}~~~: ")
        try:
            print(f"~~~{self.name} скушал {dog_food[choise_of_food]}!~~~")
        except KeyError:
            print("~~~нет такого выбора еды~~~")
        else:
            self.weight += 0.1
            self.age += 0.1
            self.full += 10
            self.thirst += 5
        Tamagochi_Puppy.info(self)

    def water(self):
        self.age += 0.1
        self.thirst -= 15
        print(f"~~~Вы напоили {self.name} водичкой!~~~")
        Tamagochi_Puppy.info(self)

    def walk(self):
        self.health += 5
        self.weight -= 0.3
        self.age += 0.1
        self.happiness += 20
        self.sadness -= 10
        self.full -= 3
        self.thirst -= 1
        print(f"~~~Вы погуляли с {self.name}!~~~")
        Tamagochi_Puppy.info(self)

    def incident(self):
        list_of_keys = ['a', 'b', 'c', 'd']
        list_of_incidents = ["собака погналась за голубем и потерялась", "собака попала под машину",
                             "собака подралась с другой собакой", "собака наелась из мусорки и отравилась"]
        all = dict(zip(list_of_keys, list_of_incidents))
        bad_luck = random.randint(1, 100)
        if 1 <= bad_luck <= 5:
            print(all[random.choice(list_of_keys)])
            return True
        else:
            return False

    def scratch(self):
        self.age += 0.1
        self.happiness += 10
        self.sadness -= 10
        print(f"~~~Вы почесали {self.name} за ушком!~~~")
        Tamagochi_Puppy.info(self)

    def play(self):
        self.weight -= 0.1
        self.age += 0.1
        self.happiness += 10
        self.sadness -= 10
        self.full -= 5
        self.thirst += 3
        print(f"~~~Вы поиграли с {self.name}! Он счастлив!~~~")
        Tamagochi_Puppy.info(self)


Max = Tamagochi_Puppy(input("Введите имя вашего питомца: "))

while True:
    Max.menu()
    if Max.health <= 5:
        print("---питомец умер от болезней---")
        break
    elif Max.health >= 100:
        print("---у питомца прекрасное здоровье---")
    elif Max.weight >= 15:
        print("---у питомца большой вес, старайтесь больше гулять---")
    elif Max.weight <= 0.6:
        print("---питомец умер от истощения---")
        break
    elif Max.age >= 20:
        print("---питомец умер от старости---")
        break
    elif Max.happiness >= 100 or Max.sadness <= 1:
        print("---питомец счастлив---")
    elif Max.happiness <= 1 or Max.sadness >= 100:
        print("---питомец умер от печали---")
        break
    elif Max.full <= 0:
        print("---питомец умер от голода---")
        break
    elif Max.full >= 100:
        print("---вы перекормили питомца---")
        break
    elif Max.thirst >= 100:
        print("---питомец умер от жажды---")
        break
    elif Max.thirst <= 0:
        print("---слишком много воды, хватить поить питомца---")
    a = int(input("~~~введите число~~~: "))
    if a == 1:
        Max.feed()
    elif a == 2:
        Max.water()
    elif a == 3:
        Max.walk()
        if Max.incident() is True:
            print("~~~игра закончена~~~")
            break
    elif a == 4:
        Max.scratch()
    elif a == 5:
        Max.play()
    else:
        print("~~~неправильная команда, попробуйте ещё раз~~~: ")
