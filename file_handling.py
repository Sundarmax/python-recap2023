def readFile():
    # open a file
    # default mode is read
    with open("file.txt") as file_obj:
        content = file_obj.read()
        print(content)
    try:
        with open("notexist.txt") as file_obj:
            content = file_obj.read()
            pass
    except FileNotFoundError:
        print("file not found")

 # https://www.freecodecamp.org/news/file-handling-in-python/
def appendFile():
    # append the data at end
    # create new file if mentioned file not exist.
    with open("file2.txt",'a') as file_obj:
        file_obj.write("append the new data")


def writeFile():
    # write, write +, append , append + creates new file if it doesn't exist.
    with open("file3.txt",'w+') as file_obj:
        file_obj.write('Hey cool buddy.!')


def readLine_():
    with open("file.txt", 'r') as file_obj:
        lines = file_obj.readlines()
        for line in lines:
            print(line)

def writeBinary():
    # write a file with binary mode
    # used to store image file
    with open("file3.txt",'wb') as file_obj:
        file_obj.write(b'\xC3\xA9')

#readFile()
#appendFile()
#writeFile()
#readLine_()
#writeBinary()
