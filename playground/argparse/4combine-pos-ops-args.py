

# py 4combine-pos-ops-args.py 24 -v2
# py 4combine-pos-ops-args.py 24 -v1
# py 4combine-pos-ops-args.py 24

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="sqauare the number", type=int)
parser.add_argument("-v", "--verbose", help="increase output verbosity", type=int)

args = parser.parse_args()
answer = args.square**2

#bug in -v 3 or --verbose 3
# py 4combine-pos-ops-args.py 4 -v3
# 16
if args.verbose == 2:
    print(f"the square of {args.square} is {answer}")
elif args.verbose == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)