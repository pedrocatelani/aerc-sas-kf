import argparse
import main_battle_loop as mbl
import main_genetic_loop as mgl

def filter_function(type: str, weight: dict = None):
    if type == "GA":
        mgl.main_genetic_loop(weight)
    elif type == "BL":
        mbl.main_battle_loop(weight)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weight", type=dict)
    parser.add_argument("--type", type=str)
    args = parser.parse_args()
    
    if not args.type:
        args.type = "GA"
        
    filter_function(args.type, args.weight)
    