#!/usr/bin/python3

import sys, getopt, re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter = {}
letter["a"] = alphabet.copy()
letter["b"] = alphabet.copy()
letter["c"] = alphabet.copy()
domain = ["at"]
outfile = "./out"
bulksize = 0

def help_exit(error=""):
	if error != "":
		print("Error: " + error)
	print("program help WIP")
	if error == "":
		sys.exit()
	else:
		sys.exit(1)

def main(argv):
	global letter, domain, outfile, bulksize
	try:
		opts, args = getopt.getopt(argv,"hs:o:d:a:b:c:",["help","bulk-size=","domain=", "output=", "xa=", "xb=", "xc="])
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
			letter[opt[-1]] = [char for char in arg]
		elif opt in ("--xa","--xb","--xc"):
			for char in arg:
				try:
					letter[opt[-1]].remove(char)
				except:
					help_exit("Double character detected: \'"+arg+"\'")
	#print("alphabet: ", alphabet)
	#print("letter_a: ", letter_a)
	#print("letter_b: ", letter_b)
	#print("letter_c: ", letter_c)
	#sys.exit()
	if bulksize == 0:
		file = open(outfile, 'w')
	else:
		file = None
		#print(file)
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
