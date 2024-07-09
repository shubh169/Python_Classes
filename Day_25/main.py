# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temp=[]
#     for row in data:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
# print(temp)

import pandas
data = pandas.read_csv('weather_data.csv')
# avg=round(data["temp"].mean(),2)
# print(avg)
# print(data["temp"].max())
# temp=data['temp'].to_list()

# Get data in column
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day=="Monday"])
print(data[data.temp==data.temp.max()])