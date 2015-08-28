# This file contains modules to handle/verify uploaded files

import os
import xlrd
from shutil import move,copy		# To create backup files.

		
#Module to handle centre info file 
def handle_centre_info(centre_info):
	errors = []

	temp_wb = xlrd.open_workbook(path + "Centre Information.xls")
	temp_sh = temp_wb.sheet_by_index(0)
	
	columns = []
	for i in xrange(temp_sh.ncols):
		columns.append( temp_sh.cell_value(0,i) )
	
	for i in ['Centre Code' , 'Centre Name' , 'Centre Address' , 'Capacity']:		#Check for all required columns
		if i not in columns:
			errors.append("Data Insufficient!!! " + i + " not found.")
			return errors
	return errors
	
# Module to handle student info file
def handle_student_info(student_info_path):
	errors = []
	
	temp_wb = xlrd.open_workbook(student_info_path)
	temp_sh = temp_wb.sheet_by_index(0)
	
	columns = []
	for i in xrange(temp_sh.ncols):
		columns.append( temp_sh.cell_value(0,i) )
	
	for i in ['Application #' , 'Name' , 'Gender', "Father's Name" , "Mother's Name" , 'Address' , 'Contact No.' , 'Program Code']:	#Check for all required columns.
		if i not in columns:
			errors.append("Data Insufficient!!! " + i + " not found.")
			return errors
		
	return errors
