import json


def load_json_from_URL(url: str) -> dict:
    with open(url, "r") as file:
        return json.load(file)


def write_to_json(content, output_path: str):
    with open(output_path, "w") as file:
        json.dump(content, file, indent=4)
