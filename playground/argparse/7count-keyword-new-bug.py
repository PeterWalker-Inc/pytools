import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="square the number", type=int)
parser.add_argument("-v", "--verbose", help="increase the output verbosity", action="count")
args = parser.parse_args()
answer = args.square ** 2

if args.verbose == 2:
    print(f"the square of {args.square} is {answer}")
elif args.verbose == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)