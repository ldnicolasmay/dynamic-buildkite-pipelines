import argparse

from art import *


def main(i: int, j: int) -> None:
    text = f"""
    i={i}
    j={j}
    """
    print(text2art(text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("i", type=int)
    parser.add_argument("j", type=int)
    args = parser.parse_args()

    main(i=args.i, j=args.j)
