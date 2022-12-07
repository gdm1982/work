# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
user_name = ''
user_age = 0
phone_number = ''
e_mail = ''
index = ''
postal_address = ''
add_info = ''
# IP info
ogrn_ip = ''
inn = ''
pay_acc = ''
bank_name = ''
bik = ''
corr_acc = ''


def general_info_user(user_name_parameter, user_age_parameter, phone_number_parameter,
                      e_mail_parameter, index_parameter, postal_address_parameter, add_info_parameter):
    print(SEPARATOR)
    print('Имя: ', user_name_parameter)
    if 11 <= user_age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif user_age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= user_age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', user_age_parameter, years_parameter)
    print('Телефон:', phone_number_parameter)
    print('E-mail: ', e_mail_parameter)
    print('Почтовый индекс: ', index_parameter)
    print('Почтовый адрес: ', postal_address_parameter)
    if add_info:
        print('')
        print('Дополнительная информация:')
        print(add_info_parameter)

def test_sybol_sum(parametr, number, name):
    while parametr < 0 or len(str(parametr)) != number:
        parametr = int(input(f'Вы ошиблись! Должно быть {number} цифр. \nВведите {name}: '))
    return parametr



print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                user_name = input('Введите имя: ')
                while 1:
                    # validate user age
                    user_age = int(input('Введите возраст: '))
                    if user_age > 0:
                        break
                    print('Возраст должен быть положительным')

                user_phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone_number = ''
                for numeral in user_phone_number:
                    if numeral == '+' or ('0' <= numeral <= '9'):
                        phone_number += numeral

                e_mail = input('Введите адрес электронной почты: ')
                user_index = input('Введите почтовый индекс: ')
                index = ''
                for symbol_index in user_index:
                    if symbol_index == '0' or symbol_index == '1' or symbol_index == '2' or symbol_index == '3' \
                            or symbol_index == '4' or symbol_index == '5' or symbol_index == '6'\
                            or symbol_index == '7' or symbol_index == '8' or symbol_index == '9':
                        index += symbol_index
                postal_address = input('Введите почтовый адрес: ')
                add_info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # IP info
                ogrn_ip = int(input('Введите ОГРН ИП: '))
                ogrn_ip = test_sybol_sum(ogrn_ip, 15, 'ОГРН ИП')
                inn = int(input('Введите ИНН: '))
                inn = test_sybol_sum(inn, 12, 'ИНН')
                pay_acc = int(input('Введите Расчетный счет: '))
                pay_acc = test_sybol_sum(pay_acc, 20, 'Расчетный счет')
                bank_name = input('Введите Имя банка: ')
                bik = input('Введите БИК: ')
                corr_acc = input('Введите Корреспондентский счет: ')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(user_name, user_age, phone_number, e_mail, index, postal_address, add_info)

            elif option2 == 2:
                general_info_user(user_name, user_age, phone_number, e_mail, index, postal_address, add_info)

                # IP info
                print('')
                print('Информация о предпринимателе')
                print('ОГРН ИП: ', ogrn_ip)
                print('ИНН: ', inn)
                print('Банковские рекыизиты')
                print('Расчетный счет: ', pay_acc)
                print('Имя банка: ', bank_name)
                print('БИК: ', bik)
                print('Корреспондентский счет: ', corr_acc)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')