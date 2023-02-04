from collections import defaultdict, deque


def get_places(path="places"):
    with open(path) as file:
        places = file.readline().replace("\n", "")
    return eval(places)


def load_data(path="adjacency.csv"):
    global places
    adjacencies = []   # (origin, destination, distance, travel_method)
    guild_guides = []
    with open(path, "r") as file:
        while (line := file.readline().replace("\n", "")) != "":
            if line.endswith(":"):
                title = line[:-1]
            else:
                line = line.split(",")
                match title:
                    case "Ship":
                        origin = line[0]
                        captain = line[1]
                        ship = line[2]
                        for i in range(3, len(line)-1, 2):
                            adjacencies.append((origin, line[i], int(line[i+1]), title))
                    case "Silt Strider":
                        origin = line[0]
                        owner = line[1]
                        for i in range(2, len(line)-1, 2):
                            adjacencies.append((origin, line[i], int(line[i+1]), title))
                    case "Ferry":
                        origin = line[0]
                        ferryman = line[1]
                        for i in range(2, len(line)):
                            adjacencies.append((origin, line[i], 1, title))
                    case "Mage's Guild":
                        origin = line[0]
                        guild_guide = line[1]
                        guild_guides.append((origin, guild_guide))
                    case "Walking":
                        origin, destination, distance, direction = [s.strip() for s in line]
                        distance = round(float(distance))
                        adjacencies.append((origin, destination, distance, direction))
    
    for guild_guide_1 in guild_guides:
        for guild_guide_2 in guild_guides:
            if guild_guide_1 != guild_guide_2:
                origin, guide = guild_guide_1
                destination, _ = guild_guide_2
                adjacencies.append((origin, destination, 0, "Mage's Guild: {}".format(guide)))

    return adjacencies


def build_adjacency_map(data):
    origin_map = defaultdict(list)
    for origin, destination, distance, method in data:
        origin_map[origin].append((distance, destination, method))
    return origin_map


def bfs_path(origin, destination, adjacencies):

    queue = deque()
    queue.appendleft([0, (origin, "Origin")])

    visited = set()
    visited.add(origin)

    def bfs_step():
        current = queue.pop()
        for distance, new_destination, method in adjacencies[current[-1][0]]:
            if new_destination not in visited:
                visited.add(new_destination)
                new_path = current[:]
                new_path[0] += distance
                new_path.append((new_destination, method))
                queue.appendleft(new_path)
                if destination == new_destination:
                    return new_path
    
    while len(queue) > 0:
        path = bfs_step()
        if path is not None:
            return path


def all_reachable_locations(origin, adjacency):
    visited=set()
    visited.add(origin)
    queue = deque()
    queue.appendleft(origin)
    def bfs():
        current = queue.pop()
        for distance, destination, method in adjacency[current]:
            if destination not in visited:
                visited.add(destination)
                queue.appendleft(destination)
    
    while queue:
        bfs()

    return visited


def pretty_format_path(path):
    out = "Start at {}\n".format(path[1][0])
    for i in range(2, len(path)):
        out = out + "Go to {} via {}\n".format(path[i][0], path[i][1])
    out = out + "Arrived\n"
    return out


if __name__ == "__main__":
    data = load_data()
    origin_map = build_adjacency_map(data)
    # balmora_to_vos = bfs_path("Balmora", "Anudnabia (sealed)", origin_map)
    # print(pretty_format_path(balmora_to_vos))
    # breakpoint()
    print(all_reachable_locations("Balmora", origin_map))
    print(all_reachable_locations("Anudnabia (sealed)", origin_map))