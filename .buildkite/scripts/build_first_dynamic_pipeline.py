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
            return {k.format(**kwargs) if isinstance(k, str) else k: format_dict_strs(v, **kwargs) for k, v in thing.items()}
        case _:
            return thing


#plugins_dict = {
#    "plugins": [
#        {
#            "docker#v5.6.0": {
#                "image": "python:3.10.11-slim-bullseye",
#                "shell": ["/bin/bash", "-c"]
#            }
#        }
#    ]
#}

step_template = {
    "label": ":python: foo {_NUM_}",
    "key": "foo_{_NUM_}",
    #"plugins": plugins_dict,
    "commands": [
        "python 3 -m venv .venv",
        "source .venv/bin/activate",
        "python3 -m pip install --upgrade pip",
        "python3 -m pip install -r requirements.txt",
        "echo {_NUM_}",
    ]
}


def main() -> None:
    print("===== build_first_dynamic_pipeline.py =====")

    pipeline_dict = {"steps": []}
    for i in range(3):
        step_i = format_dict_strs(step_template, _NUM_=i)
        pipeline_dict["steps"].append(step_i)

    with open(f".buildkite/pipeline.first_dynamic_pipeline.yml", "w+") as pipeline_file:
        yaml.safe_dump(pipeline_dict, pipeline_file)

    print("===== build_first_dynamic_pipeline.py =====")


if __name__ == "__main__":
    main()
