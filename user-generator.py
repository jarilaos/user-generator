#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jarilaos

"""
import argparse
import string

parser = argparse.ArgumentParser(description='Generate usernames with different alphanumeric combinations.')
#Files
parser.add_argument("Names", help="The path to the file containing the dictionary with names.")
parser.add_argument("Surnames", help="The path to the file containing the dictionary with surnames.")
parser.add_argument("-o", "--output", help="If you want to specify the name of the output file. Default is usernames", default="usernames.txt")
parser.add_argument("-ef", "--emailsfile", help="If you want to specify the name of the output file for emails. Default is emails", default="emails.txt")
parser.add_argument("-lf", "--leetfile", help="If you want to specify the name of the output file for leet format usernames. Default is leet", default="leet.txt")
# Options
parser.add_argument("-mC", "--min-chars", help="The minimum number of chars from the username. Default is 1.", type=int, default=1)
parser.add_argument("-xC", "--max-chars", help="The maximum number of chars from the Name. Default is 20.", type=int, default=25)
parser.add_argument("-mY", "--min-year", help="The year it starts. Default is 1940.", type=int, default=1940)
parser.add_argument("-xY", "--max-year", help="The year it ends. Default is 2018.", type=int, default=2018)
parser.add_argument("-m", "--mode", help="If you want the results to be appended to the file or to overwrite. Default is overWrite.", choices=["a", "w"], default="w")
parser.add_argument("-u", "--union", help="Select if you want a binding character [_ . - ] etc. Default is None. ", nargs='+', default="")
parser.add_argument("-e", "--email", help="Select if you want an email [gmail.com hotmail.us] etc. Default is None. ", nargs='+', default="")
parser.add_argument("-l", "--leet", help="If you want, select the level to convert to leet format [username -> us3rn4m3]. Level 1 only vowels, level 2 some consonants too. Default is None. ", type=int, choices=[1, 2], default=0)
results = parser.parse_args()

def leet(text):
    getchar = lambda c: chars[c] if c in chars else c
    if results.leet == 1:
        chars = {"a":"4","e":"3","i":"1","o":"0","A":"4","E":"3","I":"1","O":"0"}
    else:
        chars = {"a":"4","e":"3","i":"1","o":"0","A":"4","E":"3","I":"1","O":"0","s":"5","S":"5","l":"1","L":"1","t":"7","T":"7","b":"8","B":"8"}
    return ''.join(getchar(c) for c in text)

print('''
                         __    __       _______  _______  ______      
                        |  |  |  |     /       ||   ____||   _  \     
                        |  |  |  |    |   (----´|  |__   |  |_)  |    
                        |  |  |  |     \   \    |   __|  |      /     
                        |  '--'  | .----)   |   |  |____ |  |\  \----.
                         \______/  |_______/    |_______||__| `._____|
   _______  _______  __   __   _______  ______          ___    ___________   ______    ______      
  /  _____||   ____||  \ |  | |   ____||   _  \        /   \  |           | /  __  \  |   _  \     
 |  |  __  |  |__   |   \|  | |  |__   |  |_)  |      /  ^  \ `---|  |----´|  |  |  | |  |_)  |    
 |  | |_ | |   __|  |  . `  | |   __|  |      /      /  /_\  \    |  |     |  |  |  | |      /     
 |  |__| | |  |____ |  |\   | |  |____ |  |\  \----./  _____  \   |  |     |  `--'  | |  |\  \----.
  \______| |_______||__| \__| |_______||__| `._____/__/     \__\  |__|      \______/  |__| `._____|
  
\nThe file is being generated with the following options...''')
print(results)

with open(results.output, results.mode.lower()) as outfile:
    with open(results.Surnames, 'r') as reader:
        data = reader.read().splitlines() 
        for line in data:
            if len(line) >= results.min_chars and len(line) <= results.max_chars:
                outfile.write("%s\n"%line)
            if len(line) >= results.min_chars-1 and len(line) <= results.max_chars-1:
                for letter in string.ascii_lowercase:
                    outfile.write("%s%s\n" % (letter, line))
            if len(line) >= results.min_chars-2 and len(line) <= results.max_chars-2:
                for union in results.union:
                    for x in string.ascii_lowercase:
                        outfile.write("%s%s%s\n" % (x,union, line))

    with open(results.Names, 'r') as names:
        data = names.read().splitlines() 
        for name in data:
            if len(name) >= results.min_chars and len(name) <= results.max_chars:
                outfile.write("%s\n"%name)
            if len(name) >= results.min_chars-1 and len(name) <= results.max_chars-1:
                for i in range(10):
                    outfile.write("%s%s\n" % (name, i))
            if len(name) >= results.min_chars-2 and len(name) <= results.max_chars-2:
                for i in range(100):
                    outfile.write("%s%s\n" % (name, '{:02d}'.format(i)))
            if len(name) >= results.min_chars-3 and len(name) <= results.max_chars-3:
                outfile.write("%s%d\n" % (name, 123))
            for i in range(results.min_year, results.max_year+1):
                if len(name) >= results.min_chars-4 and len(name) <= results.max_chars-4:
                    outfile.write("%s%d\n" % (name, i))
                    
            for union in results.union:
                if len(name) >= results.min_chars-2 and len(name) <= results.max_chars-2:
                    for i in range(10):
                        outfile.write("%s%s%d\n" % (name, union, i))
                if len(name) >= results.min_chars-3 and len(name) <= results.max_chars-3:
                    for i in range(100):
                        outfile.write("%s%s%s\n" % (name, union, '{:02d}'.format(i)))
                if len(name) >= results.min_chars-4 and len(name) <= results.max_chars-4:
                    outfile.write("%s%s%d\n" % (name, union, 123))
                for i in range(results.min_year, results.max_year+1):
                    if len(name) >= results.min_chars-5 and len(name) <= results.max_chars-5:
                        outfile.write("%s%s%d\n" % (name, union, i))   

    with open(results.Surnames, 'r') as reader , open(results.Names, 'r') as reader2:
        surnames = reader.read().splitlines()
        names = reader2.read().splitlines()
        for line in surnames:
            for name in names:
                if len(name+line) >= results.min_chars and len(name+line) <= results.max_chars:
                    outfile.write("%s%s\n" % (name, line))
                for union in results.union:
                    if len(name+line) >= results.min_chars-1 and len(name+line) <= results.max_chars-1:
                        outfile.write("%s%s%s\n" % (name, union, line))

if results.leet != 0:
    with open(results.output, 'r') as reader, open (results.leetfile, results.mode.lower()) as outfile:
        data = reader.read().splitlines() 
        for line in data:
            outfile.write("%s\n" % (leet(line)))   

if results.email != "":
    with open(results.output, 'r') as reader, open (results.emailsfile, results.mode.lower()) as outfile:
        data = reader.read().splitlines() 
        for e in results.email:
            for line in data:
                outfile.write("%s@%s\n" % (line, e))