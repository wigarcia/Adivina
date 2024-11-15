import random
import sys  # Para detectar la tecla ESC

def jugar():
    numero_secreto = random.randint(1, 10)
    intentos = 3

    print("\n¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 10. Tienes 3 intentos para adivinarlo.")
    print("Presiona 'ESC' para salir del juego en cualquier momento.")

    while intentos > 0:
        entrada = input("Introduce tu número o 'ESC' para salir: ").strip()
        
        if entrada.upper() == "ESC":
            print("Juego terminado. ¡Hasta la próxima!")
            sys.exit()  # Salida del programa

        if not entrada.isdigit():
            print("Por favor, introduce un número válido.")
            continue
        
        adivinanza = int(entrada)
        
        if adivinanza == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Fallaste. Te quedan {intentos} intentos.")
            else:
                print(f"Lo siento, has perdido. El número era {numero_secreto}.")
    
    volver_a_jugar()

def volver_a_jugar():
    print("\n¿Quieres intentar otra vez? (S/N)")
    respuesta = input().strip().upper()
    if respuesta == "S":
        jugar()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")
        sys.exit()

# Inicia el juego
jugar()
