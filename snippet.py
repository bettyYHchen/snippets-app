import logging
import csv
import argparse
import sys

def make_parser():
	"""Construct the command line parse"""
	logging.info("Constructing parser")
	description="Store and retrieve snippets of text"
	parser=argparse.ArgumentParser(description=description)
	#the add_subparsers method allow us to add multiple subparser
	#For subparser, I mean the subset of the arguments that the program can still run

	subparsers = parser.add_subparsers(dest="command",help="Available commands")
	#the "dest" argument is added to allow us to work out which command was entered 
	#after the parsing has been taken place
	# Subparser for the put command
	logging.debug("Constructing put subparser")
	#Initialize a new subparser (subparser is same as parser except that it allow partial arguments)
	put_parser = subparsers.add_parser("put",help="Store a snippet")
	#Add argument of the parser
	put_parser.add_argument("name", help="The name of the snippet")
	put_parser.add_argument("snippet", help="The snippet text")
	put_parser.add_argument("filename", default="snippets.csv",nargs="?", help="The snippet filename")

	return parser

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name,snippet,filename):
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename,"a") as f:
    	writer = csv.writer(f)
    	logging.debug("Writing snippet to file")
    	writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def main():
	""" Main function """
	logging.info("Starting snippet")
	parser=make_parser() #make_parser create the command line parser object
	arguments=parser.parse_args(sys.argv[1:]) #the parse_args method of the perser
	print parser.parse_args(sys.argv[1:])
	#object, passing in all of the command line argument except the first, coz the 
	#first one always contains the name of our program
	#It returns a Namespace object, and we want to convert it to a dictionary object
	#arguments = vars(arguments) #Convert to dictionary object
	print arguments
	arguments = vars(arguments)
	print arguments
	command = arguments.pop("command")
	print command
	#The use of the double-star opertator is known as uppacking. 
	#It converts the key-value pair in the dictionary into keyword arguemnts to the function.
	if command == "put":
		name, snippet = put(**arguments)
		print "Store {!r} as {!r}".format(snippet, name)


if __name__ == "__main__":
	main()

