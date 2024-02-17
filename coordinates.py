import csv

def collect_coordinates_bus_shelter(csv_file_path):
    coordinates = []

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            geometry = eval(row['geometry'])
            if 'coordinates' in geometry:
                for coordinate in geometry['coordinates']:
                    if len(coordinate) == 2:
                        coordinates.append([coordinate[1], coordinate[0]])

    return coordinates

