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
	print('Program zako�czy� si� nieoczekiwanym b��dem. Moz�sz to zg�osi� pod adresem pomocautor.pl')

