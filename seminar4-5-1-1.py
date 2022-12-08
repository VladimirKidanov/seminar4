# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

with open('polynomial_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('polynomial_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('polynomial_1.txt','r') as file:
    polynomial_1 = file.readline()
    list_of_polynomial_1 = polynomial_1.split()


with open('polynomial_2.txt','r') as file:
    polynomial_2 = file.readline()
    list_of_polynomial_2 = polynomial_2.split()

print(f'{list_of_polynomial_1} + {list_of_polynomial_2}')
sum_polynomial = list_of_polynomial_1 + list_of_polynomial_2

with open('sum_polynomial.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_polynomial_1} + {list_of_polynomial_2}')