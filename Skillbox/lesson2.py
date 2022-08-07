def annuity(years, bid):
    year_rate = pow(bid + 1, years)
    return bid * year_rate / (year_rate - 1)


def print_info(period, credit, interest_paid):
    print(f'\nПериод: {period}')
    print(f'Остаток долга на начало периода: {credit:.2f}')
    print(f'Выплачено процентов: {credit * interest_paid:.2f}')
    ds = a - credit * interest_paid
    print(f'Выплачено тела кредита: {ds:.2f}')
    return credit - ds


credit_amount = float(input('Введите сумму кредита: '))
time = int(input('На сколько лет выдан? '))
percent = float(input('Сколько процентов годовых? ')) / 100

a = credit_amount * annuity(time, percent)
for loan_period in range(1, 4):
    credit_amount = print_info(loan_period, credit_amount, percent)

print(f'\nОстаток долга: {credit_amount:.2f}\n')
print('==============================\n')

contract_time = int(input('На сколько лет продляется договор? '))
rate_increase = float(input('Увеличение ставки до: ')) / 100
order = contract_time + time - 3

a = credit_amount * annuity(order, rate_increase)
for j in range(1, order + 1):
    credit_amount = print_info(j, credit_amount, rate_increase)

print(f'\nОстаток долга: {credit_amount:.2f}')