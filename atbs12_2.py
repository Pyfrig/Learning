import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s')

logging.debug('start of program')
def factorial(n):
    total = 1
    logging.debug('for loop starting')
    for i in range (1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    return total
logging.debug('print function')
print(factorial(5))

logging.debug('end of program')