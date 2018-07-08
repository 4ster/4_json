import json
import argparse


def load_data(filepath):
    with open(filepath) as json_file:
        try:
            decoded = json.load(json_file)
        except json.JSONDecodeError as e:
            return None
    return decoded


def pretty_print_json(text_to_beautify):
    formatted_json = json.dumps(
        text_to_beautify,
        sort_keys=True,
        indent=4,
        ensure_ascii=False
        )

    print(formatted_json)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Print json file in human readble format.')
    parser.add_argument('filepath', metavar='f', type=str,
                        help='path to json file')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = create_parser()
    try:
        json_data = load_data(args.filepath)
        if json_data is None:
            exit("Error: Invalid json in file {0}".format(args.filepath))
        pretty_print_json(json_data)
    except FileNotFoundError as e:
        exit("Error: File not found '{0}'".format(e.filename))
    
