# TRY EXCEPT ELSE

# Também se observa a importância de definir strings e ints


vr_nome = input("Informe o seu nome: ")
vr_idade = input("Informe a sua idade: ")
#next_idade = int(vr_idade) + 1

try:
    next_idade = int(vr_idade) + 1 #VAR trazida pra dentro do try
except:
    print("ERRO: Idade precisa ser um número")
else:
    print("Seu nome é " + vr_nome + ", e você possue " + vr_idade + " anos de idade.")
    print("Logo, você terá " + str(next_idade) + " anos.")

