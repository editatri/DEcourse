'''
1. Напишите функцию, которая принимает JSON-строку и выводит данные в виде словаря
Python.
'''

def func(a):
   print(dict(a))


'''
2. Напишите код, который загружает данные из Excel-файла, подсчитывает количество строк и
выводит результат.
'''

import pandas as pd
file = pd.read_excel('weather.xlsx')
print(file.shape[0])


'''
3. Напишите функцию, которая загружает данные из API и обрабатывает их, выводя только
нужные поля. (по аналогии с примером, который мы смотрели на уроке)
'''


#Nationalize.io - Предсказывает национальность человека по его имени.

def nationalize(name):
    import pandas as pd
    import requests
    url = f'https://api.nationalize.io/?name={name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        probability = 0
        for i in data['country']:
            if i['probability'] > probability:
                probability = i['probability']
                country = i['country_id']
        data_df = pd.DataFrame([{'Probability': probability,
                                 'country': country}])
        return data_df
    else:
        return 'Something is wrong.'


print(nationalize('Edita'))

'''
4. Напишите программу, которая загружает данные из нескольких Excel файлов,
объединяет их и сохраняет в новый файл.
'''

import pandas as pd
file1 = pd.read_excel('weather.xlsx')
file2 = pd.read_excel('weather2.xlsx')
newFile = pd.concat([file1, file2])
newFile.to_excel('weather3.xlsx', index=False)


'''
5. Напишите код, который загружает данные из API, выполняет предварительную обработку
(например, фильтрацию) и сохраняет результат в Excel-файл.
'''

#С помощью этого API можно получить список университетов в указанной стране.

import pandas as pd
import requests
country = 'Belarus'
url = f'http://universities.hipolabs.com/search?country={country}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for i in data:
        if 'Minsk State Linguistic University' in i['name']:
            output_df = pd.DataFrame([{
                'University': i['name'],
                'web page': i['web_pages']
            }])
    output_df.to_excel('mslu_data.xlsx', index=False)
else:
    print('Error.')