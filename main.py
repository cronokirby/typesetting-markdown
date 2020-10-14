#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Do stuff')
    parser.add_argument('--arg1', type=int, help='The first argument')


if __name__ == '__main__':
    main()
