import json  # Импортируем модуль для работы с JSON файлами.
file = open("fish.json", 'r', encoding='utf-8')  # Открываем файл fish.json в режиме чтения с кодировкой UTF-8.
data = json.load(file)  # Загружаем содержимое JSON файла в переменную `data`.
counter = 0  # Инициализируем счетчик операций.
run = True

# Запускаем бесконечный цикл для работы программы до выхода пользователя.
def menu():
    global counter
    # Выводим текстовое меню для выбора действия.
    print("""
        1: Вывести все записи 
        2: Вывести запись по полю 
        3: Добавить запись 
        4: Удалить запись по полю 
        5: Выйти из программы
        """)

    # Обработка действия 1: Вывод всех записей.
def Statistic():
        global counter
        for fish in data:  # Перебираем все записи (объекты) из списка `data`.
            print(f"""
            Номер записи: {fish['id']}, 
            Общее название: {fish['name']},                       
            Латинское название: {fish['latin_name']}, 
            Пресноводная: {fish['is_salt_water_fish']},    
            Кол-во подвидов: {fish['sub_type_count']} 
            """)
        counter += 1  # Увеличиваем счетчик операций.

    # Обработка действия 2: Поиск записи по полю `id`.
def StatNumb():
        global counter
        id = int(input("Введите номер рыбы: "))  # Запрашиваем номер записи.
        find = False  # Переменная для проверки, была ли найдена запись.
        for fish in data:  # Перебираем все записи.
            if id == fish['id']:  # Сравниваем введенное значение с полем `id` записи.
                print(f"""
                Номер записи: {fish['id']}, 
                Общее название: {fish['name']},                       
                Латинское название: {fish['latin_name']}, 
                Пресноводная: {fish['is_salt_water_fish']},    
                Кол-во подвидов: {fish['sub_type_count']} 
                """)
                find = True  # Если запись найдена, устанавливаем `find` в True.
                break  # Прекращаем дальнейший поиск.
        counter += 1  # Увеличиваем счетчик операций.
        if not find:  # Если запись не найдена, выводим сообщение.
            print("Запись не найдена.")

    # Обработка действия 3: Добавление новой записи.
def AddFish():  
        global counter 
        id = int(input("Введите номер рыбы: "))          
        name = input("Введите общее название рыбы: ")  
        latin_name = input("Введите латинское название рыбы: ")  
        is_salt_water_fish = input("Введите, является ли рыба пресноводной (да/нет): ")  
        sub_type_count = input("Введите количество подвидов этой рыбы: ")

            # Формируем новый объект записи.
        new_fish_records = {
                'id': id,
                'name': name,
                'latin_name': latin_name,
                'is_salt_water_fish': True if is_salt_water_fish.lower() == 'да' else False, 
                'sub_type_count': sub_type_count
            }

        data.append(new_fish_records)  # Добавляем новую запись в список.
        with open("fish.json", 'w', encoding='utf-8') as out_file:  # Открываем файл для записи.
            json.dump(data, out_file)  # Сохраняем обновленный список в файл.
        print("Запись успешно добавлена.")
        counter += 1  # Увеличиваем счетчик операций.

    # Обработка действия 4: Удаление записи по полю `id`.
def DeleteFish():
        global counter
        id = int(input("Введите номер рыбы: "))  # Запрашиваем номер записи.
        find = False  # Переменная для проверки, была ли найдена запись.
        for fish in data:  # Перебираем записи.
            if id == fish['id']:  # Если запись найдена.
                data.remove(fish)  # Удаляем запись из списка.
                find = True  # Устанавливаем `find` в True.
                break  # Прекращаем поиск.
        if not find:  # Если запись не найдена, выводим сообщение.
            print("Запись не найдена.")
        else:  # Если запись удалена, сохраняем изменения в файл.
            with open("fish.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)  # Сохраняем обновленный список.
            print("Запись успешно удалена.")
        counter += 1  # Увеличиваем счетчик операций.

    # Обработка действия 5: Завершение работы программы.
def EndProgramm():
        global run
        global counter
        print(f"""Программа завершена.
               Количество операций: {counter}""")  # Выводим сообщение о завершении и количество операций.
        run = False

def main():
    while run: 
        menu()
        num = int(input("Введите номер действия: "))
        if num == 1: 
            Statistic()
        elif num == 2:
            StatNumb()
        elif num == 3:
            AddFish()
        elif num == 4:
            DeleteFish()
        elif num == 5:
            EndProgramm()
        else:
            print("Такого номера нет")

main()
