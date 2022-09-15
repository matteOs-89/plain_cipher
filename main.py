
print("WELCOME TO OS' CIPHER")
alphabet = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z", "?", "!", "@", " ", "a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z", "?", "!", "@", " ", "a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z", "?", "!", "@", " "]


code_is_on = True


def encypted_code(letter, number):
    code = ""
    for item in letter:
        pos = alphabet.index(item)
        newpos = pos + number
        code += alphabet[newpos]
    return code


def decypted_code(letter, number):
    decode = ""
    for item in letter:
        pos = alphabet.index(item)
        newpos = pos - number
        decode += alphabet[newpos]
    return decode


def run_code(start, msg, num):
    if start == "encode":
         return encypted_code(msg, num)

    elif start == "decode":
         return decypted_code(msg, num)


while code_is_on:
    start = input("Good day, please state if you are here to 'ENCODE', 'DECODE' or type 'QUIT' to leave !: ").lower()

    if start == "encode" or start == "decode":
        msg = input("Please type message in plain text: ").lower()
        num = int(input("please type for secret code shift number: "))
        num = num % 30
        print(run_code(start, msg, num))


    elif start == "quit":
        code_is_on = False

    else:
        print("Please input the right command! ")







