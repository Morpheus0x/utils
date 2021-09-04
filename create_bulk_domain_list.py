#!/usr/bin/python3

import sys, getopt, re

help = "Usage: "+ __file__ + """ [-s bulksize] [-o output] [-d domains]
\t\t\t\t\t\t\t\t\t[-a|b|c string] [--xa|xb|xc string]
Examples:
"""+__file__+""" -o \"./out\" -s 2000
"""+__file__+""" -o \"./out\" -a d -b dsi -c dst -d at,eu,com,net,org
"""+__file__+""" -o \"./out\" -s 2000 -a d --xb xyz --xc xyz -d at,eu,gmbh
"""+__file__+""" --output \"./out\" --bulk-size 100 --domain at,eu,gmbh

Info:
\tDomain scheme: abc.tld
\t\tThe default for a b and c is the alphabet from a to z.
\t\tThis can be reduced or replaced by using arguments described below

Options:
\t-h, --help
\t-s, --bulk-size <size>\tHow many domain per file, default: 0
\t-o, --output <file>\tOutput file name/path
\t-d, --domain <domains>\t comma seperated list of TLDs, default: at
\t-a|b|c <string>\treplace the default alphabet with selected characters
\t--xa|xb|xc <string>\tremove the characters in string from alphabet
works pretty good\n
\t even tabulated"""+ __file__+ "and even with variables"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter = {}
letter["a"] = alphabet.copy()
letter["b"] = alphabet.copy()
letter["c"] = alphabet.copy()
alphamod = {"a": False, "b": False, "c": False}
domain = ["at"]
outfile = "./out"
bulksize = 0

def help_exit(error=""):
	if error != "":
		print("##########\nError: " + error +"\n##########\n")
	print(help.expandtabs(4))
	if error == "":
		sys.exit()
	else:
		sys.exit(1)

def main(argv):
	global letter, domain, outfile, bulksize
	try:
		opts, args = getopt.getopt(argv,"hs:o:d:a:b:c:",["help","bulk-size=", "output=", "domain=", "xa=", "xb=", "xc="])
	except getopt.GetoptError:
		help_exit()
	for opt, arg in opts:
		if opt in("-h", "--help"):
			print("actual help")
			help_exit()
		elif opt in ("-s", "--bulk-size"):
			bulksize = int(arg)
		elif opt in ("-o", "--output"):
			outfile = arg
		elif opt in ("-d", "--domain"):
			if re.match("([a-z]){2,}(,([a-z]){2,})*", arg) == None:
				print(help_exit("Wrong Domain format: \'"+arg+"\'"))
				exit(1)
			domain = arg.split(",")
		elif opt in ("-a", "-b", "-c"):
			if alphamod[opt[-1]] == True:
				help_exit("Only one replacement or exclusion list is allowed per position, a b or c!")
			alphamod[opt[-1]] = True
			letter[opt[-1]] = [char for char in arg]
		elif opt in ("--xa","--xb","--xc"):
			if alphamod[opt[-1]] == True:
				help_exit("Only one replacement or exclusion list is allowed per position, a b or c!")
			alphamod[opt[-1]] = True
			for char in arg:
				try:
					letter[opt[-1]].remove(char)
				except:
					help_exit("Double character detected: \'"+arg+"\'")
	if bulksize == 0:
		file = open(outfile, 'w')
	else:
		file = None
	counter = 0
	file_count = 0;
	for tld in domain:
		for a in letter["a"]:
			for b in letter["b"]:
				for c in letter["c"]:
					if counter % 2000 == 0 and bulksize != 0:
						if file != None:
							file.close()
						file = open(outfile+str(file_count), 'w')
						file_count += 1
					counter += 1
					file.write(a+b+c+"."+tld+"\n")


if __name__ == "__main__":
	main(sys.argv[1:])
