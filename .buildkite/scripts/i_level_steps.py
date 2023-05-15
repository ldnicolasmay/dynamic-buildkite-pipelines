import yaml

from utils.utils import format_dict_strs


step_template = {
    "label": ":python: i={_I_NUM_}",
    "key": "i_{_I_NUM_}",
    "commands": [
        "echo i={_I_NUM_}",
        "python3 -m venv .venv",
        "source .venv/bin/activate",
        "python3 -m pip install --upgrade pip",
        "python3 -m pip install -r requirements_1.txt",
        "python3 .buildkite/scripts/j_level_steps.py {_I_NUM_}",
        "buildkite-agent pipeline upload .buildkite/pipeline.i_{_I_NUM_}_j_level.yml",
    ]
}


def main() -> None:
    num_pipelines = 3
    pipeline_dict = {"steps": []}

    for i in range(num_pipelines):
        step_i = format_dict_strs(step_template, _I_NUM_=i)
        pipeline_dict["steps"].append("wait")
        pipeline_dict["steps"].append(step_i)

    with open(".buildkite/pipeline.i_level.yml", "w") as pipeline_file:
        yaml.safe_dump(pipeline_dict, pipeline_file)


if __name__ == "__main__":
    main()
