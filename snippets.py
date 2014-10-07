import sys
import argparse
import logging
import csv
 
# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)
 
def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file")
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def get(name,filename):
    """Retrieve a snippet from the file"""
    logging.info("Getting {} from {}".format(name,filename))
    logging.debug("Reading file")
    with open(filename,"rb") as f_obj:
        reader = csv.reader(f_obj)
        logging.debug("Reading speadsheet")
        my_dict={}
        for row in reader:
            #row is a list, where the first element is name and the second element 
            # is snippet
            my_dict[row[0]]=row[1]
            logging.debug("Read sucessful")
        try: 
            return my_dict[name]
        except:
            print "Error: the snippet hasn't been stored yet"



 
def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)
 
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    # Subparser for the get command
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?",
                            help="The snippet filename")
    get_parser.add_argument("name",help="The name of the snippet")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?",
                            help="The snippet filename")
 
    return parser
 
def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")
 
    if command == "put":
        name, snippet = put(**arguments)
        print "Stored '{}' as '{}'".format(snippet, name)
    elif command == "get":
        snippet = get(**arguments)
        print "Retrieve '{}'".format(snippet)
    else:
        raise NameError('Undefined command')

     
if __name__ == "__main__":
    main()