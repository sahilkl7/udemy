# # with open('weather_data.csv') as w:
# #     data = w.readlines()
# #     print(data)
#
# # import csv
#
# # with open('weather_data.csv') as w:
# #     data = csv.reader(w)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int((row[1]))
# #     print(temperatures)
#
# import pandas
# data = pandas.read_csv('weather_data.csv')
# #print(data['temp'])
#
# # temp_list= data['temp'].to_list()
# # print(temp_list)
# #
# # len_list = len(temp_list)
# #
# # # avg = round((sum(temp_list)/len_list),2)
# # # print(avg)
# #
# # print(data['temp'].mean())
# # print(data['temp'].max())
# #
# # # Get a column in data
# # print(data['condition'])
# # print(data.condition)
#
# # Get a row in Data
#
# #print(data[data.day == 'Monday'])
# # return true or false print(data.day == 'Monday')
#
# # highest_temp = (data['temp'].max())
# #
# # #print(data[data.temp == highest_temp ])
# #
# # monday = data[data.day == 'Monday']
# # monday_temp = (monday.temp[0] * 9/5) +32
# #
# # print(monday_temp)
#
# # Create a data Frame from SCRATCH
#
# data_dict = {
#     "student" : ["Amy",'James','Angela'],
#     'scores' : [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# #data.to_csv('new_data.csv')

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])
# print(grey_squirrel)
# print(red_squirrel)
# print(black_squirrel)

dict_s = {
    'Primary Fur Color': ['Gray','Cinnamon','Black'],
    'rows': [grey_squirrel,red_squirrel,black_squirrel]
}

df = pandas.DataFrame(dict_s)
#df.to_csv('squirrel_count.csv')

data1 = pandas.read_csv('nato_phonetic_alphabet.csv')


phonetic_dict = {row.letter:row.code for (index,row) in data1.iterrows()}
# print(phonetic_dict)

word = input("Enter a word : ").upper()
l1 = [phonetic_dict[letter] for letter in word ]
print(l1)






















