#Building a command line snippets app
* This application can store a snippet with an associated name in the CSV file. The signiture of the function is put(name, snippet, filename).
* This application can also retrieve a snippet from a CSV file. The signiture of the function is get(name,filename)
* If you are trying to retrieve a snippet that hasn't been stored, then an error message will be printed out and you retrieve the value 'None'.
* The last argument 'filename' is optional. If it is missing, the default filename is snippets.csv
* This application support command line arguments, but the arguments must be inputed in the same order as the function signiture.
