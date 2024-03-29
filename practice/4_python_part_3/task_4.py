"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
import Faker

def print_name_address(args: argparse.Namespace) -> None:
    fake=Faker()
    for _ in range(args.number):
        data={}
        for input,provider in args.field.items():
            data[input]=getattr(fake,provider)()

        print(data)
fake_argument=argparse.Namespace(number=2,fields={'fake_address':'address','some_name':'name'})
print_name_address(fake_argument)
