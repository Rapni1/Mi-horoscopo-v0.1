#Horoscopo Python V0.1 - Mi primer proyecto en python.
#Autor: Rapni
def obtener_signo(mes, dia):
	if (mes == 3 and dia >= 21) or (mes == 4 and dia <=19):
		return "Aries"
	elif (mes == 4 and dia >= 20) or (mes == 5 and dia <=20):
		return "Tauro"
	elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
		return "Geminis"
	elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
		return "Cancer"
	elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
		return "Leo"
	elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
		return "Virgo"
	elif (mes == 9 and dia >=23) or (mes == 10 and dia <= 22):
		return "Libra"
	elif (mes == 10 and dia >= 23) or (mes == 11 and dia <=21):
		return "Escorpio"
	elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
		return "Sagitario"
	elif (mes == 12 and dia >= 22) or (mes ==1 and dia <= 19):
		return "Capricornio"
	elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
		return "Acuario"
	elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
		return "Piscis"
	else:
		return "Signo no valido o no encontrado"
dia = int(input("Ingrese su dia de nacimiento (1, 31) :"))
mes = int(input("Ingrese su mes de nacimiento (1, 12) :"))
signo = obtener_signo(mes, dia)
print(f'Tu signo es: {signo}')
