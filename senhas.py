import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada:", senha_gerada)

# Definimos a função gerar_senha que recebe um argumento tamanho que indica o número de caracteres que a senha deve ter.
# Na próxima linha, criamos uma string caracteres que contém todas as letras minúsculas e maiúsculas, todos os dígitos numéricos e todos os caracteres de pontuação. Esses caracteres serão usados para construir a senha.