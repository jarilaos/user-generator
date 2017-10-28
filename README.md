# user-generator
Generate usernames with different alphanumeric combinations.
## Parameters
### Required parameter
  Names - The file containing the names.
### Optional parameters
               
| Short Form |     Long Form     | Description |
| ---------- | ----------------- | ------------ |
| -s  | --surnames | The file containing the surnames. Default is None |
| -o  | --output | The output name file. Default is usernames.txt |
| -mC | --min-chars | The minimum number of chars from the username. Default is 1. |
| -xC | --max-chars | The maximum number of chars from the Name. Default is 25. |
| -mY | --min-year | The year it starts. Default is 1942...No country for old men |
| -xY | --max-year | The year it ends. Default is 2018. |
| -n  | --number | Add a specific number. Default is None. |
| -u  | --union | Select if you want a binding character ( _ . - ) etc. Default is None. |
| -e  | --email | Select if you want email usernames (gmail.com hotmail.us) etc. Default is None. |
| -ef | --emailsfile | The output file name for emails. Default is emails.txt |
| -l  | --leet | To convert to leet format (username -> us3rn4m3). Choices=[1, 2, 3, 4]. 1(e, o), 2(a, e, i, o), 3(a, e, i, o, s, t), 4(a, e, i, o, s, t, l, b, g). Default is None. |
| -lf | --leetfile | The output file name for usernames in leet format. Default is leet.txt |
| -d  |--delduplicates| Sometimes the surnames are used as names and vice versa and this generates duplicates.|
| -m  | --mode  | Results can be added or overwritten. Default is to overwrite. |
| -h  | --help  | Show this help message and exit  |
