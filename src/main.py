import argparse
from data.load_data import load_data


parser = argparse.ArgumentParser(
    prog="ml_practice", epilog="This is a practice program"
)

parser.add_argument("-p", "--path")
args = parser.parse_args()

df = load_data(args.path)
