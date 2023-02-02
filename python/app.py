import json
from flask import Flask
from pathfinding import load_data, bfs_path, get_places, build_adjacency_map


app = Flask(__name__)
places = get_places()
adjacencies = build_adjacency_map(load_data())
print(adjacencies)

@app.route("/path/<origin>/<destination>")
def pathfind(origin, destination):
    error = None
    if origin not in places or destination not in places:
        error = "Either your origin or destination were incorrectly spelled. The following places are acceptable: {}".format(places)
        return json.dump({"status": 400, "body": error})
    
    print(origin, destination)
    path = bfs_path(origin, destination, adjacencies)
    if path:
        return json.dumps({"status": 200, "body": path})
    else:
        return json.dumps({"status": 200, "body": "No such path is available at this time."})