segundos=int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias=segundos//(3600*24)
segRest=segundos%(3600*24)
horas=segRest//3600
segRest=segRest%3600
minutos=segRest//60
segRest=segRest%60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segRest,"segundos.")
