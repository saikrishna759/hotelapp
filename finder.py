import os
import csv
import sqlite3

conn = sqlite3.connect("hosdb.db")
cursor = conn.cursor()


def main():
	f = open("C:\Book1.csv")
	reader = csv.reader(f)
	#for A, B in reader:
		#cursor.execute("insert into hospital(problem,loc) values(:problem, :loc)",{"problem":A , "loc":B})

	cursor.execute("select * from hospital")
	result = cursor.fetchall()
	for id,problem,loc in result:
		print("id:%d,problem:%s,loc:%s" %(id,problem,loc))
	conn.commit()
if __name__ == "__main__":
	main()
