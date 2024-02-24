recordatorios = [
    ['2021-01-01', '11:00', 'Levantarse y ejercitar'],
    ['2021-07-15', '13:00', 'No hacer nada es feriado'],
    ['2021-09-18', '16:00', 'Ramadas'],
    ['2021-12-25', '00:00', 'Navidad'],
]

recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

for recordatorio in recordatorios:
    if recordatorio[0] == '2021-07-15':
        recordatorio[0] = '2021-07-16'

recordatorios = [recordatorio for recordatorio in recordatorios if recordatorio[2] != 'Día del trabajo']

recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

recordatorios.sort()

for recordatorio in recordatorios:
    print(recordatorio)