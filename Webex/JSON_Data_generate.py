import openpyxl  # python lib to read and write excel file
import json

# Open the Excel file and read the data
workbook = openpyxl.load_workbook('webex_groups.xlsx')
sheet = workbook.active

# Initialize an empty dictionary to store the grouped data
groups = {}


# Iterate over the rows in the sheet
for row in sheet.iter_rows(min_row=2, values_only=True):
    # Get the group for this user
    group = row[0]

    # If the group is not in the dictionary, add it
    if group not in groups:
        groups[group] = []

    # Add the user data to the appropriate group
    groups[group].append({
        # 'group': row[0],
        'name': row[1],
        'email': row[2]
    })

# reference : https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

# Convert the dictionary of groups to a JSON object
json_data = json.dumps(groups, indent=4)

# Print the JSON data
print(json_data)

with open('data.json', 'w') as json_file:
    # Write the data to the file as JSON
    json.dump(json_data, json_file)
