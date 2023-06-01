import csv

with open('BKB_WaterQualityData_2020084.csv') as BKB_Water:
    water_csv = csv.reader(BKB_Water, delimiter=',')
    with open('BKB_WaterCleaned.csv', mode='w') as BKB_Cleaned:
        cleaned_csv = csv.writer(BKB_Cleaned, delimiter=',')

print("We're up to date!")