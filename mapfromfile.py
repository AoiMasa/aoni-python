__author__ = "Gianni"

import json

def get_map_from_csv_file(fileName):
    map = []

    with open(fileName) as file:
        for line in file:
            line = line.replace("\n","")
            map.append([int(i) for i in line.split(",")])
    return map

def get_map_from_json_file(filename): #
    """Take a json file exported from Tiled and transform it into a 2d list.

    /!\ Not functional. Can't get the tile ID from Tiled json export

    :return: 2d list of int
    """
    map = []

    with open(filename) as file:
        data_json = json.load(file)
        map_data = data_json['layers'][0]['data']
        map_height = data_json['height']
        map_width = data_json['width']

        for height in range(0, map_height - 1):
            line = []
            for width in range(0, map_width - 1):
                line.append(map_data[height * width])
            map.append(line)

    return map