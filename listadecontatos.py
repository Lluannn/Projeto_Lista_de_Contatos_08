idade= 0 
try:  
  while idade <= 0:
   nome= input("digitr o seu nome:")
   email= input("digite o seu email:")
   idade= int(input("informe a  sua idade:"))
    
  if idade < 18:
    print("menor de idade, proibido para uso!")
  elif idade >= 18:
    print("maior de idade, liberado para uso")

  with open("cadastros.txt", "a") as cadastro:
   cadastro.write( nome + "|" + email + "|" + idade + "\n" )
   
except:
  print("inválido!!")
