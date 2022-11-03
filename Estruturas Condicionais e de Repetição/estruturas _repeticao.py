# texto = input("Informe um texto: ")
#texto = " "
#VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
#for letra in texto: 
#    if letra.upper() in VOGAIS 
#        print(letra, end="")
#else:
#    print()    # adiciona uma quebra de linha        




# Exemplo utilizando a fução built-in range 

#for numero in range(0, 11): 
#    print(numero, end=" ") 

#exibindo a tabuada de 5
#for numero in range(0, 51, 5): 
#    print(numero)   



#while True:
#    numero = int(input("Informe um número: "))

#    if numero == 10: 
#        break 

#print(numero)
#print("Fim!")

for numero in range(100):

   if numero % 2 == 0: 
       continue

print(numero, end=" ")
print("Fim!")
    