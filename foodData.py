import tkinter as tk
from tkinter import filedialog
import csv

# Define the lists to store data
restaurants = []
items = []
types = []
serving_sizes = []
calories = []
fats = []
sodiums = []
sugars = []

list_data = []
uniqueRestaurants = set()

# Read the CSV file and store the data into lists

def choose_file():
    root = tk.Tk()
    root.withdraw()  #Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    #print(file_path)
    return file_path

def read_csv(file_name):
    with open(file_name, newline='', mode='r', encoding='utf=8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            restaurants.append(row['restaurant'])
            items.append(row['item'])
            types.append(row['type'])
            serving_sizes.append(float(row['serving_size']))
            calories.append(int(row['calories']))
            fats.append(float(row['fat']))
            sodiums.append(float(row['sodium']))
            sugars.append(float(row['sugars']))

            list_data.append(row)
            uniqueRestaurants.add(row['restaurant'])
      #  print(uniqueRestaurants)
            
"""
def allItemsList():
    for i in range(len(items)):
        itemsList = []
        itemsList.append(restaurants[i])
        itemsList.append(items[i])
        itemsList.append(types[i])
        itemsList.append(serving_sizes[i])
        itemsList.append(calories[i])
        itemsList.append(fats[i])
        itemsList.append(sodiums[i])
        itemsList.append(sugars[i])
"""
def findAvg(list_of_values):
    avg = sum(list_of_values)/len(list_of_values)
    return avg

def maxVal(list_of_values):
    maxValue = max(list_of_values)
    return maxValue

def minVal(list_of_values):
    minValue = min(list_of_values)
    return minValue

def countItems(list_of_values):
    count = len(list_of_values)
    return count

def sugarsPerRestaurantReport():
    report = {}
    for restaurant in uniqueRestaurants:
        totalSugars = 0
        for i in range(len(restaurants)):
            if restaurants[i] == restaurant:
                totalSugars += sugars[i]
    report[restaurant] = totalSugars
    print(report)
    return report

def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    #read_file(file_path)
    read_csv(file_path)
    print("Average calories is", findAvg(calories))
    print("Min calories is", minVal(calories))
    print("Max sodium is ", maxVal(sodiums))
    print("Count of items is", countItems(items))
    
    print("List of restaurants and their total sugars: ")
    report = sugarsPerRestaurantReport()
    for result in report:
        print(result, ": ", report[result])
    print("\n")

if __name__ == '__main__':
    main()

