import random

def guess_number():
    secret_number = random.randint(1, 100)
    num_guesses = 0
    
    while True:
        guess = int(input("Digite um número entre 1 e 100: "))
        num_guesses += 1
        
        if guess < secret_number:
            print("Muito baixo, tente novamente!")
        elif guess > secret_number:
            print("Muito alto, tente novamente!")
        else:
            print(f"Parabéns, você acertou em {num_guesses} tentativas!")
            break

guess_number()

