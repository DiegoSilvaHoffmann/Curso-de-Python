cidade = str(input('Indique o nome de uma cidade: ')).strip()
print('Essa cidade comeca com palavra Santo? {}'.format(cidade[:5].upper() == 'SANTO'))
