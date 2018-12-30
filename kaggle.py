#!/usr/bin/env python3

import json

predict_file = "predictions.txt"
test_file = "test.json"
output_file = "kaggle.csv"

with open(predict_file) as f:
    labels = f.readlines()
labels = [x.strip() for x in labels]

with open(test_file, 'r') as f:
    json_data = f.read()
obj = json.loads(json_data)

with open(output_file, "w") as out:
    print("id,cuisine", file=out)

    i = 0
    for recipe in obj:
        idx = recipe["id"]
        ingredient = labels[i]
        print(str(idx) + "," + ingredient, file=out)
        i += 1
