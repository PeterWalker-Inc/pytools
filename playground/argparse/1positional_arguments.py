import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string!")
parser.add_argument("magic", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.echo)
print(args.magic**2)
print(args)