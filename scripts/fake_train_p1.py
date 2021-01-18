import json

with open("summary.json") as f_in:
    with open("pipelines/p1/summary.json", "w") as f_out:
        data = json.load(f_in)
        print(data)
        data[
            "link"
        ] = "https://github.com/Extrality/extrality-production-ml/pulls?q=is%3Apr+is%3Aclosed"
        data["toto"] = "test"
        data["yolo"] = 3
        json.dump(data, f_out)

with open("plots.csv") as f_in:
    with open("pipelines/p1/plots.csv", "w") as f_out:
        f_out.write(f_in.read())
