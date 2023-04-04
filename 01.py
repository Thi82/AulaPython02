# VARIAVEIS, STRINGS, E INTEIROS

# Obs: A importância de separar string de int,
# ou definir os dois parar trabalharem juntos

var_nome = input("Qual o seu nome? ") #USANDO o próprio input como variável
var_idade = 20
var_idade2 = var_idade + 1 # Vai ser transformado em INT no código
var_idade_namo = "27"
var_idade3 = str(var_idade_namo) + str(1) # Vai ser transformado em STR
var_objeto = "Arvore"
var_nome2 = "Chico"
var_namorada = "Rosinha"

print(type(var_idade))
print(type(var_idade2))

# int : integer/inteiro : 0, 1, 2, 3, ... -3, -2, -1 etc ...
# str(30) -> "30"

# flt: float/flutuante : 1.2, 4.3, 7.8 ... -7.8, -4.3, -1.2 ...etc
# booleans: True/False

#print("Este objeto é uma " + var_objeto)

# Strings e inteiros não se misturam na mesma escrita, É preciso definir cada um
# seja no código, seja na variável lá em cima

print("Meu nome é " + var_nome + ", eu tenho " + (str(var_idade)) + " anos.")
print("O nome da minha namorada é " + var_namorada + ".")
print("Sim, " + var_namorada + " é uma moça bonita. Ela tem " + var_idade_namo + " anos.")

print("Logo, eu terei " + (str(var_idade2))) # STR + INT transformado em STR no código = OK
print("Logo, ela terá " + var_idade3) # STR + INT transformado em STR na variável = OK