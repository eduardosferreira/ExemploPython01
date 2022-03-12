segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horas = segundos // 3600

dias = horas//86400

segundos = segundos % 3600

minutos = segundos // 60

segundos = segundos % 60

if (horas >= 24): 
	dias = int(horas / 24)
	horas = int(horas % 24)

print("%s dias, %s horas, %s minutos e %s segundos." %(dias,horas,minutos,segundos))  