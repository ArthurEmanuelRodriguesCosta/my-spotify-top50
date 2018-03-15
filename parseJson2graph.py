import json

with open('arthur-top-50.json') as data_file:
    data = json.load(data_file)

graph = {}

graph["nodes"] = []
graph["edges"] = []

for e in data["items"]:
    node = {
        "id": e["id"],
        "name": e["name"],
        "genres": e["genres"],
        "img": e["images"][0]["url"]
    }

    graph["nodes"].append(node)

for e1 in graph["nodes"]:
    for e2 in graph["nodes"]:
        s1 = set(e1["genres"])
        s2 = set(e2["genres"])
        intersection = s1.intersection(s2)
        if e1["id"] != e2["id"] and len(intersection) > 0:
             edge = {
                "source": e1["id"],
                "target": e2["id"],
                "type": list(intersection)[0]
             }

             graph["edges"].append(edge)

with open("arthur-top-50-graph.json", 'w') as outfile:
    json.dump(graph, outfile)
