# print('\n> ')
print()
print('Enter the credit principal:')
credit_principal = int(input())
print(credit_principal)
print('What do you want to calculate?\n'
      + 'type "m" - for count of months,\n'
      + 'type "p" - for monthly payment:')
option = input()
print(option)
if option == 'm':
    print('Enter monthly payment:')
    m_payment = int(input())
    print(m_payment)
    print('It takes '
          + str(round(credit_principal / m_payment))
          + ' months to repay the credit')
elif option == 'p':
    print('Enter count of months:')
    periods = int(input())
    m_payment = int(credit_principal / periods)
    if credit_principal % periods == 0:
        print('Your monthly payment = ' + str(m_payment))
    else:
        print('Your monthly payment = '
              + str(int(m_payment) + 1)
              + ' with last month payment = '
              + str(credit_principal - (periods - 1) * (m_payment + 1)))
# else:
#     print('You write wrong type argument!\n'
#           + 'Repeat, i give you another chance.')
