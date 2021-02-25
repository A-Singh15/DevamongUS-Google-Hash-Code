# Singh
# saber

from hash_code_parser import *
from pprint import pprint


def solve(input_file_name, dry_run=False):
    problem = parse_file(input_file_name)
    output = create_streets(
        problem["intersections_in"],
        int(problem["duration"]),
        problem["streets"],
        problem["black_list"],
        problem["weights"],
        problem["nb_car"],
    )
    if not dry_run:
        with open("output_" + input_file_name, "w") as output_file:
            output_file.write(output)
    else:
        print(output)


def create_streets(intersections, time, streets_dict, blacklist, weights, nb_car):
    max_time = min(10, time)
    res = ""
    inter_count = 0
    for inter in intersections.items():
        if len(inter[1]) == 1:
            res += inter[0] + "\n"
            res += "1\n" + inter[1][0] + " " + str(time) + "\n"
            inter_count += 1
        else:
            streets = sorted_streets(inter[1], streets_dict)
            num_streets = len(inter[1])
            streets_time = [
                i
                + " "
                + str(weights[int(inter[0])][i] * (time / nb_car))
                for acc, i in enumerate(streets)
                if round(max_time - max_time * (acc / num_streets)) != 0
                and i not in blacklist
            ]
            if len(streets_time) > 0:
                res += inter[0] + "\n"
                res += str(len(streets_time)) + "\n" + "\n".join(streets_time) + "\n"
                inter_count += 1
    res = str(inter_count) + "\n" + res
    return res


def sorted_streets(streets, streets_dict):
    return sorted(
        streets,
        key=lambda s: streets_dict[s]["nb_use"] / streets_dict[s]["L"],
        reverse=True,
    )


def main():
    for l in "abcdef":
        print(l)
        solve(l + ".txt")


def test_():
    solve('b.txt', dry_run=True)


if __name__ == "__main__":
    main()
