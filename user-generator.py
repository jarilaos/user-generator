#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jarilaos

"""
import argparse
import string
import sys
import os

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
#username counter
n=0
default_surnames = "Top_World_Surnames_ByDefault.txt"

def banner():
    print('''%s
                             __    __       _______  _______  ______      
                            |  |  |  |     /       ||   ____||   _  \     
                            |  |  |  |    |   (----`|  |__   |  |_)  |    
                            |  |  |  |     \   \    |   __|  |      /     
                            |  '--'  | .----)   |   |  |____ |  |\  \----.
                             \______/  |_______/    |_______||__| `._____|
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
    parser = argparse.ArgumentParser(description='Generate usernames with different alphanumeric combinations.')
    parser.error = parser_error
    parser._positionals.title = "REQUIRED PARAMETERS"
    parser._optionals.title = "OPTIONAL PARAMETERS"
    #Files
    parser.add_argument("Names", help="The file containing the names.")
    parser.add_argument("-s", "--surnames", help="The path of the file containing the surnames. If none is specified, the 16 most common world surnames will be used")
    parser.add_argument("-o", "--output", help="The output name file. Default is usernames.txt", default="usernames.txt")
    parser.add_argument("-ef", "--emailsfile", help="The output file name for emails. Default is emails.txt", default="emails.txt")
    parser.add_argument("-lf", "--leetfile", help="The output file name for usernames in leet format. Default is leet.txtt", default="leet.txt")
    # Options
    parser.add_argument("-mC", "--min-chars", help="The minimum number of chars from the username. Default is 1.", type=int, default=1)
    parser.add_argument("-xC", "--max-chars", help="The maximum number of chars from the Name. Default is 25.", type=int, default=25)
    parser.add_argument("-mY", "--min-year", help="The year it starts. Default is 1942...No country for old men)", type=int, default=1942)
    parser.add_argument("-xY", "--max-year", help="The year it ends. Default is 2018.", type=int, default=2018)
    parser.add_argument("-n", "--number", help="Add a specific number. Default is None.", type=int, nargs='+')
    parser.add_argument("-u", "--union", help="Select if you want a binding character [_ . - ] etc. Default is None. ", nargs='+', default="")
    parser.add_argument("-e", "--email", help="Select if you want email usernames [gmail.com hotmail.us] etc. Default is None. ", nargs='+')
    parser.add_argument("-l", "--leet", help="To convert to leet format [username -> us3rn4m3]. 1:[e, o] 2:[a, e, i, o] 3:[a, e, i, o, s, t] 4:[a, e, i, o, s, t, l, b, g]. Default is None. ", type=int, choices=[1, 2, 3, 4])
    parser.add_argument("-m", "--mode", help="Results can be added or overwritten. Default is to overwrite.", choices=["a", "w"], default="w")
    parser.add_argument("-d", "--delduplicates", action='store_true', help="Sometimes the surnames are used as names and vice versa and this generates duplicates.")
    return parser.parse_args()

def create_surnames_file():
    results.surnames = default_surnames
    with open(results.surnames, 'w') as outfile:
        data = ['smith', 'garcia', 'gonzalez', 'hernandez', 'smirnov', 'müller', 'lee', 'li', 'zhang', 'wang', 'chang', 'nguyen', 'kumar', 'martin', 'silva', 'rossi', 'johnson']
        for line in data:
            outfile.write("%s\n"%line)

def leet(line):
    if results.leet == 1:
        chars = {"e":"3","E":"3","o":"0","O":"0"}
    elif results.leet == 2:
        chars = {"a":"4","A":"4","e":"3","E":"3","i":"1","I":"1","o":"0","O":"0"}
    elif results.leet == 3:
        chars = {"a":"4","A":"4","e":"3","E":"3","i":"1","I":"1","o":"0","O":"0","s":"5","S":"5","t":"7","T":"7"}    
    elif results.leet == 4:
        chars = {"a":"4","A":"4","e":"3","E":"3","i":"1","I":"1","o":"0","O":"0","s":"5","S":"5","t":"7","T":"7","l":"1","L":"1","b":"8","B":"8","g":"6","G":"6"}
    # TODO:customize the letters to convert
    getchar = lambda c: chars[c] if c in chars else c
    return ''.join(getchar(c) for c in line)

def add_numbers(line):
    global n
    l = len(line)
    #Line+Number
    if results.number is not None:
        for num in results.number:
            if l+len(str(num)) >= results.min_chars and l+len(str(num)) <= results.max_chars:
                outfile.write("%s%s\n" % (line, num))
                n+=1
    if l+1 >= results.min_chars and l+1 <= results.max_chars:
        for i in range(10):
            outfile.write("%s%s\n" % (line, i))
            n+=1
    if l+2 >= results.min_chars and l+2 <= results.max_chars:
        for i in range(100):
            outfile.write("%s%s\n" % (line, '{:02d}'.format(i)))
            n+=1
    if l+3 >= results.min_chars and l+3 <= results.max_chars:
        outfile.write("%s%d\n" % (line, 123))
        n+=1
    if l+4 >= results.min_chars and l+4 <= results.max_chars:
        for i in range(results.min_year, results.max_year+1):
            outfile.write("%s%d\n" % (line, i))
            n+=1
    #Line+Union+Number        
    for union in results.union:
        if results.number is not None:
            for num in results.number:
                if l+len(str(num))+1 >= results.min_chars and l+len(str(num))+1 <= results.max_chars:
                    outfile.write("%s%s%d\n" % (line,union, num))
                    n+=1
        if l+2 >= results.min_chars and l+2 <= results.max_chars:
            for i in range(10):
                outfile.write("%s%s%d\n" % (line, union, i))
                n+=1
        if l+3 >= results.min_chars and l+3 <= results.max_chars:
            for i in range(100):
                outfile.write("%s%s%s\n" % (line, union, '{:02d}'.format(i)))
                n+=1
        if l+4 >= results.min_chars and l+4 <= results.max_chars:
            outfile.write("%s%s%d\n" % (line, union, 123))
            n+=1
        if l+5 >= results.min_chars and l+5 <= results.max_chars:
            for i in range(results.min_year, results.max_year+1):
                outfile.write("%s%s%d\n" % (line, union, i))
                n+=1


if __name__ == "__main__":
    results = parse_args()
    banner()

    if results.surnames is None:
        create_surnames_file()      

    with open(results.output, results.mode.lower()) as outfile:
        with open(results.surnames, 'r') as reader:
            data = reader.read().splitlines() 
            for line in data:
                if len(line) >= results.min_chars and len(line) <= results.max_chars:
                    outfile.write("%s\n"%line)
                    n+=1
                #Letter+Surname    
                if len(line) >= results.min_chars-1 and len(line) <= results.max_chars-1:
                    for letter in string.ascii_lowercase:
                        outfile.write("%s%s\n" % (letter,line))
                        n+=1
                #Letter+Union+Surname 
                if len(line) >= results.min_chars-2 and len(line) <= results.max_chars-2:
                    for union in results.union:
                        for x in string.ascii_lowercase:
                            outfile.write("%s%s%s\n" % (x,union,line))
                            n+=1
                add_numbers(line)
        
        with open(results.Names, 'r') as names:
            data = names.read().splitlines() 
            for name in data:
                if len(name) >= results.min_chars and len(name) <= results.max_chars:
                    outfile.write("%s\n"%name)
                    n+=1
                #Name+Letter  
                if len(name) >= results.min_chars-1 and len(name) <= results.max_chars-1:
                    for letter in string.ascii_lowercase:
                        outfile.write("%s%s\n" % (name, letter))
                        n+=1
                #Name+Union+Letter 
                if len(name) >= results.min_chars-2 and len(name) <= results.max_chars-2:
                    for union in results.union:
                        for x in string.ascii_lowercase:
                            outfile.write("%s%s%s\n" % (name,union,x))
                            n+=1
                add_numbers(name)  

        with open(results.surnames, 'r') as reader , open(results.Names, 'r') as reader2:
            surnames = reader.read().splitlines()
            names = reader2.read().splitlines()
            for line in surnames:
                for name in names:
                    if len(name+line) >= results.min_chars and len(name+line) <= results.max_chars:
                        outfile.write("%s%s\n" % (name, line))
                        n+=1
                    if len(name+line) >= results.min_chars-1 and len(name+line) <= results.max_chars-1:
                        for union in results.union:
                            outfile.write("%s%s%s\n" % (name, union, line))
                            n+=1

        print ("Usernames generated:"+G+str(n))
        print (W+"Usernames dictionary: "+G+results.output+W)

    if results.surnames == default_surnames:
        os.remove(results.surnames)

    if results.delduplicates:
        n=0
        lines_stored = set()
        with open("temp", "w") as outfile:
            with open(results.output, "r") as reader:
                for line in reader:
                    if line not in lines_stored:
                        outfile.write(line)
                        lines_stored.add(line)
                        n+=1
        os.rename("temp", results.output) 
        print ("Usernames after delete duplicates: "+G+str(n)+W)

    if results.leet is not None:
        with open(results.output, 'r') as reader, open (results.leetfile, results.mode.lower()) as outfile:
            data = reader.read().splitlines() 
            for line in data:
                outfile.write("%s\n" % (leet(line)))
        print ("Leet dictionary: "+G+results.leetfile+W)   

    if results.email is not None:
        with open(results.output, 'r') as reader, open (results.emailsfile, results.mode.lower()) as outfile:
            data = reader.read().splitlines() 
            for e in results.email:
                for line in data:
                    outfile.write("%s@%s\n" % (line, e))
        print ("Emails dictionary: "+G+results.emailsfile+W)

