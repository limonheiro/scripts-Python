import csv, json, requests
#converter csv para json, supondo que a primeira linha seja o cabeçalho
urls = ['http://dados.ifmt.edu.br/dataset/0b1504bd-9568-449c-aa68-22166ba27669/resource/269aee3c-a636-43e9-8a5c-20aa20617b4e/download/unidadeorganizacional.csv']

for url in urls:
    r = requests.get(url)

    arquivo = r.text.splitlines()
    fl = arquivo[0] # cabeçalho do arquivo csv
    namefile = url.split('/')[-1].split('.csv')[0] # retorna o nome do arquivo
    
    with open(f'{namefile}.json', 'w', encoding='utf-8') as jsonfile:
        fieldnames = (fl.split(','))
        reader = csv.DictReader(arquivo, fieldnames)
        jsonfile.write('[')
        for row in reader:
            json.dump(row, jsonfile, ensure_ascii=False)
            jsonfile.write(',')
            jsonfile.write('\n')
        jsonfile.write(']')
    print(namefile+".json Criado")