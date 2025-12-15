import math
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user_pass = [
    ("bob", "123"),
    ("ann", "pass123"),
    ("mike", "password123"),
    ("liz", "pass123")
]

def clean_list(text):
    cleaned = []
    for x in text:
        if x != '' and x != '\n':
            cleaned_word = ''
            for char in x:
                if char.isalnum():
                    cleaned_word += char
            cleaned.append(cleaned_word)

    return cleaned

def print_graph(words_len: dict):
    sorted_dict = dict(sorted(words_len.items()))
    sorted_values = sorted(words_len.values())
    biggest = int(sorted_values[len(sorted_values) - 1])
    spaces = math.ceil((biggest - 3) / 2)
    print(f"LEN |{' ' * int(spaces)}COUNT{' ' * (int(spaces) if spaces % 2 == 0 else int(spaces - 1))}| WORDS")
    for k, v in sorted_dict.items():
        print(f"  {' ' if k < 10 else '' }{k}| {'*' * v}{' ' * (biggest - v)} | {v}")


def analyze(words):
    title = 0
    upper = 0
    lower = 0
    numbers = []
    words_len = dict()

    for word in words:
        if word.istitle():
            title += 1
        elif word.isupper():
            upper += 1
        elif word.islower():
            lower += 1
        elif word.isnumeric():
            numbers.append(int(word))

        if words_len.get(len(word)) is None:
            words_len[len(word)] = 1
        else:
            words_len[len(word)] = words_len.get(len(word)) + 1

    print("Titles: ", title)
    print("Upper: ", upper)
    print("Lower: ", lower)
    print("Numbers count: ", len(numbers))
    print("Numbers: ", sum(numbers))
    print_graph(words_len)


username = input("username: ")
password = input("password: ")

if (username, password) in user_pass:
    print("Welcome")
    picked_num = input(f"pick text from 1 to {len(TEXTS)}: ")
    if picked_num.isnumeric():
        picked_num = int(picked_num)
        if picked_num <= len(TEXTS) and picked_num > 0:
            picked_text = TEXTS[picked_num - 1]

            filtered = clean_list(picked_text.split(" "))
            num_words = len(filtered)

            print("Number of words: ", num_words)
            analyze(filtered)
        else:
            print("wrong text number, terminating the program..")
    else:
        print("wrong character, terminating the program..")
else:
    print("I don't know you, get out")