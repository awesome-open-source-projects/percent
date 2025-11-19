from . import percent
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Calculate the percentage of arg1 with respect to arg2.')
    parser.add_argument('arg1', type=float, nargs='?', help='The part (numerator) to calculate the percentage from')
    parser.add_argument('arg2', type=float, nargs='?', help='The whole (denominator) to calculate the percentage of')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    result = percent(args.arg1, args.arg2)

    print(f'The percentage of {args.arg1} out of {args.arg2} is {result:.2f}%.')

if __name__ == "__main__":
    main()
