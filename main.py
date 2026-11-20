with open("dna.txt", "r") as arquivo:
  dna = arquivo.read()
def subsequencia(abc_s):
 a = 0
 cba = ""
 for i in dna:
   if a == len(abc_s):
     break
   elif abc_s[a] == i:
     cba += i
     a += 1
 if cba == abc_s:
   print("A Subsequência",cba,"foi encontrada")
def subscadeia(abc_c) :
 n = 0
 cba = ""
 for i in dna:
  if len(cba) < len(abc_c) :
   cba = cba + i
   continue
  cba = cba.replace(cba[0],"",1)
  cba += i
  if cba == abc_c:
   n += 1
   print("A Subcadeia", cba, "foi encontrada")
 if n > 0:
  print("A Subcadeia",abc_c,"foi encontrada",n,"vezes")
Num = input("Digite 1 para buscar Subcadeia ou Digite 2 para buscar Subsequência : ")
if Num == "1" :
 abc_c = input("Digite uma Subcadeia : ")
 subscadeia(abc_c)
elif Num == "2" :
 abc_s = input("Digite uma Subsequência : ")
 subsequencia(abc_s)

