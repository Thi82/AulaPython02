# ELIFs

age = 0
# Função ask age
def ask_age():
    global age # GLOBAL dentro da funcão
    while age == 0:
        age_str = input("Sua idade? ")
        try:
            age = int(age_str)
        except:
            print("ERRO")
# Pergunta o nome
name = ""
while name == "":
    name = input("Seu nome? ")

# Função Ask age invocada, agora via global variable (observar 03)
ask_age()

print("Seu nome é " + name + ", você tem " + str(age) + " anos.")
print("Logo você terá " + str(age + 1))

# == equalidade
# > >=
# < <=
# bool: True / False
# elif : else if

# AQUI, temos uma condição if que atua como boolean
# Cria uma variavel cond para mostrar o comportamento atravpes de type()

# cond = age >= 18
# print(cond)
# print(type(cond))

if age == 17: # Idade exatos 17
    print("Tá ficando de maior")
elif 10 <= age < 18:
    print("Você é adolescente")
elif age == 1 or age == 2: # idade exatos 18
    print("Você é um bebê!")
elif age == 18:
    print("Você agora é adulto. Parabéns")
elif age >= 18:
    print("Você agora é adulto. Parabéns")
elif age > 60:  # idade = > 18
    print("Você é um senhor.")
# if age <= 18: # idade = < 18
#     print("Você é menor")
else:
    print("Você é menor")