from collections import defaultdict


def sum_nb_use(streets):
    pass


def weights(intersection_in, streets):
    memo = {}
    def sum_intersection_use(intersection, inter_number):
        intersection = set(intersection)
        if inter_number not in memo:
            memo[inter_number] = sum(
                street['nb_use'] for street in streets.values() if street['name'] in intersection
            )
        return memo[inter_number]
    return {
        i: {
            name: streets[name]['nb_use'] / max(sum_intersection_use(names, i), 1)
            for name in names
        }
        for i, names in enumerate(intersection_in.values())
    }


def parse_file(file_name):
    with open(file_name, 'r') as my_file:
        lines = my_file.read().splitlines()
        first_line = lines[0].split(' ')
        duration = first_line[0]
        nb_intersections = int(first_line[1])
        nb_streets = int(first_line[2])
        nb_car = int(first_line[3])
        intersections = defaultdict(list)
        intersections_in = defaultdict(list)
        intersections_out = defaultdict(list)
        streets = {}
        cars = {}
        for line in lines[1:nb_streets + 1]:
            words = line.split(' ')
            streets[words[2]] = {
                'L': int(words[3]),
                'start': int(words[0]),
                'end': int(words[1]),
                'name': words[2],
                'nb_use': 0
            }
            intersections[words[0]].append(words[2])
            intersections[words[1]].append(words[2])
            intersections_in[words[1]].append(words[2])
            intersections_out[words[0]].append(words[2])
        for i, line in enumerate(lines[nb_streets + 1:]):
            words = line.split(' ')
            cars[i] = words[1:]
            for street_name in words[1:]:
                streets[street_name]['nb_use'] += 1
        black_list = {street['name'] for _, street in streets.items() if street['nb_use'] == 0}
        return {
            'duration': duration,
            'nb_intersections': nb_intersections,
            'nb_streets': nb_streets,
            'nb_car': nb_car,
            'intersections': intersections,
            'streets': streets,
            'cars': cars,
            'intersections_in': intersections_in,
            'intersections_out': intersections_out,
            'black_list': black_list,
            'weights': weights(intersections_in, streets)
        }
