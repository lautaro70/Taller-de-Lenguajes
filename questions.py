import random

words = {
    "general" : ["programa"],
    "programacion" : ["python","variable","funcion","bucle"],           #Genero el nuevo diccionario con las nuevas categorías.
    "tipos" : ["cadena","entero","lista"]
}

guessed = []
attempts = 6
puntaje = 0         #Inicializo la variable del puntaje.

print("¡Bienvenido al Ahorcado!")
print()

categoria_elegida = ""
while categoria_elegida not in words:
    print ("Categorias disponibles:")
    
    for categoria in words:
        print("-", categoria)                                                           #Ofrezo las opciones de categorías al usuario.
    categoria_elegida = input("Elegi una categoria de las brindadas: ").lower()         #La persona elige la categoria del juego.
    
    if categoria_elegida not in words:
        print("La categoría ingresada no existe. Intentá nuevamente")
        print()
        
print(f"Se jugará con la categoría de palabras '{categoria_elegida}'")
print()

word = random.choice(words[categoria_elegida])                                          #Elige una palabra al azar de la categoría elegida.


while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje += 6
        print(f"Puntaje final: {puntaje}")
        break
    
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()
     
    if (len(letter) == 1) and letter.isalpha():     #Condición en caso de ingresar más de una letra o caracter inválido.
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
    else:
        print ("Entrada no válida.")
        continue
    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0
    print(f"Puntaje final: {puntaje}")