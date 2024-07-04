import pandas as pd
import random

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите новые данные (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
        elif choice == 7:
            src_file = input('Введите имя исходного файла: ')
            dest_file = input('Введите имя файла назначения: ')
            line_number = int(input('Введите номер строки для копирования: '))
            copy_line(src_file, dest_file, line_number)

        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные абонента\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Скопировать строку из одного файла в другой\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)

    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    return [record for record in phone_book if record['Фамилия'] == last_name]

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return f"Номер для {last_name} изменен на {new_number}"
    return "Фамилия не найдена"

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            return f"Запись для {last_name} удалена"
    return "Фамилия не найдена"

def find_by_number(phone_book, number):
    return [record for record in phone_book if record['Телефон'] == number]

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.strip().split(',')))
    phone_book.append(record)

def copy_line(src_file, dest_file, line_number):
    with open(src_file, 'r', encoding='utf-8') as src, open(dest_file, 'a', encoding='utf-8') as dest:
        lines = src.readlines()
        if 0 < line_number <= len(lines):
            dest.write(lines[line_number - 1])
            print(f'Строка номер {line_number} скопирована из {src_file} в {dest_file}')
        else:
            print('Неверный номер строки')

work_with_phonebook()
