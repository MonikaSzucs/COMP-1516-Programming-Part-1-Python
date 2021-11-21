"""
Lab 10 by Monika Szucs A00878763
A script containing the main() function
:author: Monika Szucs
:date: November 15, 2021
"""

import sys
import argparse

if __name__ == "__main__":
    # initialize the parser
    parser = argparse.ArgumentParser(
        description="my mathscript"
    )

    # add the parameters positional/optional
    parser.add_argument('-n', '--num1', help="Number 1", type=float)
    parser.add_argument('-i', '--num2', help="Number 2", type=float)
    parser.add_argument('-o', '--operation', help="provide operator", default="+")

    # Parse the arguments
    args = parser.parse_args()
    print(args)
    result =  None
    if args.operation == '+':
        result = args.num1 + args.num2
    if args.operation == '-':
        result = args.num1 - args.num2
    if args.operation == '*':
        result = args.num1 * args.num2
    if args.operation == 'pow':
        result = pow(args.num1, args.num2)

    print("Result:",  result)
