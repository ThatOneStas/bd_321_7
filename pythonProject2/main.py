import json


def SumNum(Num1, Num2):
    return Num1 + Num2


def runProg():
    # SumNum(int(input('Num1 - ')), int(input('Num2 - ')))
    temperature = int(input('Vvedit temperaturu: '))
    if temperature > 0:
        print('Teplo')
    else:
        print('Cholodno')


def Initials(Name, LastName, FathersName):
    try:
        intials = f'{LastName.capitalize()} {int(Name[0].upper())}. {FathersName[0].upper()}.'
        return intials
    except Exception as err:
        print('При введенні сталася помилка')


if __name__ == '__main__':
    # try:    # <--- якщо буде помилка то...
    #     num = 1/0
    # except Exception as err:
    #     print(err) # <--- ...виконається цей код.
    # finally: # <--- виконується за будь яких умов (можна не юзати)
    #     print('Some text')
    #     print('\n')

    # active = True
    # while active:
    #     try:
    #         runProg()
    #     except Exception as Err:
    #         print(Err)
    #     finally:
    #         ch = input('Чи бажаєте продовжити користування? (Y/N): ')
    #         if ch.lower() == 'n':
    #             active = False
    # Initials(input('Input your name: '),input('Input your lastname: '),input('Input your fathersname: '))

    def DogAdder():
        with open('zoo.json', 'r', encoding='utf-8') as file:
            zoo = json.load(file)
        name = input('Введіть ім`я собаки: ').capitalize()
        poroda = input('Введіть породу собаки: ').capitalize()
        favfood = input('Введіть улюблену їжу собаки: ').lower().title()
        zoo_frame = {
            'Name': name,
            'Poroda': poroda,
            'FavFood': favfood
        }
        zoo.append(zoo_frame)
        with open('zoo.json', 'w', encoding='utf-8') as f:
            json.dump(zoo, f)
            
    def DogFinder():
        with open('zoo.json', 'r', encoding='utf-8') as file:
            zoo = json.load(file)
        FinderCond = input('Введіть назву породи: ').capitalize()
        for dog in zoo:
            if FinderCond == dog['Poroda']:
                print(dog)
    def DogFood():
        with open('zoo.json', 'r', encoding='utf-8') as file:
            zoo = json.load(file)
        FoodCond = input('Введіть корм: ').lower().title()
        for dog in zoo:
            if dog['FavFood'] == FoodCond:
                print(dog)


    try:
        with open('zoo.json', 'r', encoding='utf-8') as file:
            zoo = json.load(file)
    except Exception as error_adder:
        with open('zoo.json', 'w', encoding='utf-8') as f:
            json.dump([], f)
        RezCond = input('Файл був створений. Він пустий.\nБажаєте добавити собаку? (Y/N): ')
        if RezCond.lower() == 'y':
            DogAdder()
    GlobalCond = input('Що бажаєте зробити?\n- Добавити тварину (1)\n- Знайти за породою (2)\n- Харчування за породою (3)\n--> : ')
    if GlobalCond == '1':
        DogAdder()
    elif GlobalCond == '2':
        DogFinder()
    elif GlobalCond == '3':
        DogFood()
