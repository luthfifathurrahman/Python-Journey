# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
import pandas as pd
from numpy.ma.extras import average

data = pd.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(average(temp_list))
print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp
fahrenheit = (monday_temp * 9/5) + 32
print(fahrenheit)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "james"],
    "scores": [10, 20]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)