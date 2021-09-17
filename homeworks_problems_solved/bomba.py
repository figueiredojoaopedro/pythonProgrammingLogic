from math import*

vazao_bomba = float (input("Digite a vazão da bomba em l/s: "))
capacidade_reservatorio = float ( input ("Digite a capacidade do reservatório: ") )

tempo_horas = capacidade_reservatorio // (vazao_bomba*3600)
tempo_minutos = (capacidade_reservatorio // (vazao_bomba*60)) - (tempo_horas * 60)
tempo_segundos = (capacidade_reservatorio // vazao_bomba) - (tempo_minutos * 60) - (tempo_horas * 3600)

int(tempo_horas)
int(tempo_minutos)
int(tempo_segundos)

print ("Tempo necessário para encher o reservatório: %d:%d:%d" % (tempo_horas, tempo_minutos, tempo_segundos))