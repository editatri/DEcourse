'''
1. Напишите функцию, которая загружает данные из API и фильтрует их по заданному
пользователем условию.
'''

import pandas as pd
import requests

#фильтром служит аргумент функции, при введении которого будут отображаться данные только за заданный год
def func(year):
    url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
    response = requests.get(url)
    if response.status_code == 200:
        output1 = response.json()
        output2 = output1['data']
        for i in output2:
            if int(i['Year']) == year:
                output_df = pd.DataFrame([{
                    'Nation': i['Nation'],
                    'Year': i['Year'],
                    'Population': i['Population']
                }])
        return output_df
    else:
        return 'Error'


print(func(2022))

'''
2.Напишите программу, которая загружает данные из нескольких CSV-файлов, объединяет их,
сортирует по нескольким столбцам и сохраняет результат в новый файл.
'''

import pandas as pd
file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')
file3 = pd.read_csv('file3.csv')
result = pd.concat([file1, file2, file3], axis=1).sort_values(by=['Age', 'Total number'])
result.to_csv('file4.csv')