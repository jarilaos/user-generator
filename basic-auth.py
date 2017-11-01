#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jarilaos

"""
import argparse
import sys
import base64

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
                    .______        ___           _______. _______    __    _  _
                    |   _  \      /   \         /       ||   ____|  / /   | || |
                    |  |_)  |    /  ^  \       |   (----`|  |__    / /_   | || |_
                    |   _  <    /  /_\  \       \   \    |   __|  | '_ \  |__   _|
                    |  |_)  |  /  _____  \  .----)   |   |  |____ | (_) |    | |
                    |______/  /__/     \__\ |_______/    |_______| \___/     |_|
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
    parser = argparse.ArgumentParser(description='Generate base64-encoded usernames and passowords tuples.')
    parser.error = parser_error
    parser._positionals.title = "REQUIRED PARAMETERS"
    parser._optionals.title = "OPTIONAL PARAMETERS"

    parser.add_argument("-u", "--username", help="One or more username. Default is None",nargs='+')
    parser.add_argument("-uf", "--usernames", help="The file containing the usernames.")
    parser.add_argument("-p", "--passwords", help="The path of the file containing the passwords.", required=True)
    parser.add_argument("-o", "--output", help="The output file. Default is base64.txt", default="base64.txt")
    parser.add_argument("-d", "--decode", help="The file containing the base64-encoded strings. Default is None")    
    parser.add_argument("-l", "--linkage", help="Select the linkage character [: -] etc. Default is : ", default=":")
    parser.add_argument("-m", "--mode", help="Results can be added or overwritten. Default is to overwrite.", choices=["a", "w"], default="w")
    return parser.parse_args()

def decode():
    n=0
    print (Y+"[+]Decoding strings..."+W)
    with open(results.output, results.mode.lower()) as outfile:
        with open(results.decode, 'r') as reader:
            lines = reader.read().splitlines()
            for line in lines:
                decoded =  base64.b64decode(line).decode('utf-8')
                outfile.write("%s\n" % decoded)
                n+=1
                if "adm" in decoded.lower():
                    print(R + "[+]Critical user: "+decoded+W)
    print (Y+"[+]Strings decoded:  "+G+str(n))
    print (Y+"[+]Output file: "+G+results.output+W)

def encode():
    n=0
    print (Y+"[+]Generating tuples..."+W)
    with open(results.output, results.mode.lower()) as outfile:
        if results.usernames is not None:
            with open(results.usernames, 'r') as reader , open(results.passwords, 'r') as reader2:
                usernames = reader.read().splitlines()
                passwords = reader2.read().splitlines()
                for username in usernames:
                    for password in passwords:
                        data = (username+results.linkage+password).encode('utf-8')
                        encoded = base64.b64encode(data).decode('utf-8')                    
                        outfile.write("%s\n" % encoded)
                        n+=1

        elif results.username is not None:
             with open(results.passwords, 'r') as reader2:
                passwords = reader2.read().splitlines()
                for username in results.username:
                    for password in passwords:
                        data = (username+results.linkage+password).encode('utf-8')
                        encoded = base64.b64encode(data).decode('utf-8')                    
                        outfile.write("%s\n" % encoded)
                        n+=1
    	else:
        	parser_error("Any input parameter introduced")

        print (Y+"[+]Tuples generated:  "+G+str(n))
        print (Y+"[+]Base64 dictionary: "+G+results.output+W)

def main():
    if results.decode is None:
        encode()
    else:
        decode()

if __name__ == "__main__":
    results = parse_args()
    banner()
    main()
