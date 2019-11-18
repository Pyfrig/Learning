import logging, os, shelve, time, openpyxl
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s')
logging.debug('start of program')
#logging.disable(logging.DEBUG)

# make store folder as active.
os.chdir(r'c:\Users\Dan Helgeland\Documents\timeDocs')
#TODO function for previous made workbook
wb = openpyxl.load_workbook('timeSheet.xlsx') #TODO add number for previous file, count and use highest in folder?
ws = wb.active

#wb.save('example.xlsx')
#TODO add running number when saving example.xlsx to avoid fucking up file.
activeProject = 0


activeProject = input('Hvilket prosjekt jobbes på: ')
activeCell = ''
#TODO search through timesheet to find correct column to write to, based on active project, todays date and if there data present.
#TODO if data is present, add accumulated time this session to that cell, if not, make new cell. 
def findCell(activeProject, date):
    for col in ws.iter_cols(min_row=0, max_col=1 ,max_row=10):
        logging.debug('active project: %s' % (activeProject))
        for cell in col:
            logging.debug('cell is: %s' % (cell))   
            logging.debug('cell value is: %s' % (cell.value))   
            if cell.value == activeProject:

                activeCell = cell
                print (activeCell)
            else:
                logging.debug('no cell found')
runState = True

def timeCount(activeProject, timeFile):
    start = time.time()
    newActiveProject = ""
    while newActiveProject == '':
        newActiveProject = input('Tast inn nytt prosjekt: ')
        if newActiveProject in timeDict.keys():
            print("ja")
        else:
             print("nei")


    stop = time.time()
    timeDict['timeToday'] = timeDict['timeToday'] + (stop - start)
    print(timeDict['timeToday'])

while runState:
    if activeProject != '':
        #timeCount(activeProject, timeLog)
        findCell(activeProject,wb)
        break

#TODO skill mellom forskjellige timebærere



#TODO lagre total tid per dag og sorter til fil,
# alternativt mulighet for print direkte i konsoll. 

#TODO pakk hele driten til exe fil?


