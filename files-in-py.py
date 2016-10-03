#!/bin/python
#
import os, sys

path = os.getcwd()
path = path + "/test/"

# print path
#
os.system("mkdir -p ./test")

# file = open(path + 'test.txt', 'w')

def genFiles():
    count = 0
    for i in range(10000):
        count += 1
        # print('Hello world' + str(count))
        file = open(path + 'Hello world' + str(count), 'w')
        file.close


def renameFiles():
    files = os.listdir(path)
    for i in files:
        # print i
        os.rename(os.path.join(path, i), os.path.join(path, i.replace(' ', '-')))

    newfiles = os.listdir(path)
    for i in newfiles:
        print i

def delFiles():
    delfiles = os.listdir(path)

    for i in delfiles:
      print i
      os.remove(path + i)

# for arg in sys.argv:
#     print arg

args = sys.argv[1:]

def main():
    # print command line arguments
    for arg in args:
        print arg

        if arg == "genFiles":
            genFiles()
        elif arg == "renameFiles":
            renameFiles()
        elif arg == "delFiles":
            delFiles()
        else:
            print 'Usage with args. Example: genFiles, renameFiles, delFiles'
        # print args
    if not args:
         print 'Usage with args. Example: genFiles, renameFiles, delFiles'

if __name__ == "__main__":
    main()


# genFiles
# renameFiles
# delFiles()