# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(**params):
    print(f'Имя: {name}, Фамилия: {family}, : {year}, : {city}, : {email}, : {phone}')

name = input('Введите имя: ')
family = input('Введите фамилию: ')
year = int(input('Введите дату рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')

user_info(name=name, family=family, year=year, city=city, email=email, phone=phone)

