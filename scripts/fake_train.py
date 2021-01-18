with open("summary.json") as f_in:
    with open("pipelines/p0/summary.json", "w") as f_out:
        f_out.write(f_in.read())

with open("plots.csv") as f_in:
    with open("pipelines/p0/plots.csv", "w") as f_out:
        f_out.write(f_in.read())
