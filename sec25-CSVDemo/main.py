# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])  # Getting the temperature values as a series
#
# # data_dict = data.to_dict()  # Converting the data to a dictionary
# # print(data_dict)
#
# # temp_list = data["temp"].to_list()  # Converting the temperature series to list
# # print(temp_list)
#
# # average_temp = sum(temp_list)/len(temp_list)  # easier way for average of a series is using "series.mean()" method
# # print(average_temp)
#
# # print(max(data["temp"]))
#
# print(data[data.temp == max(data.temp)])  # data.temp is same as data["temp"]



import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
