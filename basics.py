#Text aus einer Datei lesen
#open(filename,mode) and .close()
fobj = open("poem.txt", "r") 
for line in fobj:
    print(line.rstrip())
fobj.close()

#read()
poem = open("poem.txt").read()
print(poem[4:7])
poem.close()

#readlines()
poem = open("poem.txt").readlines()
print(poem)
poem.close()

#In einer Datei schreiben: .write()
fo = open("poem.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()

#with-Anweisung verwenden
with open("poem.txt", "w") as fh:
	fh.write("To write or not to write\nthat is the question!\n")

#Ausgabe mit .format() in print() formatieren
data = dict(province="Ontario",capital="Toronto")
data
{'province': 'Ontario', 'capital': 'Toronto'}
print("The capital of {province} is {capital}".format(**data))
#The capital of Ontario is Toronto


capital_country = {"Vereinigte Staaten" : "Washington", 
                   "US" : "Washington", 
                   "Kanada" : "Ottawa",
                   "Deutschland": "Berlin",
                   "Frankreich" : "Paris",
                   "England" : "London",
                   "Großbritannien" : "London",
                   "Schweiz" : "Bern",
                   "Österreich" : "Wien",
                   "Niederlande" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    format_string = c + ": {" + c + "}" 
    print(format_string.format(**capital_country))



#Das os-Modul kennen
#The OS module in Python provides a way of using operating system dependent functionality.
#The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on.
import os

#Executing a shell command
os.system()    

#Get the users environment 
os.environ()   

#Returns the current working directory
os.getcwd()   

#Return the real group id of the current process.
os.getgid()       

#Return the current process’s user id.
os.getuid()    

##Returns the real process ID of the current process.
os.getpid()     

#Set the current numeric umask and return the previous umask.
os.umask(mask)   

#Return information identifying the current operating system.
os.uname()     

#Change the root directory of the current process to path.
os.chroot(path)   

#Return a list of the entries in the directory given by path.
os.listdir(path) 

#Create a directory named path with numeric mode mode.
os.mkdir(path)    

#Recursive directory creation function.
os.makedirs(path)  

#Remove (delete) the file path.
os.remove(path)    

#Remove directories recursively.
os.removedirs(path) 

#Rename the file or directory src to dst.
os.rename(src, dst)  

#Remove (delete) the directory path.
os.rmdir(path)    

#Zeichenkodierung in Python
#UTF-8 Standard ab Python 3.x (Es kann aber jede andere Zeichenkodierung genutzt werden)
#8 Bits = 1 Byte für die Kodierung eines einzelnen Zeichens
#Die ersten 256 Zeichen entsprechen dem ISO Latin-1-Zeichensatz
#-*-coding: utf-8-*-
#-*-coding: iso-8859-1-*-
#https://docs.python.org/3/howto/unicode.html
intZeichen = ord('A')chrZeichen = chr(intZeichen)

zeichenUnicode = u"æøå"

escapeUnicode = "\u00E6\u00F8\u00E5"
