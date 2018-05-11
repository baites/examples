#! /bin/env python3

import argparse
from importlib import import_module
from pprint import pprint
import logging
import sys


def main():

    # Setup the basic command line and options
    parser = argparse.ArgumentParser(description='Run a plugin.')
    parser.add_argument('--plugin', dest='plugin', help='plugin name', required=True)
    parser.add_argument('--srvuser', dest='srvuser', help='service user name', required=True)
    parser.add_argument('--srvpasswd', dest='srvpasswd', help='service password', required=True)
    args = parser.parse_args()

    plugin = import_module(args.plugin).create(
        srvuser=args.srvuser,
        srvpasswd=args.srvpasswd
    )

    payload = plugin()

    pprint(payload)


if __name__ == '__main__':
    main()
