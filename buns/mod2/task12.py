
phone_number = input("Введите номер телефона: ")
purified_number = ''.join(phone_number.replace('(', '')
                         .replace(')', '').replace('-', '').split())
print(purified_number)

#phone_number = input("Введите номер телефона: ")
#number = ""

#for i in 0, 1, 4, 5, 6, 9, 10, 11, 13, 14, 16, 17, 18:
    #number += phone_number[i]
#print(number)