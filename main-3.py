# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
file = open('files/text-3.txt', 'r', encoding='utf-8')

lines = file.readlines()

minimum = 20000
total_salary = 0

personal = []
salaries = []

for line in lines:
    if line.strip().replace(' ', ''):
        lst = line.strip().split()
        salary = int(lst[1])
        salaries.append(salary)
        total_salary += salary
        if int(lst[1]) < minimum:
            personal.append(lst[0])

personal = ', '.join(personal)
print(f'Данные сотрудники имеют зарплату меньше {minimum}: {personal}')
print(f'Общая сумма зарплаты составляет: {total_salary}')
print(f'Средняя зарплата составляет: {sum(salaries) / len(salaries)}')
file.close()
