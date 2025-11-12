import argparse
import main_battle_loop as mbl
import main_genetic_loop as mgl
import main_deck_fetch as mdf


def filter_function(type: str, weight: dict = None, generations: int = None, plot: list = []):
    if type == "GA":
        mgl.main_genetic_loop(weight, generations, plot)
    elif type == "BL":
        mbl.main_battle_loop(weight)
    elif type.capitalize() == "Fetch":
        mdf.main_deck_fetch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weight", type=dict)
    parser.add_argument("--type", type=str)
    parser.add_argument("--gen", type=int)
    parser.add_argument("--plot", type=str)
    args = parser.parse_args()
    
    if not args.plot:
        args.plot = None
    if not args.type:
        args.type = "GA"
    if not args.gen:
        args.gen = 25
        
    if args.plot:
        args.plot = [int(v) for v in args.plot.split(",")]

    filter_function(args.type, args.weight, args.gen, args.plot)
