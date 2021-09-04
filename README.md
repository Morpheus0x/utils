# Utils
General Scripts and Utilities
## Scripts
### create_bulk_domain_list.py
Generates three letter domain names
#### Help
```
Usage: ./create_bulk_domain_list.py [-s bulksize] [-o output] [-d domains]
                                    [-a|b|c string] [--xa|xb|xc string]
Examples:
./create_bulk_domain_list.py -o "./out" -s 2000
./create_bulk_domain_list.py -o "./out" -a d -b dsi -c dst -d at,eu,com,net,org
./create_bulk_domain_list.py -o "./out" -s 2000 -a d --xb xyz --xc xyz -d at,eu,gmbh
./create_bulk_domain_list.py --output "./out" --bulk-size 100 --domain at,eu,gmbh

Info:
    Domain scheme: abc.tld
        The default for a b and c is the alphabet from a to z.
        This can be reduced or replaced by using arguments described below

Options:
    -h, --help
    -s, --bulk-size <size>  How many domain per file, default: 0
    -o, --output <file> Output file name
    -d, --domain <domains>   comma seperated list of TLDs, default: at
    -a|b|c <string> replace the default alphabet with selected characters
    --xa|xb|xc <string> remove the characters in string from alphabet
```
