"""Console script for python_practice_demo."""

import fire


def help() -> None:
    print("python_practice_demo")
    print("=" * len("python_practice_demo"))
    print("This is a demo for learning how to make a python project")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
