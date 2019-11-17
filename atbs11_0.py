import os
"""
filePath = os.path.join('folder1', 'folder2', 'folder3','file.png')

print(os.getcwd())
"""

totalSize = 0


# listdir lister opp alle filer/mapper i gitt sti.
for filename in os.listdir(r'C:\Users\Dan Helgeland\Downloads'):
    # for feilhåndtering ? 
    if not os.path.isfile(os.path.join(r'C:\Users\Dan Helgeland\Downloads', filename)):
        continue
    #tar nåværende totalSize og legger på størrelsen til alle filene funnet i for loopen. er i kB.
    totalSize= totalSize + os.path.getsize(os.path.join(r'C:\Users\Dan Helgeland\Downloads', filename))
    
print(totalSize)