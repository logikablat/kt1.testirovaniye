import json
import csv


with open('SuperHero.json', 'r') as json_file:
    data = json.load(json_file)


with open('SuperHero.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)


    writer.writerow(['name', 'age', 'secretIdentity', 'powers'])


    for member in data['members']:
        writer.writerow([member['name'], member['age'], member['secretIdentity'], ', '.join(member['powers'])])

print("JSON данные успешно преобразованы в CSV.")
