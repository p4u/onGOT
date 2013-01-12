import string
import sys
import os

class ConfigManager:
	def __init__(self,file):
		self.options = {}
		self.MapContainer = MapManager()
		self.icons = {}
		self.__readConfig(file)
		
	def __readConfig(self,file):
		fd = open(file,'r')
		options = {}
		ln = fd.readline()
		op = ""
		
		while ln != "":
			
			ln = ln.strip() #Clear before/after spaces
			
			if len(ln) > 0 and ln[0] != '#':
				if ln[0] == '[':
					if ln.find("OPTIONS") >= 0:
						op = "OP"
					elif ln.find("ICONS") >= 0:
						op = "IC"
					elif ln.find("MAP") >= 0:
						op = "MP"
					else:
						err = "WARNING: in config file, %s not recognized\n" %(ln)
						sys.stderr.write(err) 
								
				else:
					lnsplited = ln.split()
						
					if op == "OP" and len(lnsplited) > 1:
						self.options[lnsplited[0]] = lnsplited[1]
					
					elif op == "IC" and len(lnsplited) > 1:
						self.icons[lnsplited[0]] = lnsplited[1]
					
					elif op == "MP" and len(lnsplited) > 1:					
						if lnsplited[0] == "Troop":	
							name = lnsplited[1]
							for i in range(2,len(lnsplited)):
								poss = lnsplited[i]
								self.MapContainer.addTroop(name,poss)
								
						elif lnsplited[0] == "Power":	
							name = lnsplited[1]
							poss = lnsplited[2]
							self.MapContainer.addPower(name,poss)		
						
						elif lnsplited[0] == "Order":	
							name = lnsplited[1]
							poss = lnsplited[2]
							self.MapContainer.addOrder(name,poss)
						
						elif lnsplited[0] == "Barrel":
							number = lnsplited[1]
							poss = lnsplited[2]
							self.MapContainer.addBarrel(int(number),poss)	
						
						elif lnsplited[0] == "Chip":
							name = lnsplited[1]
							poss = lnsplited[2]
							self.MapContainer.addChip(name,poss)
							
						else:
							err = "WARNING: in config file, [MAP]->%s not recognized\n" %(lnsplited[0])	
							sys.stderr.write(err) 
							
			ln = fd.readline()
		
		#self.MapContainer.debugPrintAll() #DEBUG
		
	def getOption(self,name):
		if name in self.options:
			ret = self.options[name]
		else:
			ret = False
		return ret		

	def getIcon(self,name):
		if name in self.icons:
			ret = self.icons[name]
		else:
			ret = False
		return ret
		
	def getTroop(self,name,type):
		return self.MapContainer.getTroop(name,type)
	
	def getPower(self,name):
		return self.MapContainer.getPower(name)			

	def getOrder(self,name):
		return self.MapContainer.getOrder(name)
		
	def getAllPoss(self):
		return self.MapContainer.getAll()	
	
	def delTroop(self,name):
		return self.MapContainer.delTroop(name)
	
	def getChip(self,name):
		return self.MapContainer.getChip(name)
	
	def getBarrel(self,num):
		hsep = self.getOption("BarrelSeparationH")
		vsep = self.getOption("BarrelSeparationV")

		if not hsep or not vsep:
			sys.stderr.write("ERROR: Is needed to specify BarrelSeparation[H/V] option\n")
			ret = False
		else:
			ret = self.MapContainer.getBarrel(int(num),int(hsep),int(vsep))
			
		return ret	
					
class MapManager:	
		def __init__(self):
			self.troop = {}
			self.power = {}
			self.order = {}
			self.barrel = [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]
			self.chip = {}
			
		def debugPrintAll(self):
			print "\nTROOPS\n"
			print self.troop
			print "\nPOWER\n"
			print self.power
			print "\nORDER\n"
			print self.order
			print "\nBARREL\n"
			print self.barrel
			
		def addTroop(self,name,poss):
			if name in self.troop:
				self.troop[name].append([0,poss])
			else:
				self.troop[name] = [[0,poss]]
				
		def addPower(self,name,poss):
			if not name in self.power:
				self.power[name] = poss
				ret = True
			else:
				ret = False
			return ret
		
		def addOrder(self,name,poss):
			if not name in self.order:
				self.order[name] = poss
				ret = True
			else:
				ret = False	
			return ret
		
		def addChip(self,name,poss):
			if not name in self.chip:
				self.chip[name] = poss
				ret = True
			else:
				ret = False	
			return ret
		
		def addBarrel(self,num,poss):
			if num < 0 or num > 8:
				err = "ERROR: invalid barrel index "+ str(num)+ "\n"	
				sys.stderr.write(err)
				ret = False
				 
			else:
				self.barrel[num][0] = poss
				self.barrel[num][1] = 1
				ret = True
				
			return ret
			
		def delTroop(self,name):
			if name in self.troop:
				del self.troop[name]
				ret = True
			else:
				ret = False
			return ret
				
		def getTroop(self,name,type):
			ret = False
			if name in self.troop and type != 0:
				isThere = False
				
				
				for i in range(0,len(self.troop[name])): 
					if self.troop[name][i][0] == type:
						ret = self.troop[name][i][1]
						isThere = True
						break
						
				if not isThere:			
					for i in range(0,len(self.troop[name])):
						if self.troop[name][i][0] == 0:
							self.troop[name][i][0] = type
							ret = self.troop[name][i][1]
							isThere = True
							break
			return ret		

		def getPower(self,name):
			if name in self.power:
				ret = self.power[name]
			else:
				ret = False
			return ret
			
		def getOrder(self,name):
			if name in self.order:
				ret = self.order[name]
			else:
				ret = False
			return ret
			
		def getChip(self,name):
			if name in self.chip:
				ret = self.chip[name]
			else:
				ret = False
			return ret	
			
		def getBarrel(self,num,hsep,vsep):	
			if num < 0 or num > 8:
				err = "ERROR: invalid barrel index "+ str(num)+ "\n"	
				sys.stderr.write(err)
				ret = False
				 
			else:
				
				if self.barrel[num][0] == 0:
					err = "ERROR: no barrel possition for "+ str(num)+ "\n"
					sys.stderr.write(err)
					ret = False
				
				else:	
					pos = self.barrel[num][0].split('x')
					x = int(pos[0])
					y = int(pos[1])
					n = self.barrel[num][1]
				
					if n > 4: 
						x += hsep 
						y += vsep*(n-4)
					else:
						y += vsep*(n)
						 
					n += 1
					self.barrel[num][1] = n
					ret = str(x) + 'x' + str(y)	
				
			return ret	
						
		def getAll(self):
			troops=[]
			orders=[]
			powers=[]
			barrel=[]
			
			i=0
			for t in self.troop:
				troops.append([])
				for p in self.troop[t]:
					troops[i].append(p[1])
				i+=1	
					
			for p in self.power:
				powers.append(self.power[p])	
				
			for o in self.order:
				orders.append(self.order[o])
					
			return troops,powers,orders	
			
			
			
