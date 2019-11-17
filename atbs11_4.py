import os

# for x, y, z in er pga forventet retur av os.walk. se doc
for folderName, subFolders, fileNames in os.walk(r'D:\Google Drive\Prosjekter\Learning'):
        print('The folder is ' + folderName)
        print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
        print('The fileNames in ' +folderName + ' are: ' + str(fileNames))
        # tom print for å få linjeskift mellom iterasjonene av for loopen.
        print()

        #eventuelle nye for loops under her for videre arbeid med subfolders/filer
        #f.eks slette alle filer med spesielt navn, eller type.