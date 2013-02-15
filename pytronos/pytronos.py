#!/usr/bin/python

import Image, ImageDraw
import sys
import string
import ConfigManager
import random

class DrawMap:

	def __init__(self):		
		self.Cfg = ConfigManager.ConfigManager('pytronos.cfg')
		self.Map = Image.open(self.Cfg.getOption("MainMap"))
		
		if not self.Map:
			sys.stderr.write('ERROR: MainMap option is needed!\n')
			sys.exit(1)
			
		self.iconCount = {}

	def colorize(self,im,house,type=None):
		#Colorizing
		hextoChange = self.Cfg.getOption("ColorToChange")
		if not hextoChange:
			sys.stderr.write('ERROR: No color to change!, please define ColorToChange option\n')
			sys.exit(1)
			
		hexcolor = self.Cfg.getOption("Color"+house)
		if not hexcolor:
			err = "ERROR: No color defined for %s\n" %(house) 
			sys.stderr.write(err)
			sys.exit(1)
	
		hextoChangeFrom = self.Cfg.getOption("ColorToChangeFrom")
		if hextoChangeFrom:
			toChangeFrom = [0,0,0]
			toChangeFrom[0] = string.atoi('0x'+hextoChangeFrom[0:2],16)
			toChangeFrom[1] = string.atoi('0x'+hextoChangeFrom[2:4],16)
			toChangeFrom[2] = string.atoi('0x'+hextoChangeFrom[4:6],16)
		
		color = [0,0,0]
		color[0] = string.atoi('0x'+hexcolor[0:2],16)
		color[1] = string.atoi('0x'+hexcolor[2:4],16)
		color[2] = string.atoi('0x'+hexcolor[4:6],16)

		toChange = [0,0,0]
		toChange[0] = string.atoi('0x'+hextoChange[0:2],16)
		toChange[1] = string.atoi('0x'+hextoChange[2:4],16)
		toChange[2] = string.atoi('0x'+hextoChange[4:6],16)
	
	
		i = 0
		imseq = list(im.getdata())
		
		for pix in imseq:
			if hextoChangeFrom:
				b0 = toChangeFrom[0] <= pix[0] and pix[0] <= toChange[0]
				b1 = toChangeFrom[1] <= pix[1] and pix[1] <= toChange[1]
				b2 = toChangeFrom[2] <= pix[2] and pix[2] <= toChange[2]
			else:
				b0 = pix[0] == toChange[0]
				b1 = pix[1] == toChange[1]	
				b2 = pix[2] == toChange[2]
				
			if b0 and b1 and b2:
				newpix = (color[0],color[1],color[2])
				imseq[i] = newpix	
			i+=1
			
		im.putdata(imseq)
		#Resizing
		width = self.Cfg.getOption('Size'+type)
		if width:	
			width = int(width)
			im_size = im.size
			height = (width*im_size[1])//im_size[0]
			im = im.resize((width,height))
		
		return im
			
	def insertTroop(self,house,region,type,ntype):
		im_path = self.Cfg.getIcon(type)
		
		if not im_path:
			return False,'Icon path not found: %s%s\n' %(house,type)
		
		regionposs = self.Cfg.getTroop(region,ntype)
		
		if not regionposs:
			return False,'There is not free position for %s\n' %(region)
			
		poss = regionposs.split('x')		
		im = Image.open(im_path)
		icon = self.colorize(im,house,type)
		
		try:
			x = int(poss[0]) + self.iconCount[region] 
			y = int(poss[1]) + self.iconCount[region]
		except:
			x = int(poss[0])
			y = int(poss[1])
			self.iconCount[region] = 0

		self.iconCount[region] += 7
		self.Map.paste(icon,(x,y),icon) 

		return True,'None'

	def insertPower(self,house,region):
		im_path = self.Cfg.getIcon(house+"Power")
		
		if not im_path:
			return False,'Icon path not found: %s%s\n' %(house,type)
	
		regionposs = self.Cfg.getPower(region)
		
		if not regionposs:
			return False,'There is not free position for %s\n' %(region)
			
		poss = regionposs.split('x')		
		icon = Image.open(im_path)
		x = int(poss[0])
		y = int(poss[1])
		
		self.Map.paste(icon,(x,y),icon) 
		return True,'None'
	
	def insertOrder(self,region,type,mode):
		im_path = self.Cfg.getIcon(type+mode)
		
		if not im_path:
			return False,'Icon path not found: %s%s\n' %(type,mode)
	
		regionposs = self.Cfg.getOrder(region)
		
		if not regionposs:
			return False,'There is not free position for %s\n' %(region)
		
		poss = regionposs.split('x')		
		icon = Image.open(im_path)
		x = int(poss[0])
		y = int(poss[1])
		
		self.Map.paste(icon,(x,y),icon) 
		return True,'None'	
	
	def insertBarrel(self,house,num):
		im_path = self.Cfg.getIcon(house+'Barrel')
		
		if not im_path:
			return False,'Icon path not found: Barrel %s\n' %(house)
	
		poss = self.Cfg.getBarrel(num)
		if not poss:
			return False,'There is not position for barrel %s\n' %(num) 
	
		poss = poss.split('x')
		icon = Image.open(im_path)
		x = int(poss[0])
		y = int(poss[1])
		
		self.Map.paste(icon,(x,y),icon)
		return True,'None'
		
	def insertChip(self,region,name):
		im_path = self.Cfg.getIcon(name+"Chip")
		
		if not im_path:
			return False,'Chip path not found: %s\n' %(name)
	
		regionposs = self.Cfg.getChip(region)
		
		if not regionposs:
			return False,'There is not position for %s\n' %(region)
		
		poss = regionposs.split('x')		
		icon = Image.open(im_path)
		x = int(poss[0])
		y = int(poss[1])
		
		self.Map.paste(icon,(x,y),icon)
		return True,'None'	
		
	def insertAll(self):
		army = ["Soldier", "Horse"]
		houses = ["Lannister", "Tyrell", "Tully", "Stark",\
				"Targaryen", "Arryn", "Martell", "Baratheon", "Greyjoy"]
		seas = ["BayOfIce", "TheShimeringSea", "BlazewaterBay", "TheBitf"]		
		movs = ["Defense", "March", "Consolide", "March", "Raid"]
		
		for s in seas:
			#house = houses[random.randint(0,8)]
			house = "Targaryen"
			poss = self.Cfg.getTroop(s,1)
			if poss:
				self.Cfg.delTroop(s)
				poss = poss.split('x')
				im_path = self.Cfg.getIcon("Boat")
				if im_path:
					house = houses[random.randint(0,8)]
					icon = Image.open(im_path)
					icon = self.colorize(icon,house,"Boat")
					x = int(poss[0])
					y = int(poss[1])
					number = random.randint(1,3)
					for n in range(1,number+1):
						x+=10
						y+=10
						self.Map.paste(icon,(x,y),icon)
					 
		troops,powers,orders = self.Cfg.getAllPoss()
		
		for region in troops:
			house = houses[random.randint(0,8)]
			fort = False
			siege = False
			soldier = False
			horse = False
			
			for t in region:
				#Inserting fort
				if not fort:
					typename = "Fort"
					im_path = self.Cfg.getIcon(typename)
					icon = Image.open(im_path)
					icon = self.colorize(icon,house,typename)
					poss = t.split('x')
					x = int(poss[0]) 
					y = int(poss[1])
					self.Map.paste(icon,(x,y),icon)
					fort = True
					
				#inserting Siege	
				elif not siege:
					typename = "Siege"
					im_path = self.Cfg.getIcon(typename)
					icon = Image.open(im_path)
					icon = self.colorize(icon,house,typename)
					poss = t.split('x')
					x = int(poss[0]) 
					y = int(poss[1])
					self.Map.paste(icon,(x,y),icon)
					siege = True	
					
				#inserting horse and soldier in the rest of regions
				else:
					if not horse:
						typename = "Horse"
						horse = True
						soldier = False
						
					elif not soldier:	
						typename = "Soldier"
						soldier = True
						horse = False
						
					im_path = self.Cfg.getIcon(typename)
					icon = Image.open(im_path)
					icon = self.colorize(icon,house,typename)
					poss = t.split('x')
					x = int(poss[0]) 
					y = int(poss[1]) 
			
					number = random.randint(1,2)
					for n in range(0,number):
						self.Map.paste(icon,(x,y),icon) 
						x+=7
						y+=7	
				
				
		for p in powers:
			house = houses[random.randint(0,8)]
			im_path = self.Cfg.getIcon(house+"Power")
			if im_path:	
				icon = Image.open(im_path)
				poss = p.split('x')
				x = int(poss[0])
				y = int(poss[1])	
				self.Map.paste(icon,(x,y),icon)
		
		for o in orders:
			m = movs[random.randint(0,4)]
			if m == "Consolide" or m == "Raid":
				modes = ["1s","0s"]
			elif m == "Defense":
				modes = ["p1","p2","p3"]
			elif m == "March" or m == "Support":
				modes = ["m1","p0","p1","p2"]
				
			mode = modes[random.randint(0,len(modes)-1)]
			im_path = self.Cfg.getIcon(m+mode)
			if im_path:	
				icon = Image.open(im_path)
				poss = o.split('x')
				x = int(poss[0])
				y = int(poss[1])	
				self.Map.paste(icon,(x,y),icon)				
			
		for i in range(0,9):
			house = houses[i]
			num = random.randint(0,8)
			self.insertBarrel(house,num)	
			
	def getMap(self):
		return self.Map	


types = {"Soldier":1, "Horse":2, "Fort":3,\
		"Siege":4, "Dragon":5, "Boat":6, \
		"Archer":7, "Direwolf":8, "Sperman":9,
		"Mercenary":10, "Bastion":11, "Barcoluengo":12,
		"Clanman":13}
dm = DrawMap()

opt = raw_input().strip().split()
if len(opt) == 0:
		opt.append("NoOption")
		
while opt[0] != 'exit':
	
	if opt[0] == "troop":
		if len(opt) != 5:
			sys.stderr.write('WARNING: invalid number of parameters\n')
		else:
			house = opt[1]
			region = opt[2]
			num = opt[4]
			type = opt[3]
			
			if type in types:
				ntype = types[type]
				
				for n in range(0,int(num)):
					ok,errno = dm.insertTroop(house,region,type,ntype)
					if not ok:
						err = "ERROR: cannot insert troop: %s %s %s\n" %(house,region,type)
						sys.stderr.write(err)	
						sys.stderr.write(errno)
						break	
			else:
				err = "WARNING: invalid type %s\n" %(type)	
				sys.stderr.write(err) 
	
	elif opt[0] == "power":
		if len(opt) != 3:
			sys.stderr.write('WARNING: invalid number of parameters\n')
		
		else:
			house = opt[1]
			region = opt[2]	
			ok,errno = 	dm.insertPower(house,region)
			if not ok:
				err = "ERROR: cannot insert power: %s %s %s\n" %(house,region,type)
				sys.stderr.write(err)	
				sys.stderr.write(errno)
				break
	
		
	elif opt[0] == "order":
		if len(opt) != 4:
			sys.stderr.write('WARNING: invalid number of parameters\n')
		
		else:
			type = opt[2]
			mode = opt[3]
			region = opt[1]	
			retval,reterr = dm.insertOrder(region,type,mode)	
			
			if not retval:
				err = "ERROR: cannot insert order: %s %s %s\n" %(region,type,mode)
				sys.stderr.write(err)	
				sys.stderr.write(reterr)
				break
	
	elif opt[0] == "barrel":
		if len(opt) != 3:
			sys.stderr.write('WARNING: invalid number of parameters\n')			
		
		else:
			house = opt[1] 
			num = opt[2]
			retval,reterr = dm.insertBarrel(house,num)
			if not retval:
				sys.stderr.write(reterr)
					
	elif opt[0] == "chip":
		if len(opt) != 3:
			sys.stderr.write('WARNING: invalid number of parameters\n')
			
		else:
			name = opt[1]
			point = opt[2]
			retval,reterr = dm.insertChip(point,name)
			if not retval:
				sys.stderr.write(reterr)
						
	elif opt[0] == "printall":
		dm.insertAll()	


	elif opt[0] == "write":
		if len(opt) != 2:
			sys.stderr.write('WARNING: invalid number of parameters\n')
			
		else:
			map = dm.getMap()
			map.save(opt[1], "JPEG")
	else:
		err = "ERROR: invalid option %s\n" %(opt[0])
		sys.stderr.write(err) 
				
	opt = raw_input().strip().split()
	if len(opt) == 0:
		opt.append("NoOption")

#map = dm.getMap()
#map.save("/home/hitz/image.jpeg", "JPEG")

#Mapa = Image.open("images/MapaBase.png")
#horse = Image.open("images/horse_tully.png")
#soldier = Image.open("images/soldier.png")

#draw = ImageDraw.Draw(Mapa)

#x = im.size[0]/2
#y = im.size[1]/2

#draw.ellipse((128,128,400,400), fill='#FFFFFF')

#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
#del draw 

#Mapa.paste(horse, (528,1440),horse)
#Mapa.paste(soldier, (271,1485),soldier)
#Mapa.paste(horse, (535,1447),horse)

# write to stdout
#Mapa.save(sys.stdout, "PNG")


