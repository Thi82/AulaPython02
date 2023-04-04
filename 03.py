#WHILE LOOP

'''
vr_nome = input("Informe o seu nome: ")
vr_idade = input("Informe a sua idade: ")
#next_idade = int(vr_idade) + 1

try:
    next_idade = int(vr_idade) + 1
except:
    print("ERRO: Idade precisa ser um número")
else:
    print("Seu nome é " + vr_nome + ", e você possue " + vr_idade + " anos de idade.")
    print("Logo, você terá " + str(next_idade) + " anos.")
'''

# '''
# frase = "Olá mundo,"
# frase2 = "hoje eu acordei"
# frase3 = "feliz, porém com fome."
#
# print(frase, frase2, frase3)
#
# print(frase)
# print(frase2)
# print(frase3)
#
# print("    /\ ")
# print("   /\/\ ")
# print("  /\/\/\ ")
# print(" /\/\/\/\ ")
# print("/\/\/\/\/\ ")
# print("    | | ")
# print("    | | ")
# print("    | | ")
# print("   /   \ ")
# '''

#print(n)
#
# n = "012" # IMPRIME a identidade string 0
# print(n)
#
# n = 1 # ASSIMILO um valor
# print (n)
#
# n = n + 1 # Incremento
# print(n)

# n = 0 # CRIA a identidade 0
#
# print("Iniciando")
#
# while n < 5:
#     print("O valor atual é: " + str(n))
#     n = n + 1
# print("Fim")

'''
senha = ""

while not senha == "123456":
    senha = input("Insira a senha: ")

print("Acesso Permitido")
'''

# vr_nome = input("Informe o seu nome: ")
# str_idade = input("Informe a sua idade: ")
# #str_idade = int(str_idade)
#
# try:
#     idade = int(str_idade)
# except:
#     print("ERRO: Idade precisa ser um número")
# else:
#     print("Seu nome é " + vr_nome + ", e você possue " + str(idade) + " anos de idade.")
#     print("Logo, você terá " + str(idade + 1) + " anos.")

'''
# nome = input("Informe o seu nome: ")
# idade = 0
# while idade == 0: # ENQUANTO o número 0 for colocado, o programa insiste na pergunta
#     str_idade = input("Informe a sua idade: ")
#     try:
#         idade = int(str_idade)
#     except:
#         print("ERRO: Idade precisa ser um número")
# 
# print("Seu nome é " + nome + ", e você possue " + str(idade) + " anos de idade.")
# print("Logo, você terá " + str(idade + 1) + " anos.")
'''

# Função ask age
def ask_age():
    age_int = 0
    while age_int == 0:
        age_str =  input("Sua idade? ")
        try:
            age_int = int(age_str)
        except:
            print("ERRO")
    return age_int # RETURN permite utilizar a variável fora da função,
                   # Caso contrário, só é possivel com
                   # Variáveis globais.

# Pergunta o nome
name = ""
while name == "":
    name = input("Seu nome? ")

# Função Ask age invocada
age = ask_age()

print("Seu nome é " + name + ", você tem " + str(age) + " anos.")
print("Logo você terá " + str(age + 1))



