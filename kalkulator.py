def Dodawanie(a,b):
	return a+b 
	
def get_info():
	print('Program kalkulator. Autor: Jacek')
	
get_info()

try:
	l1 = int(input())
	l2 = int(input())
	print(dodawanie(l1,l2))
except:
	print('Program zakoñczy³ siê nieoczekiwanym b³êdem. Mozêsz to zg³osiæ pod adresem pomocautor.pl')

