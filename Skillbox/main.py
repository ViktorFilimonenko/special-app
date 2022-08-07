def annuity(k, p):
    t = pow(p + 1, k)
    return p * t / (t - 1)


def print_info(j, s, i):
    print(f'\nПериод: {j}')
    print(f'Остаток долга на начало периода: {s:.2f}')
    print(f'Выплачено процентов: {s * i:.2f}')
    ds = a - s * i
    print(f'Выплачено тела кредита: {ds:.2f}')
    return s - ds


credit_amount = float(input('Введите сумму кредита: '))
time = int(input('На сколько лет выдан? '))
percent = float(input('Сколько процентов годовых? ')) / 100

a = credit_amount * annuity(time, percent)
for j in range(1, 4):
    s = print_info(j, credit_amount, percent)

print(f'\nОстаток долга: {credit_amount:.2f}\n')
print('==============================\n')

contract_time = int(input('На сколько лет продляется договор? '))
rate_increase = float(input('Увеличение ставки до: ')) / 100
n = contract_time + time - 3

a = credit_amount * annuity(n, rate_increase)
for j in range(1, n + 1):
    s = print_info(j, credit_amount, rate_increase)

print(f'\nОстаток долга: {contract_time:.2f}')

---------------------------------------------------------------------

def annuity(k, p):
    t = pow(p + 1, k)
    return p * t / (t - 1)


def print_info(j, s, i):
    print(f'\nПериод: {j}')
    print(f'Остаток долга на начало периода: {s:.2f}')
    print(f'Выплачено процентов: {s * i:.2f}')
    ds = a - s * i
    print(f'Выплачено тела кредита: {ds:.2f}')
    return s - ds


s = float(input('Введите сумму кредита: '))
n = int(input('На сколько лет выдан? '))
i = float(input('Сколько процентов годовых? ')) / 100

a = s * annuity(n, i)
for j in range(1, 4):
    s = print_info(j, s, i)

print(f'\nОстаток долга: {s:.2f}\n')
print('==============================\n')

n2 = int(input('На сколько лет продляется договор? '))
i2 = float(input('Увеличение ставки до: ')) / 100
n = n2 + n - 3

a = s * annuity(n, i2)
for j in range(1, n + 1):
    s = print_info(j, s, i2)

print(f'\nОстаток долга: {s:.2f}')