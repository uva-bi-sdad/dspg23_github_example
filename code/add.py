import argparse
import pandas as pd
import logging

# import traceback


def main(a, b):
    return a + b


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Given two values, print the sum")
    parser.add_argument(
        "-a",
        type=float,
        help="The first floating point value",
        required=True,
    )
    parser.add_argument(
        "-b",
        type=float,
        help="The second floating point value",
        required=True,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Show debugging outputs",
        action=argparse.BooleanOptionalAction,
    )

    args = parser.parse_args()
    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG

    logging.basicConfig(format="%(levelname)s: %(message)s", level=log_level)
    sum = main(args.a, args.b)
    print(sum)
