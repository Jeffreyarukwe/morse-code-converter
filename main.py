from art import morsecode_welcome, morsecode_goodbye
from decode import decode
from encode import encode

print(morsecode_welcome)
print("Type the '!cmd-quit' to abort program")

abort_program = False
morse_symbols = ['*', '-', '/', ' ']

while not abort_program:
    to_encode = False

    text = input("Enter your text here: ")

    if text == '!cmd-quit':
        abort_program = True
        print(morsecode_goodbye)
        break

    for char in text:
        if char not in morse_symbols:
            to_encode = True
            break

    if to_encode:
        print(encode(text))
    else:
        print(decode(text))
