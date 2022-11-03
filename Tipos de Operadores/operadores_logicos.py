# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or True)
print(False or False or False) 

saldo = 1000
saque = 200 
limite = 100 
conta_especial = True 


exp = saldo >= saque and saldo <= limite or conta_especial and saldo >= saque 
print(exp)

exp_2 = (saldo >= saque and saldo <= limite) or (conta_especial and saldo >= saque) 
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saldo <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque) 

exp_3 = conta_especial_com_saldo_suficiente or conta_normal_com_saldo_suficiente 
print(exp_3) 
