#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jarilaos

"""
import argparse
import sys
import string
from itertools import product


# Console Colors
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white

#You should not be using windows for that XD
if sys.platform.startswith('win'):
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
    except:
        print("[!] Error: Coloring libraries not installed. If you want to do it, type this: [python.exe -m pip install win_unicode_console colorama]")
        G = Y = B = R = W = ''

def banner():
    print('''%s
                  ___       ______ .______        ______   .__   __. ____    ____ .___  ___.
                 /   \     /      ||   _  \      /  __  \  |  \ |  | \   \  /   / |   \/   |
                /  ^  \   |  ,----'|  |_)  |    |  |  |  | |   \|  |  \   \/   /  |  \  /  |
               /  /_\  \  |  |     |      /     |  |  |  | |  . `  |   \_    _/   |  |\/|  |
              /  _____  \ |  `----.|  |\  \----.|  `--'  | |  |\   |     |  |     |  |  |  |
             /__/     \__\ \______|| _| `._____| \______/  |__| \__|     |__|     |__|  |__|
       _______  _______  __   __   _______  ______          ___    ___________   ______    ______      
      /  _____||   ____||  \ |  | |   ____||   _  \        /   \  |           | /  __  \  |   _  \     
     |  |  __  |  |__   |   \|  | |  |__   |  |_)  |      /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
     |  | |_ | |   __|  |  . `  | |   __|  |      /      /  /_\  \    |  |     |  |  |  | |      /     
     |  |__| | |  |____ |  |\   | |  |____ |  |\  \----./  _____  \   |  |     |  `--'  | |  |\  \----.
      \______| |_______||__| \__| |_______||__| `._____/__/     \__\  |__|      \______/  |__| `._____|%s
      '''% (Y,W))


def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(description='Generate alphabet acronyms.')
    parser.error = parser_error
    parser._positionals.title = "REQUIRED PARAMETERS"
    parser._optionals.title = "OPTIONAL PARAMETERS"

    parser.add_argument("-o", "--output", help="The output file. Default is acronyms.txt", default="acronyms.txt")
    parser.add_argument("-n", "--num-chars", help="The number of chars from the username. Default is 4.", type=int, default=4)
    parser.add_argument("-p", "--prefix", help="Select the prefix string. Default is "" ",nargs='+', default="")
    parser.add_argument("-s", "--sufix", help="Select the sufix string. Default is "" ",nargs='+', default="")
    parser.add_argument("-m", "--mode", help="Results can be added or overwritten. Default is to overwrite.", choices=["a", "w"], default="w")
    return parser.parse_args()

def generate():
    n=0
    acronym=""
    print (Y+"[+]Generating acronyms..."+W)
    with open(results.output, results.mode.lower()) as outfile:
        acronyms = list(map(''.join, product(string.ascii_lowercase, repeat =results.num_chars)))
        for line in acronyms:
            outfile.write(line+"\n")
            n+=1

    if results.prefix is not "":
        with open(results.output, "r+") as reader:
            lines = reader.read().splitlines()
            print (Y+"[+]Adding prefix..."+W)
            for prefix in results.prefix:
                for line in lines:
                    reader.write(prefix+line+"\n")
                    n+=1
                    
    elif results.sufix is not "":
        with open(results.output, "r+") as file:
            lines = file.read().splitlines()
            for sufix in results.sufix:
                print (Y+"[+]Adding sufix..."+W)
                for line in lines:
                    file.write(line+sufix+"\n")
                    n+=1                                
    
    print (Y+"[+]Acronyms generated:  "+G+str(n))
    print (Y+"[+]Acronym dictionary: "+G+results.output+W)

def main():
    generate()

if __name__ == "__main__":
    results = parse_args()
    banner()
    main()
