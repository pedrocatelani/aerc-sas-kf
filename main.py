import argparse
import main_battle_loop as mbl
import main_genetic_loop as mgl
import main_deck_fetch as mdf


def filter_function(type: str, weight: dict = None, generations: int = None):
    if type == "GA":
        mgl.main_genetic_loop(weight, generations)
    elif type == "BL":
        mbl.main_battle_loop(weight)
    elif type.capitalize() == "Fetch":
        mdf.main_deck_fetch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weight", type=dict)
    parser.add_argument("--type", type=str)
    parser.add_argument("--gen", type=int)
    args = parser.parse_args()

    if not args.type:
        args.type = "GA"
    if not args.gen:
        args.gen = 25

    filter_function(args.type, args.weight, args.gen)
