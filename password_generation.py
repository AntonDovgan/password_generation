from random import choice

# symbols
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = "!#$%&*+-=?@^_"
# end symbols

# options
count = input('Сколько нужно сгенирировать паролей: ')
while count.isdigit() == False:
    print('Укажите число')
    count = input('Сколько нужно сгенирировать паролей: ')

length = input('Укажите длину пароля: ')
while length.isdigit() == False:
    print('Укажите число')
    length = input('Укажите длину пароля: ')

add_digits = input('Включить цифры? (Y/N): ')
while add_digits.lower() not in ['y', 'n']:
    print('Укажите "Y" или "N"')
    add_digits = input('Включить цифры? (Y/N): ')

add_lowercase_letters = input('Включать строчные буквы? (Y/N): ')
while add_lowercase_letters.lower() not in ['y', 'n']:
    print('Укажите "Y", "N"')
    add_lowercase_letters = input('Включать строчные буквы? (Y/N): ')

add_uppercase_letters = input('Включать прописные буквы? (Y/N): ')
while add_uppercase_letters.lower() not in ['y', 'n']:
    print('Укажите "Y", "N"')
    add_uppercase_letters = input('Включать прописные буквы? (Y/N): ')

add_punctuation = input('Включать специальные символы "!#$%&*+-=?@^_"? (Y/N): ')
while add_punctuation.lower() not in ['y', 'n']:
    print('Укажите "Y", "N"')
    add_punctuation = input('Включать специальные символы "!#$%&*+-=?@^_"? (Y/N): ')

rmv_bad_symbols = input('Исключить символы il1Lo0O? (Y/N):' ).strip()
while rmv_bad_symbols.lower() not in ['y', 'n']:
    print('Укажите "Y", "N"')
    rmv_bad_symbols = input('Исключить символы il1Lo0O? (Y/N):')
# end options


# function witch get answers and generate passwords
# def generate_password(add_digits, add_lowercase_letters, add_uppercase_letters, add_punctuation, rmv_bad_symbols):
#     chars = ''
#     if add_digits.lower() == 'y':
#         chars += digits
#     if add_lowercase_letters.lower() == 'y':
#         chars += lowercase_letters
#     if add_uppercase_letters.lower() == 'y':
#         chars += uppercase_letters
#     if add_punctuation.lower() == 'y':
#         chars += punctuation
#     if rmv_bad_symbols.lower() == 'y':
#         for i in 'il1Lo0O':
#             chars = chars.replace(i, '')
#
#     def print_pass(count, length, chars):
#         for i in range(count):
#             password = ''
#             for j in range(length):
#                 password += choice(chars)
#             print(password)
#
#     print_pass(count, length, chars)

# end function

# generate_password(add_digits, add_lowercase_letters, add_uppercase_letters, add_punctuation, rmv_bad_symbols)
