# importing the required modules
import os
import argparse
import re

 
# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."
 
 
def validate_file(file_name):
    '''
    validate file name and path.
    '''
    if not valid_path(file_name):
        print(INVALID_PATH_MSG%(file_name))
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG % (file_name))
        quit()
    return
     
def valid_filetype(file_name):
    # validate file type
    return file_name.endswith('.txt')
 
def valid_path(path):
    # validate file path
    return os.path.exists(path)

def read(args):
    # get the file name/path
    file_name = args.lines[0]

    # validate the file name/path
    validate_file(file_name)
    # read and print Number of lines in file
    with open(file_name, 'r') as f:
        file = f.read()
    return file

def lines(args):
    NoOfLine= 0
    file = read(args)
    for i in file:
        if i:
            NoOfLine += 1
    print(NoOfLine)


def noOfChars(args):
    file = read(args)
    text = file.strip().split()
    noofchars = sum(len(word) for word in text)
    print(noofchars)


def noOfWords(args):
    file = read(args)
    text = file.strip().split()
    words = len(text)
    print(words)

def onlyNumeric(args):
    file = read(args)
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
    print(numbers)
 
def onlyAlphabets(args):
    file = read(args)
    for i in file:
        if i.isalpha():
            alpha = "".join([alpha, i])
    print(alpha)

def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "The help for command line argiments!")
 
    # defining arguments for parser object
    parser.add_argument("-l", "--lines", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "display no. of lines in the input file.")
     
    parser.add_argument("-c", "--noOfChars", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "display no. of character present in the input file.")

    parser.add_argument("-w", "--noOfWords", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "display no. of words present in the input file.")


    parser.add_argument("-n", "--onlyNumeric", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "display only numeric numbers present in the input file.")
     

    parser.add_argument("-a", "--onlyAlphabets", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "display only alphabets in the input file.")

    # parse the arguments from standard input
    args = parser.parse_args()
     
    # calling functions depending on type of argument
    if args.lines != None:
        lines(args)
    elif args.noOfChars != None:
        noOfChars(args)
    elif args.noOfWords !=None:
        noOfWords(args)
    elif args.onlyNumeric != None:
        onlyNumeric(args)
    elif args.onlyAlphabets != None:
        onlyAlphabets(args)
 
 
if __name__ == "__main__":
    # calling the main function
    main()