import argparse
import yaml

from utils.utils import format_dict_strs


step_template = {
    "label": ":python: i={_I_NUM_} j={_J_NUM_}",
    "key": "i_{_I_NUM_}_j_{_J_NUM_}",
    "commands": [
        "echo i={_I_NUM_} j={_J_NUM_}",
        "python3 -m venv .venv",
        "source .venv/bin/activate",
        "python3 -m pip install --upgrade pip",
        "python3 -m pip install -r requirements_2.txt",
        "python3 do_something/main.py {_I_NUM_} {_J_NUM_}",
    ]
}


def main(i: int) -> None:
    num_pipelines = 3
    pipeline_dict = {"steps": []}
    for j in range(num_pipelines):
        step_j = format_dict_strs(step_template, _I_NUM_=i, _J_NUM_=j)
        pipeline_dict["steps"].append("wait")
        pipeline_dict["steps"].append(step_j)

        with open(f".buildkite/pipeline.i_level_{i}_j_level.yml", "w+") as pipeline_file:
            yaml.safe_dump(pipeline_dict, pipeline_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("i", type=int)
    args = parser.parse_args()

    main(args.i)
