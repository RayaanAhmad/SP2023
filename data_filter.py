import csv

with open('BKB_WaterQualityData_2020084.csv') as bkb_water:
    water_csv = csv.reader(bkb_water, delimiter=',')
    with open('BKB_WaterCleaned.csv', mode='w') as bkb_cleaned:
        cleaned_csv = csv.writer(bkb_cleaned, delimiter=',')

print("We're not up to date!")
