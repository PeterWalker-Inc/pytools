
# py 2optional_arguments.py --magic 16 --magic-without-type
# py 2optional_arguments.py --echo add --magic 16 --magic-without-type
# py 2optional_arguments.py --echo add --magic-without-type 


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--echo", help="echo the string!")
parser.add_argument("--magic", help="display a square of a given number", type=int)
parser.add_argument("--magic-without-type", help="display a square of a given number", action="store_true")
args = parser.parse_args()
print(args.echo)

if args.magic:
    print(args.magic**2) 

print(args)