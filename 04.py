# Global Variables

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