from sys import exit
from json import load, dump

JSON_FILE = "test_payload.json"


def _remove(data, element):
    if isinstance(data, dict):
        return {key: _remove(val, element) for key, val in data.items() if key != element}
    elif isinstance(data, list):
        return [_remove(val, element) for val in data]
    else:
        return data


def remove_element(element):
    with open(JSON_FILE, 'r') as _fh:
        data = load(_fh)
        if not data:
            exit("Json file is empty")

    data = _remove(data, element)
    with open(JSON_FILE, 'w') as _fh:
        dump(data, _fh, indent=2)



if __name__ == '__main__':
    remove_element('inParams')