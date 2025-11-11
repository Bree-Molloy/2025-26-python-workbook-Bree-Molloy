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

def sugarsPerRestaurant(list_of_values, restaurant_name):
    sugarsPer = []
    for i in range(len(restaurants)):
        if restaurants[i] == restaurant_name:
            sugarsPer.append(list_of_values[i])
    return sugarsPer

def main():
    # Read and load data from a CSV file
    file_path = choose_file()
    #read_file(file_path)
    read_csv(file_path)
    print("Average sugars for mcdonalds ", findAvg(sugarsPerRestaurant(sugars, "McDonald's")))
    print("Average calories is", findAvg(calories))
    print("Min calories is", minVal(calories))
    print("Max sodium is ", maxVal(sodiums))
    print("Count of items is", countItems(items))

if __name__ == '__main__':
    main()

