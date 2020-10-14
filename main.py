#!/usr/bin/env python3
import argparse
from enum import Enum
import logging
from shutil import which

REQUIREMENTS = [
    ('pandoc', 'https://www.pandoc.org'),
    ('context', 'https://wiki.contextgarden.net'),
    ('gs', 'https://www.ghostscript.com')
]


class ColoredFormatter(logging.Formatter):

    GRAY = "\x1b[38;1m"
    BLUE = "\x1b[34;1m"
    YELLOW = "\x1b[33;1m"
    RED = "\x1b[31;1m"
    BOLD = "\x1b[4m"
    RESET = "\x1b[0m"

    LEVEL_FORMAT = '[%(levelname)-7s]'
    MESSAGE_FORMAT = '%(message)s'

    FORMATS = {
        logging.INFO: f'{GRAY}{LEVEL_FORMAT}{RESET} {GRAY}{MESSAGE_FORMAT}{RESET}',
        logging.DEBUG: f'{BLUE}{LEVEL_FORMAT}{RESET} {BLUE}{MESSAGE_FORMAT}{RESET}',
        logging.WARN: f'{YELLOW}{BOLD}{LEVEL_FORMAT}{RESET} {YELLOW}{MESSAGE_FORMAT}{RESET}',
        logging.CRITICAL: f'{YELLOW}{BOLD}{LEVEL_FORMAT}{RESET} {YELLOW}{MESSAGE_FORMAT}{RESET}',
        logging.ERROR: f'{RED}{BOLD}{LEVEL_FORMAT}{RESET} {RED}{MESSAGE_FORMAT}{RESET}',
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger(log_level, no_color):
    level = logging.WARN

    declared = log_level.upper()
    if declared == 'DEBUG':
        level = logging.DEBUG
    elif declared == 'INFO':
        level = logging.INFO

    ch = logging.StreamHandler()
    if no_color:
        ch.setFormatter(logging.Formatter("[%(levelname)-7s] %(message)s"))
    else:
        ch.setFormatter(ColoredFormatter())
    get_logger().addHandler(ch)
    get_logger().propagate = False
    logging.basicConfig(level=level)


def get_logger():
    return logging.getLogger(__name__)


def log_info(*args, **kwargs):
    get_logger().info(*args, **kwargs)


def log_warn(*args, **kwargs):
    get_logger().warning(*args, **kwargs)


def log_error(*args, **kwargs):
    get_logger().error(*args, **kwargs)


def log_debug(*args, **kwargs):
    get_logger().debug(*args, **kwargs)


def parse_args():
    '''
    Parse the arguments we need for our script.
    '''
    parser = argparse.ArgumentParser(description='Do stuff')
    parser.add_argument('-ll', '--log-level', type=str,
                        help='Log more information during execution')
    parser.add_argument('--no-color', action='store_true',
                        help='Do not use color when logging')
    return parser.parse_args()


def command_exists(name):
    return which(name) is not None


def check_requirements():
    for name, url in REQUIREMENTS:
        if not command_exists(name):
            log_error(f'Missing required program: {name}\t{url}')
            return False
    return True


def main():
    '''
    The main body of our script.

    Overview:
        1. Parse Arguments
        2. Use Arguments
    '''
    args = parse_args()

    setup_logger(args.log_level, args.no_color)

    if not check_requirements():
        exit(-1)

    log_warn('Something bad has happened')
    log_error('Something even worse has happened')
    log_info('Program requirements satisfied!')
    log_debug('Testing')


if __name__ == '__main__':
    main()
