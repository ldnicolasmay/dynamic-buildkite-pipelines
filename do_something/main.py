import argparse

from art import text2art


def main(i: int, j: int) -> None:
    text = f"i={i}\nj={j}"
    print(text2art(text, font="block"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("i", type=int)
    parser.add_argument("j", type=int)
    args = parser.parse_args()

    main(i=args.i, j=args.j)
