import datetime

#populated available services and required time foreach service
services={
	"installment":datetime.timedelta(minutes=30),
	"consultation":datetime.timedelta(minutes=20),
	"complaint":datetime.timedelta(minutes=40)
}

#populated customers
customers={
	1:{'name':'a','priority':0,'service':'installement'},
	2:{'name':'b','priority':1,'service':'installement'},
	3:{'name':'c','priority':0,'service':'installement'},
	4:{'name':'d','priority':1,'service':'consultation'},
	5:{'name':'e','priority':0,'service':'complaint'},
	6:{'name':'f','priority':1,'service':'consultation'},
	7:{'name':'g','priority':0,'service':'complaint'},
	8:{'name':'h','priority':0,'service':'consultation'},
	9:{'name':'i','priority':1,'service':'consultation'}
}

#create class Customer
class Customer :
	def __init__(self,customer,kedatangan):
		#construct variable for customer
		self.name=customer['name']
		self.priority=customer['priority']
		self.kedatangan=kedatangan
		self.service=customer['service']

class Loket:
	def __init__(self,loket,duration):
		#construct variable for loket
		self.antrian=[]
		self.cust=[]
		self.name=loket
		self.duration=duration

#adding customer into loket's queue
	def addQueue(self,customer):
		self.antrian.append([customer.kedatangan,customer.name,customer.priority])

#poping customer from queue using FIFO
	def processAntrian(self):
		#sort by priority
		self.antrian=sorted(self.antrian,key=lambda x:x[2])
		#sort by arrival for priority customer
		a=sorted([x for x in self.antrian if x[2]==1],key=lambda x:x[0],reverse=True)
		#sort by arrival for normal customer
		b=sorted([x for x in self.antrian if x[2]==0],key=lambda x:x[0],reverse=True)
		self.antrian=b+a
		#pop customer from queue
		self.antrian.pop()
		print(self.antrian)

#print customer name inside queue	
	def printAntrian(self):
		print('Antrian dalam loket : ',[x[1] for x in self.antrian][::-1])

#print waiting time for customer base on existing customer in queue
	def waktuTunggu(self,customer):
		#find customer position in queue
		a=[[i, el.index(customer)] for i, el in enumerate(self.antrian) if customer in el]
		#calculate waiting time
		print(self.duration*(len(self.antrian)-a[0][0]))

cust=[]
loket=[]

#create new customer
for i in customers.keys():
	cust.append(Customer(customers[i],i))

#create new loket
for x in services.keys():
	loket.append(Loket(x,services[x]))

#input customer to each loket
for x in loket:
	for y in cust:
		if x.name==y.service:
			x.addQueue(y)

#try each func in class loket
#pop using first in first out
loket[1].processAntrian()

#printing customer inside the queue
loket[1].printAntrian()

#search by using customer name who still inside the queue
loket[1].waktuTunggu('h')