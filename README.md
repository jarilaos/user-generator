# user-generator
Generate usernames with different alphanumeric combinations.

FILES REQUIRED:
  Names - The path of the file containing the dictionary with names.

OPTIONS:

  -h, --help - show this help message and exit 
  
  -s SURNAMES, --surnames SURNAMES - The path of the file containing the dictionary with surnames. If none is specified, the 16 most common world surnames will be used
                                       
  -o OUTPUT, --output OUTPUT - If you want to specify the name of the output file. Default is usernames.txt 
                        
  -ef EMAILSFILE, --emailsfile EMAILSFILE - If you want to specify the name of the output file for emails. Default is emails.txt 
                        
  -lf LEETFILE, --leetfile LEETFILE - If you want to specify the output file name for usernames in leet format. Default is leet
                        
  -mC MIN_CHARS, --min-chars MIN_CHARS - The minimum number of chars from the username. Default is 1.
                        
  -xC MAX_CHARS, --max-chars MAX_CHARS - The maximum number of chars from the Name. Default is 25.
                        
  -mY MIN_YEAR, --min-year MIN_YEAR - The year it starts. Default is 1942...No country for old men
                        
  -xY MAX_YEAR, --max-year MAX_YEAR - The year it ends. Default is 2018.
                        
  -n NUMBER [NUMBER ...], --number NUMBER [NUMBER ...] - Add a especific number. Default is None.
                        
  -u UNION [UNION ...], --union UNION [UNION ...] - Select if you want a binding character [_ . - ] etc. Default is None.
                        
  -e EMAIL [EMAIL ...], --email EMAIL [EMAIL ...] - Select if you want email usernames [gmail.com hotmail.us] etc. Default is None.
                        
  -l {1,2,3,4}, --leet {1,2,3,4} - To convert to leet format [username -> us3rn4m3]. 
                        
                        1:[e, o] 
                        
                        2:[a, e, i, o] 
                        
                        3:[a, e, i, o, s, t] 
                        
                        4:[a, e, i, o, s, t, l, b, g]. Default is None.
                        
  -m {a,w}, --mode {a,w} - If you want the results to be appended to the file or to overwrite. Default is overWrite.
                        
  -d, --delduplicates - Sometimes the surnames are used as names and vice versa and this generates duplicates.
