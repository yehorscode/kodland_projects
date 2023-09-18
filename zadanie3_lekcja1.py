meme_dict = {
            "cringe": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "lol": "Częsta reakcja na coś zabawnego",
            }

while True:
    word = input("Wpisz słowo, którego nie rozumiesz:")
    if word.lower() in meme_dict.keys():
        print(meme_dict[word])
    elif word.lower() == "exit":
        quit()
    else:
        print("Kolego, ale ja nie wymyślam słów")