from alphabet import alphabet
from art import morsecode_welcome, morsecode_goodbye

print(morsecode_welcome)
print("Type the '!cmd-quit' to abort program")

abort_program = False

while not abort_program:
    plaintext_wordlist = input("Enter your plaintext word here: ")

    if plaintext_wordlist == '!cmd-quit':
        abort_program = True
        print(morsecode_goodbye)
        break

    word_to_join = []
    for word in plaintext_wordlist:
        candidate_word = word.upper()
        if candidate_word not in alphabet.keys():
            continue
        word_to_join.append(alphabet[candidate_word])

    result = " ".join(word_to_join)
    print(result)





