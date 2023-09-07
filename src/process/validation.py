from jsonschema import validate

request_schema = {
    "type": "object",
    "properties": {
        "image": {"type": "string"},
    },
}


def request_validate(data: dict[str, str]) -> dict[str, str]:
    validate(data, request_schema)
    return data
