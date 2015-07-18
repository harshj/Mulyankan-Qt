# Module to evaluate results and save them to Result.xls 

import xlwt
import xlrd
import os
#from shutil import copy	#To make backup of results

from data import get_data
from result import get_result, analyze
from constants import(
                        PASSIVE_DATA_SIZE,
                        BOOKLET_CODE_SIZE,
                        NO_OF_QUES,
                      )

# questions: questions not to be evaluated.


def evaluate(response_path , key_path , questions = "" , NO_OF_QUESTIONS = NO_OF_QUES):
	errors = []
	questions = questions.split()
	for i in xrange(len(questions)):
		questions[i] = int(questions[i])
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Result')
	i = 0
	ws.write(i,0,'Roll No.')
	ws.write(i,1,'Correct')
	ws.write(i,2,'Incorrect')
	ws.write(i,3,'Missed')
	ws.write(i,4,'Invalid #')
	ws.write(i,5,'Marks Obtained')
	for j in xrange(NO_OF_QUESTIONS):
		ws.write( i,j + 6,'Q%d'%(j+1) )
	
	try:
		#path = SYS_ROOT + os.sep + 'system' + os.sep + 'data' + os.sep
		f = open (response_path)
	except IOError:
		errors.append("File not found error!!!")
		return errors

	for line in f :
	    i += 1
	    j = 5
	    data = line[ PASSIVE_DATA_SIZE : ]
	    roll_no , qpset , response = get_data(data)
	    if qpset != '*':
	    	correct , wrong , missed , invalid , score , stats = get_result(key_path ,qpset , NO_OF_QUESTIONS , response , questions)
	    	correct_qp = 1
	    else:
	    	correct = "Invalid question " 
	    	wrong = "paper set."
	    	missed = " Booklet code is "
	    	invalid = line[:BOOKLET_CODE_SIZE]
	    	score = ""
	    	correct_qp = 0
		
	    ws.write(i,0,roll_no)
	    ws.write(i,1,correct)
	    ws.write(i,2,wrong)
	    ws.write(i,3,missed)
	    ws.write(i,4,invalid)
	    ws.write(i , 5 , score)
		
		# Write stats only if the qpset is correct.
	    if correct_qp:
	    	for j in xrange(NO_OF_QUESTIONS):
	    		ws.write( i , j + 6 , stats[j] )
	f.close()
	
	#copy(path + "Result.xls" , path + "backup" + os.sep + "Result.bak")		#Make backup of previous result.
	wb.save("Result.xls")
	error = analyze()
	if error : 
	    for e in error:
	    	errors.append('AnalyzeError :' + e)
	return errors

#show function returns a list of list which contains all the data of Result.xls
#Not used in Qt version.
def show(n):
	path = SYS_ROOT + os.sep + 'system' + os.sep + 'data' + os.sep + 'Result.xls'
	errors = []
	if(os.path.exists(path)):
		wb = xlrd.open_workbook(path)
		sh = wb.sheet_by_index(n)
		data = []
		row = []
		for i in xrange(0,sh.nrows):
			for j in xrange(0,sh.ncols):
				temp  = sh.cell_value(i,j)				
				'''if i > 0 :
					temp = int(temp)		#Values read from excel sheets are in floating point.'''
				
				row.append(temp)
			data.append(row)
			row = []
		
		success = True
					
				
	else:
		data = []
		errors.append("File Not Found!!!")
		success = False
	
	return data,success,errors

