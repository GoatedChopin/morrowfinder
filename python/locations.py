from math import sqrt, atan2, pi
from heapq import heappush, heappop


def read_locations(path="../data/mwlocations.txt"):
    locations = []
    with open(path) as file:
        for line in file:
            locations.append(eval(line))
    return locations


def get_coord(row):
    return (row[5], row[6])


def get_name(row):
    return row[9]


def euclidean(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return sqrt(abs(x1-x2)**2+abs(y1-y2)**2)


def closest_location(location, locations):
    best = float("inf")
    closest_location = None
    location_coord = get_coord(location)
    for l in locations:
        if location != l:
            if (distance := euclidean(location_coord, get_coord(l))) < best:
                best = distance
                closest_location = l
    return closest_location


def connect_all_locations(locations):
    location_pairs = set()
    location_set = set()
    distances = []
    for i1, l1 in enumerate(locations):
        for i2, l2 in enumerate(locations):
            l1_coord, l2_coord = get_coord(l1), get_coord(l2)
            if l1_coord != l2_coord:
                if (l1_coord, l2_coord) not in location_pairs and (l2_coord, l1_coord) not in location_pairs:
                    location_pairs.add((l1_coord, l2_coord))
                    heappush(distances, (euclidean(l1_coord, l2_coord), l1, l2))
    
    closest_connections = []
    while len(location_set) < len(locations):
        print(len(location_set) - len(locations))
        if not distances:
            break
        distance, l1, l2 = heappop(distances)
        if l1 not in location_set or l2 not in location_set:
            closest_connections.append((distance, l1, l2))
            location_set.add(l1)
            location_set.add(l2)    
    return closest_connections

    
def cardinal_direction(origin, destination):
    x1, y1 = origin
    x2, y2 = destination
    compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]

    degrees = atan2(x2-x1, y2-y1)/pi*180
    if degrees < 0:
        degrees += 360
    
    cardinal = round(degrees / 45)
    return "Walk {}".format(compass_brackets[cardinal])


if __name__ == "__main__":

    locations = read_locations()
    closest_connections = connect_all_locations(locations)
    closest_connections = [(_, l1, l2) for (_, l1, l2) in closest_connections if get_name(l1) != get_name(l2)]
    with open("walking.csv", "w") as file:
        for distance, l1, l2 in closest_connections:
            n1, n2 = get_name(l1).replace(",", ":"), get_name(l2).replace(",", ":")
            file.write("{}, {}, {}, {}\n".format(n1, n2, distance, cardinal_direction(get_coord(l1), get_coord(l2))))
            file.write("{}, {}, {}, {}\n".format(n2, n1, distance, cardinal_direction(get_coord(l2), get_coord(l1))))

            # print("{} to {} is {}".format(get_name(l1), get_name(l2), cardinal_direction(get_coord(l1), get_coord(l2))))
