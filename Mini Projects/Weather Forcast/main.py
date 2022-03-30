# # with open ("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #         print(temperature)
#
import pandas

data = pandas.read_csv("weather_data.csv")
# # print(data)
#
# data_dict = data.to_dict()
# print(data_dict)
#
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # average = sum(temp_list/len(temp_list))
# # print(average)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # Get data in column
#
# print(data["condition"])
# print(data.condition)


# Get data in the row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_in_F = (monday_temp * 9/5 + 32)
# print(monday_temp_in_F)



# Create Data Frame

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")