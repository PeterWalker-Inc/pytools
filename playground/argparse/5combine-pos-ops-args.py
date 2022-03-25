
# py 5combine-pos-ops-args.py 24 -v3
# py 5combine-pos-ops-args.py 24 -v2
# py 5combine-pos-ops-args.py 24 -v1
# py 5combine-pos-ops-args.py 24 -v0

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="square of the number", type=int)
parser.add_argument("-v", "--verbose", help="increase output verbosity", choices=[0,1,2], type=int)
args = parser.parse_args()
answer = args.square ** 2

if args.verbose == 2:
    print(f"the square of {args.square} is {answer}")
elif args.verbose == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)