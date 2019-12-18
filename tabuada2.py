#!/usr/bin/python


print "\t\t\t****** menu ******\n "
print "\t\t 1 -- Tabuada de n\n"
print "\t\t 2 -- Tabuada de intervalo de n a m\n"
print "\t\t 0 -- Terminar o Programa\n"



escolha = -1
while escolha != 0:
  
  k = input('\tOperacao do menu: ')
  
  if (k < 0 or k > 2) :
    if k == 0 :
      print "\tPrograma encerrado "
    else:
      print "\tOpecao nao existente"
  if k > 0:
    if k == 1:
      n = input('\tvalor n : ')
      print("\n")
      i = 1
      j = 1;
      while j < n+1:
        i = 1
        while i < 11:
          print "\t","",j," * ", "", i, "=", "",j * i
          i = i + 1
        j = j+1
        print "\n\n"
    else:
      n = input('\tvalor n: ')
      m = input('\tvalor m: ')
      while n < m+1:
        i = 1
        while i < 11:
          print "\t","",n," * ", "", i, "=", "",n * i
        n = n + 1
        print("\n")
    escolha = input('\tOperacao do menu: ')
        


