import logging, os, time, openpyxl, datetime
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
runState = True
activeProject = input('Hvilket prosjekt jobbes på: ')
activeCell = ''
weekDayInt = 0
weekDayDict = {
    "0":    "Mandag",
    "1":    "Tirsdag",
    "2":    "Onsdag",
    "3":    "Torsdag",
    "4":    "Fredag",
    "5":    "Lørdag",
    "6":    "Søndag"
 }
weekDay = ''

def init():
    global weekDayInt
    global weekDayDict
    global weekDay
    weekDayInt = datetime.datetime.today().weekday()
    weekDay = weekDayDict[str(weekDayInt)]

#TODO search through timesheet to find correct column to write to, based on active project, todays date and if there data present.
#TODO if data is present, add accumulated time this session to that cell, if not, make new cell. 

def findCell(activeProject):
    for col in ws.iter_cols(min_row=0, max_col=1 ,max_row=10):
        logging.debug('active project: %s' % (activeProject))
        i = 0
        for cell in col:
            logging.debug('cell is: %s' % (cell))   
            logging.debug('cell value is: %s' % (cell.value))
            i +=1
            if str(cell.value) == activeProject:
                global activeCell
                activeCell = cell
                logging.info('Active cell is %s ' % (activeCell))
                break
            elif i == 10 and activeCell=='':
                logging.info('no project found, creating new row.')
                #findCell(1264)
                break
            
def timeCount(activeProject, timeFile):
    start = time.time()
    newActiveProject = ""
    userInput = ''
    while userInput == '':
        userInput = input('Tast inn nytt prosjekt nummer eller "stopp" for å avslutte: ')
    stop = time.time()
    activeProject = activeProject + (stop - start)
    print(activeCell)
    #except ValueError:
       # print('something fucky')

#def writeToExcel(activeProject, timeFile, date):


init()

while runState:
    if activeProject != '':
        findCell(activeProject)
        timeCount(activeProject, wb)  
        #break


#TODO skill mellom forskjellige timebærere



#TODO lagre total tid per dag og sorter til fil,
# alternativt mulighet for print direkte i konsoll. 

#TODO pakk hele driten til exe fil?


