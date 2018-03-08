#The purpose of this code is to 
# Read input from whatsapp chat
# Parse the debate transcript into the following fields:
# 1. Sentence No. 2. Paragraph No. 3. Speaker 4. Conversation Text

import csv
from os import path
from transcript import *
import glob

#if you want all .txt files to .csv files in same directory
def parse_whatsapp():
    if len(sys.argv)!=1:
        print ("Run: python parse_whatsapp.py")
        sys.exit(1)
    files_list=glob.glob("/home/subhendu/Documents/subhendu/project_automation_whatsapp/member_left/generate_all_txt_to_csv_generator/*.txt") 
    files=[]
    for i in files_list:
	    st=i.replace("/home/subhendu/Documents/subhendu/project_automation_whatsapp/member_left/generate_all_txt_to_csv_generator/","")
	    st=(st.lstrip()).rstrip()
	    files.append(st)
    for file_var in files:
		output=file_var.replace(".txt",".csv")
		c = Transcript(file_var, output)
		c.open_file()
		c.feed_lists()
		c.write_transcript()
		data = pd.read_csv(output)

if __name__ == "__main__":
    parse_whatsapp()
   	