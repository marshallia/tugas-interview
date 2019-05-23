import datetime
import pandas as pd

class Person:
	def __init__(self,person,transport):
		self.person=person
		self.transport=transport
		self.report=[]
		
	def main(self):
		for x in range(len(self.person['itternary'])):
			self.goTraining(x)
		

	def isSick(self,temp):
		if temp>37:
			return True
		else:
			return False

	def goTraining(self,x):
		
		date_time_obj = datetime.datetime.strptime(self.person['itternary'][x]['leave'], '%Y-%m-%d %H:%M:%S')
		if self.isSick(self.person['itternary'][x]['temp'])==True or date_time_obj.time()>datetime.time(7,0):
			self.report.append([self.person['name'],date_time_obj,date_time_obj+self.person['trainDuration']+self.transport['ojek']])
		elif date_time_obj.time()<datetime.time(6,0):
			self.report.append([self.person['name'],date_time_obj,date_time_obj+self.person['trainDuration']+self.transport['car']])
		elif date_time_obj.time()<datetime.time(7,0):
			self.report.append([self.person['name'],date_time_obj,date_time_obj+self.person['trainDuration']+self.transport['motorcycle']])
			
	def printTrainingHistory(self):
		df=pd.DataFrame(self.report,columns=['Name','Left Time','Arrived Time'])
		print(df)

	def resetTrainingHistory(self):
		del self.report[0:len(self.report)]

transport={
	"car":datetime.timedelta(minutes=30),
	"motorcycle":datetime.timedelta(minutes=20),
	"ojek":datetime.timedelta(minutes=15)
}

person={'name':'budi',
		'trainDuration':datetime.timedelta(hours=1),
		'itternary':{
		0:{'leave':'2018-03-01 05:35:00','temp':36},
		1:{'leave':'2018-03-01 06:40:00','temp':38},
		2:{'leave':'2018-03-03 06:30:00','temp':36},
		3:{'leave':'2018-03-04 07:15:00','temp':36}
		}}
	
p1=Person(person,transport)
p1.main()
p1.printTrainingHistory()
#p1.resetTrainingHistory()