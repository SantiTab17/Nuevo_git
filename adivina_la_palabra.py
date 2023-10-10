import random


def game(words: list):
    word = random.choice(words)
    hidden_letters = int(len(word) * 0.6)
    hidden_position = random.sample(range(len(word)), hidden_letters)
    hidden_word = ''
    attempts = 5
    # El enumerate devuelve un objeto iterable con el indice y el valor
    for i, letter in enumerate(word):
        if i in hidden_position:
            hidden_word += '_'
        else:
            hidden_word += letter
    while attempts > 0:

        print(
            f"Adivina la palabra: {hidden_word}\nTienes {attempts} intentos.")

        text = input("Introduce una letra o la solución completa: ")

        if len(text) == 1:

            new_hidden_word = ""
            success = False
            for index, letter in enumerate(word):
                if text == letter and hidden_word[index] == "_":
                    new_hidden_word += text
                    success = True
                else:
                    new_hidden_word += hidden_word[index]

            hidden_word = new_hidden_word

            if success:
                if word == hidden_word:
                    return (f"¡Has acertado! La palabra oculta era {word}.")

                else:
                    print("¡Has acertado la letra!")
            else:
                print("Letra no encontrada o ya visible.")
                attempts -= 1

        elif len(text) == len(word):
            if text == word:
                return (f"Ganaste! la palabra era: {word}.")
            else:
                print("Palabra incorrecta.")
                attempts -= 1
        else:
            print("Texto inválido.")

    if attempts == 0:
        return (f"Has perdido. La palabra oculta era {word}.")


print(game(['lemito66', 'murcielago', 'casa', 'perro', 'gato']))