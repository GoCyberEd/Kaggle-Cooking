#!/usr/bin/env python3

# Enable python2 compatability
from __future__ import print_function

import json

def main():
    # Define input/output file names
    train_file = "train.json"
    test_file = "test.json"
    train_file_out = "train.csv"
    test_file_out = "test.csv"
    train_file_out_labels = "train-labels.txt"
    json_data = None
    with open(train_file, 'r') as f:
        json_data = f.read()
    train_obj = json.loads(json_data)

    # Empty arrays to hold information
    labels_train = []
    labels_test = []
    # ingredients is defined as a set to prevent duplicates
    ingredients = set()

    # Generate corresponding labels and simultaneously make 
    # exhaustive set of all posible cuisines (labels)
    with open(train_file_out_labels, 'w') as f:
        for recipe in train_obj:
            label = recipe["cuisine"]
            print(label, file=f)
            labels_train.append(label)
            for ingredient in recipe["ingredients"]:
                ingredients.add(ingredient)

    with open(test_file, 'r') as f:
        json_data = f.read()
    test_obj = json.loads(json_data)

    # The test file may introduce ingredients not included in training set
    # This ensures they're included
    for recipe in test_obj:
        for ingredient in recipe["ingredients"]:
            ingredients.add(ingredient)

    # Transform set to list to ensure iteration order is constant
    ingredients_list = list(ingredients)

    # Generate the CSV files
    generate_csv_for_each_recipe(ingredients_list, train_obj, train_file_out)
    generate_csv_for_each_recipe(ingredients_list, test_obj, test_file_out)

def generate_csv_for_each_recipe(ingredients_list, json_obj, output_file):
    """
    Creates an output csv file with each ingredient being a column
    and each recipe a row. 1 will represent the recipe contains the 
    given ingredient if the recipe includes that incredient, else 0

    ingredients_list -- the full list of ingredients (without duplicates)
    json_obj -- the json object with recipes returned by json.loads
    output_file -- the name of the generated CSV file
    """
    # Loop thru each recipe
    with open(output_file, 'w') as f:
        for recipe in json_obj:
            rl = set()
            first = True
            s = ""
            for ingredient in recipe["ingredients"]:
                rl.add(ingredient)
            # This builds the csv row of ingredients for current recipe
            # Add 1 for ingredient if included in recipe; else 0
            for j in ingredients_list:
                # Don't prepend "," for first item
                if first != True:
                    s += ","  
                else:
                    first = False

                # Add 1 or 0 as explained above
                if j not in rl:
                    s += "0"
                else:
                    s += "1"
            print(s, file=f)

if __name__ == "__main__":
    main()
