import argparse
from typing import Any

import yaml


def format_dict_strs(thing: Any, **kwargs) -> Any:
    match thing:
        case str():
            return thing.format(**kwargs)
        case list():
            return [format_dict_strs(t, **kwargs) for t in thing]
        case dict():
            return {
                k.format(**kwargs)
                if isinstance(k, str) else k: format_dict_strs(v, **kwargs)
                for k, v in thing.items()
            }
        case _:
            return thing

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
    print("===== build_second_dynamic_pipelines.py =====")

    num_pipelines = 3
    pipeline_dict = {"steps": []}
    for j in range(num_pipelines):
        step_j = format_dict_strs(step_template, _I_NUM_=i, _J_NUM_=j)
        pipeline_dict["steps"].append(step_j)
        # if j < num_pipelines - 1:
        #     pipeline_dict["steps"].append("wait")

    with open(f".buildkite/pipeline.second_dynamic_pipelines.yml", "w+") as pipeline_file:
        yaml.safe_dump(pipeline_dict, pipeline_file)

    print("===== build_second_dynamic_pipelines.py =====")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("i", type=int)
    args = parser.parse_args()

    main(args.i)
