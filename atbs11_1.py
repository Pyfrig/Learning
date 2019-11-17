import os, shelve

# åpner fil i "read mode"
helloFile = open(r'D:\Google Drive\Prosjekter\Learning\hello.txt')

#leser fil
#helloFile.read()
#helloFile.close()
# leser og lagrer string til variable 
# kan evt bruke readlines/read
contents = helloFile.readlines()
print(contents)
helloFile.close()


shelfFile = shelve.open('mydata')
shelfFile ['cats'] = ['susi', 'loffen', 'pus']
shelfFile.close()

