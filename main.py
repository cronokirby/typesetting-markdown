#!/usr/bin/env python3
import argparse
from enum import Enum
import logging


def setup_logger(verbose):
    level = logging.WARN
    if verbose:
        level = logging.INFO
    logging.basicConfig(level=level, format='%(levelname)-8s %(message)s')


def get_logger():
    return logging.getLogger(__name__)


def log_info(*args, **kwargs):
    get_logger().info(*args, **kwargs)


def log_warn(*args, **kwargs):
    get_logger().warning(*args, **kwargs)


def log_error(*args, **kwargs):
    get_logger().error(*args, **kwargs)


def parse_args():
    '''
    Parse the arguments we need for our script.
    '''
    parser = argparse.ArgumentParser(description='Do stuff')
    parser.add_argument('-v', '--verbose', action="store_true",
                        help='Log more information during execution')
    return parser.parse_args()


def main():
    '''
    The main body of our script.

    Overview:
        1. Parse Arguments
        2. Use Arguments
    '''
    args = parse_args()
    setup_logger(args.verbose)
    log_error('Uh oh')
    log_warn('I think something bad is happening')
    log_info('Just for your information, it\'s ok')


if __name__ == '__main__':
    main()
