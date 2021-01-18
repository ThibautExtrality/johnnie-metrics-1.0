import json

with open("summary.json") as f_in:
    with open("pipelines/p2/summary.json", "w") as f_out:
        data = json.load(f_in)
        print(data)
        data[
            "link"
        ] = "https://github.com/Extrality/extrality-production-ml/pulls?q=is%3Apr+is%3Aclosed"
        data["toto"] = "test"
        data["yolo"] = 10
        json.dump(data, f_out)

with open("plots.csv") as f_in:
    with open("pipelines/p2/plots.csv", "w") as f_out:
        f_out.write(f_in.read())

with open("plots.csv") as f_in:
    with open("pipelines/p2/plots_2.csv", "w") as f_out:
        f_out.write(f_in.read())

with open("plots.csv") as f_in:
    with open("pipelines/p2/plots_3.csv", "w") as f_out:
        f_out.write(f_in.read())
