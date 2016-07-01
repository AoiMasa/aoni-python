__author__ = "Gianni"

def get_map_from_file(fileName):
    map = []

    with open(fileName) as file:
        for line in file:
            line = line.replace("\n","")
            map.append(line.split(","))
    file.close()

    return map
