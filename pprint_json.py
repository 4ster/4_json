import json
import pprint
import argparse
import sys


def load_data(filepath):
    with open(filepath) as f:
        shops_list = json.load(f)
    return shops_list


def pretty_print_json(shops_list):
    shop_json_string = pprint.pformat(shops_list)
    print(shop_json_string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Print json file in human readble format.')
    parser.add_argument('filepath', metavar='f', type=str,
                        help='path to json file')

    args = parser.parse_args()

    shop_list = load_data(args.filepath)
    pretty_print_json(shop_list)
