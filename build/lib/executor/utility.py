import json
import os

json_file = os.path.join(os.path.dirname(__file__), 'judge', 'test-cases.json')
def write_json(test_cases):
    """ Writes the test cases to a JSON file """
    with open(json_file, 'w') as f:
        json.dump(test_cases, f, indent=2)


def load_json():
    """ Retrieves the test cases from json file, returns a dictionary"""
    test_cases = dict()

    with open(json_file, 'r') as f:
        test_cases = json.load(f)

    return test_cases