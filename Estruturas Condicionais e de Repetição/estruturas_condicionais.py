# MAIOR_IDADE = 18
#IDADE_ESPECIAL = 15

#idade = int(input("Informe sua idade: "))

#if idade >= MAIOR_IDADE: 
#    print("Maior de idade, pode tirar a CNH.")

#if idade < MAIOR_IDADE: 
#    print("Ainda não pode tirar a CNH.")  
    


#if idade >= MAIOR_IDADE: 
#    print("Maior de idade, pode tirar a CNH.") 
#else: 
# print("Ainda não pode tirar a CNH.")    

#if idade >= MAIOR_IDADE: 
#    print("Maior de idade, pode tirar a CNH.") 
#elif idade >= IDADE_ESPECIAL: 
#    print("Pode fazer aulas teoricas, mas não pode fazer aulas práticas.")    
#else: 
# print("Ainda não pode tirar a CNH.")    


#conta_normal = False
#conta_universitaria = False
#conta_especial = True

#saldo = 2000 
#saque = 1500
#cheque_especial = 450 


#if conta_normal: 

#    if saldo >= saque:
#        print("Saque realizado com sucesso!")
#    elif saque <= (saldo + cheque_especial):
#        print("Saque realizado com sucesso!") 
#    else:
#        print("Não foi possível realizar o saque. Saldo insuficiente!")  

#elif conta_universitaria:

#    if saldo >= saque: 
#        print("Saque realizado com sucesso!")
#    else:
#        print("Saldo insuficiente!")

#elif conta_especial:

#    print("Conta Especial selecionada!")                    
#else:
#    print("Conta não reconhecida, entre em contato com o gerente.") 

saldo = 2000
saque = 500
 
status = "Sucesso" if saldo >= saque else "falha" 

print(f"{status} ao realizar o saque!") 
