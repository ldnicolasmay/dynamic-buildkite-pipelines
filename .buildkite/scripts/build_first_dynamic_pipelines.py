from typing import Any

import yaml


# from utils.utils import format_dict_strs


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
                for k, v in thing.items()}
        case _:
            return thing


# plugins_dict = {
#    "plugins": [
#        {
#            "docker#v5.6.0": {
#                "image": "python:3.10.11-slim-bullseye",
#                "shell": ["/bin/bash", "-c"]
#            }
#        }
#    ]
# }

step_template = {
    "label": ":python: i={_I_NUM_}",
    "key": "i_{_I_NUM_}",
    # "plugins": plugins_dict,
    "commands": [
        # "python3 -m venv .venv",
        # "source .venv/bin/activate",
        # "python3 -m pip install --upgrade pip",
        # "python3 -m pip install -r requirements_1.txt",
        "echo {_I_NUM_}",
        "python3 -m venv .venv",
        "source .venv/bin/activate",
        "python3 -m pip install --upgrade pip",
        "python3 -m pip install -r requirements_1.txt",
        "python3 .buildkite/scripts/build_second_dynamic_pipelines.py {_I_NUM_}",
        "buildkite-agent pipeline upload .buildkite/pipeline.second_dynamic_pipelines.yml",
    ]
}


def main() -> None:
    print("===== build_first_dynamic_pipelines.py =====")

    num_pipelines = 3
    pipeline_dict = {"steps": []}
    for i in range(num_pipelines):
        step_i = format_dict_strs(step_template, _I_NUM_=i)
        pipeline_dict["steps"].append(step_i)
        if i < num_pipelines - 1:
            pipeline_dict["steps"].append("wait")

    with open(".buildkite/pipeline.first_dynamic_pipelines.yml", "w+") as pipeline_file:
        yaml.safe_dump(pipeline_dict, pipeline_file)

    print("===== build_first_dynamic_pipelines.py =====")


if __name__ == "__main__":
    main()
