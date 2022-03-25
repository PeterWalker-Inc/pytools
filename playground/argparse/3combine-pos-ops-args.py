
# py 3combine-pos-ops-args.py 50 -v
# py 3combine-pos-ops-args.py -v 50

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="sqauare the number", type=int)
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print(f"the square of {args.square} is {answer}")
else:
    print(answer)