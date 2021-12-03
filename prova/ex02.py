def main():
    hr_inicial = int(input('Digite a hora inicial:\n'))
    min_inicial = int(input('Digite o minuto inicial:\n'))
    hr_final = int(input('Digite a hora final:\n'))
    min_final = int(input('Digite o minuto final:\n'))

    if hr_final > hr_inicial:
        hora_total = (hr_final - hr_inicial)
    else:
        hora = 24 - (hr_inicial)
        hora_total = hora + hr_final
    if min_final > min_inicial:
        minuto_total = (min_final - min_inicial)
    elif min_final == min_inicial:
        minuto_total = 0
    else:
        hora_total = hora_total - 1
        minutos = (min_inicial - min_final)
        minuto_total = 60 - minutos
    print('O jogo durou %d hora(s) e %d minutos(s)' % (hora_total,minuto_total))
main()