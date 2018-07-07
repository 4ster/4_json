import json
import argparse


def load_data(filepath):
    with open(filepath) as json_file:
        json_data = json.load(json_file)
    return json_data


def pretty_print_json(json_data):
    json_text = json.dumps(json_data, sort_keys=True,
                           indent=4, ensure_ascii=False)

    print(json_text)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Print json file in human readble format.')
    parser.add_argument('filepath', metavar='f', type=str,
                        help='path to json file')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = create_parser()
    json_data = load_data(args.filepath)
    pretty_print_json(json_data)
