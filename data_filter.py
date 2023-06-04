import csv

list_of_sets = []  # Creates a blank list for sets
important_ones = [2, 3, 4, 5, 6, 7, 8, 9, 10, 15]  # Highly valued columns
bad_info_options = ["", "Not Recorded", "N/A"]  # Options that are the equivalent of an empty field

with open('BKB_WaterQualityData_2020084.csv') as bkb_water:
    water_csv = csv.reader(bkb_water, delimiter=',')

    header_row = next(water_csv)  # Gets the first row of water_csv and assigns it to header_row
    num_col = len(header_row)  # Gets the number of columns in the csv file and assigns it to num_col
    bkb_water.seek(0)  # Resets the index of the csv.reader

    for col in range(num_col):  # Appends a set for each column
        list_of_sets.append(set())

    # Goes through each row in the csv file
    for row in water_csv:
        important_count = 0  # Creates a counter for how many important fields the row has filled

        # Goes through each index in the row
        for e in range(len(row)):
            # If a field has bad info, adds the entire row to the corresponding set
            if row[e] in bad_info_options:
                list_of_sets[e].add(tuple(row))  # Important that row is a tuple

            # If the field is populated adequately increases the important_count for that row
            if (e in important_ones) and (row[e] not in bad_info_options):
                important_count += 1

        #print(row, important_count)  # Prints the whole row and the important_count of that row

    with open('BKB_WaterCleaned.csv', mode='w') as bkb_cleaned:
        cleaned_csv = csv.writer(bkb_cleaned, delimiter=',')

# Prints the length of each set in 'list_of_sets'
# Note that the length of each set represents the number of rows that do NOT have good info in that field
for num in range(len(list_of_sets)):
    print(header_row[num], len((list_of_sets[num])))
