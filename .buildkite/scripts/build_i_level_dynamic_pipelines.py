import yaml

from utils.utils import format_dict_strs


step_template = {
    "label": ":python: i={_I_NUM_}",
    "key": "i_{_I_NUM_}",
    "commands": [
        "echo {_I_NUM_}",
        "python3 -m venv .venv",
        "source .venv/bin/activate",
        "python3 -m pip install --upgrade pip",
        "python3 -m pip install -r requirements_1.txt",
        "python3 .buildkite/scripts/build_j_level_dynamic_pipelines.py {_I_NUM_}",
        "buildkite-agent pipeline upload .buildkite/pipeline.level_j_dynamic_pipelines.yml",
    ]
}


def main() -> None:
    num_pipelines = 3
    pipeline_dict = {"steps": []}
    for i in range(num_pipelines):
        step_i = format_dict_strs(step_template, _I_NUM_=i)
        pipeline_dict["steps"].append(step_i)
        pipeline_dict["steps"].append("wait")

    with open(".buildkite/pipeline.level_i_dynamic_pipelines.yml", "w+") as pipeline_file:
        yaml.safe_dump(pipeline_dict, pipeline_file)


if __name__ == "__main__":
    main()
