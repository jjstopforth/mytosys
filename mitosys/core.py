'''
This script will eventually be used for me to maintain a consistent config
across my various systems. 

That includes a set of core configurations such as:
    - vim and vim plugins
    - shell rc files
    - Xresources (where applicable)
    - custom scripts (such as this one)

As well as maintaining platform/distro specific things:
    - Managing packages
    - Setting up desktop environments

Hopefully all of this should eventually be able to go in a monolithic config
file with the relevant sections called as necessary/specified.

TODO: Add update vs first initialisation distinction. e.g. mitosys --init vs mitosys --update
TODO: Add detection/specification of os/distro
TODO: add groups of config: 'minimal', 'base', 'full'
TODO: allow exclusion of certain config with '--exclude' or '-x'

'''


import argparse
import configparser
import urllib.request

PROG = 'mitosys'
VERSION = "0.0.1"
DESCRIPTION = 'Duplicate system setup with mutation'

def setup_argparser(): 

    parser = argparse.ArgumentParser(prog=PROG, description=DESCRIPTION)

    parser.add_argument('-v', '--version',
            action='version', 
            version='%(prog)s ' + VERSION
            ) 

    parser.add_argument('-c', '--config',
            default='config.ini',
            help='Specify a config file'
            )

    return parser

def load_config(file):
    
    config = configparser.ConfigParser()
    config.read(file)

    return config

def apply_patches(diff_filenames):
    '''
    This should spit out errors and bail if any patch fails to be applied
    correctly.
    '''
    pass

def run():
    parser = setup_argparser()
    args = parser.parse_args()

    config = load_config(args.config)
    print(config.sections())
    print('vim' in config)
    print([x for x in config['vim.plugins']])

