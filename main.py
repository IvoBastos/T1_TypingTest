#!/usr/bin/python3

import string
import random
import readchar
from colorama import Fore, Style, Back
from time import time, ctime
import argparse
from collections import namedtuple
import pprint

Input = namedtuple("Input", ["requested", "received", "duration"])
Statistics = {
    "accuracy": 0.0,
    "inputs": [Input(requested="", received="", duration=0.0)],
    "number_of_hits": 0,
    "number_of_types": 0,
    "test_duration": 0.0,
    "test_end": "",
    "test_start": "",
    "type_average_duration": 0.0,
    "type_hit_average_duration": 0.0,
    "type_miss_average_duration": 0.0
}


def main():
    parser = argparse.ArgumentParser(description=' PSR typing test ')
    parser.add_argument('-mv', '--max_value', type=int, help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.')
    parser.add_argument('-utm', '--use_time_mode', type=bool, help='Defines if time mode is used.')

    args = vars(parser.parse_args())
    print(args)

    print("Typing test PSR. Press any key to begin the test")
    pressed_continue=readchar.readkey()
    if pressed_continue:
        if args['utm']:
            modo_tempo(args['MAX_VALUE'])
        else:
            modo_teclas(args['MAX_VALUE'])

    print(Fore.BLUE + "You finished the test, here are your results:" + Style.RESET_ALL)
    pprint(Statistics)


if __name__ == "__main__":
    main()