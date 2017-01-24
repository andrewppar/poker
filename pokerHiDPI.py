import Tkinter
from Canvas import *
import random
from sets import Set
CARDWIDTH = 300
CARDHEIGHT = 450
python_green = "#476042"
VALS = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
VALDICT = {'A': 14,'K' : 13,'Q':12,'J':11,'10':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

##  #33B5E5
def pair(hand):
	pair = False
	for x in hand:
		for y in hand:
			if x != y and x.value == y.value:
				pair = True
	return pair

def twopair(hand):
	twopair = False
	pairs = Set([])
	for x in hand:
		for y in hand:
			if x != y and x.value == y.value:
				pairs.add(x)
				pairs.add(y)
	if len(pairs) >= 4:
		twopair = True
	return twopair

def threeofakind(hand):
	three = False
	for x in hand:
		for y in hand:
			for z in hand:
				if x !=y and x != z and y!= z and x.value == y.value and x.value == z.value:
					three = True
	return three

def flush(hand):
	flush = True
	for x in hand:
		for y in hand:
			if x.suit != y.suit:
				flush = False
	return flush

def fourofakind(hand):
	four = False
	for x in hand:
		for y in hand:
			for z in hand:
				for w in hand:
					if x!=y and x!=z and x!=w and y!=z and y!=w and z!=w and x.value == y.value and y.value == z.value and z.value == w.value:
						four = True
	return four

def fullhouse(hand):
	dct = {}
	for x in VALS:
		dct[x] = 0
	for x in hand:
		dct[x.value] = dct[x.value] +1
	three = False
	for x in dct.keys():
		if dct[x] == 3:
			three = True
	two = False
	for x in dct.keys():
		if dct[x] == 2:
			two = True
	return two and three

def straight(hand):
	straight = False
	a = []
	for x in hand:
		a.append(VALDICT[x.value])
	b = sorted(a)
	patterns = []
	for x in b:
		if x + len(b) < 15:
			c = []
			for y in range(len(b)):
				c.append(x+y)
			d = sorted(c)
			patterns.append(d)
		else:
			e = []
			for y in range(len(b)):

				if x + y < 15:
					e.append(x+y)
				else:
					f = ((x+y) - 15)+2
					e.append(f)

			patterns.append(e)
	for x in patterns:
		if x == b:
			straight = True
	return straight

def straightflush(hand):
	return straight(hand) and flush(hand)

def score(hand):
	score = 0
	if straightflush(hand) ==True:
		score = 8
	elif fourofakind(hand) == True:
		score = 7
	elif fullhouse(hand) == True:
		score = 6
	elif flush(hand) == True:
		score = 5
	elif straight(hand) == True:
		score = 4
	elif threeofakind(hand) == True:
		score = 3
	elif twopair(hand) == True:
		score = 2
	elif pair(hand) == True:
		score = 1
	return score


def printhand(hand):
	if score(hand) == 0:
		return 'Lose'
	elif score(hand) == 1:
		return 'Pair'
	elif score(hand) == 2:
		return 'Two Pair'
	elif score(hand) == 3:
		return 'Three of a Kind'
	elif score(hand) == 4:
		return 'Stright'
	elif score(hand) == 5:
		return 'Flush'
	elif score(hand) == 6:
		return 'Full House'
	elif score(hand) == 7:
		return 'Four of a Kind'
	elif score(hand) == 8:
		return 'Stright Flush'

def win(phand,ohand):
	if score(phand) > score(ohand):
		return phand
	elif score(phand) < score(ohand):
		return ohand
	else:
		if score(phand) in [8,6,5,4,0]:
			return draws(phand, ohand)
		elif score(phand) == 7:
			return drawfour(phand,ohand)
		elif score(phand) in [3,1]:
			return drawpairthree(phand,ohand)
		elif score(phand) == 2:
			return drawtwopair(phand,ohand)

def draws(phand,ohand):
	pvals = []
	for x in phand:
		pvals.append(VALDICT[x.value])
		pvals = sorted(pvals)
	ovals = []
	for y in ohand:
		ovals.append(VALDICT[y.value])
		ovals = sorted(ovals)
	order = range(len(pvals))
	b = order[::-1]

	win = ''

	for x in b:
		if pvals[x] > ovals[x]:
			return phand
		elif ovals[x] > pvals[x]:
			return ohand
	else:
		return 'Draw'

def drawfour(phand,ohand):
	phigh = 0
	for x in phand:
		for y in phand:
			if x!= y and x.value == y.value:
				phigh = VALDICT[x.value]
	ohigh = 0
	for x in ohand:
		for y in ohand:
			if x!= y and x.value == y.value:
				ohigh = VALDICT[x.value]
	if ohigh > phigh:
		return ohand
	else:
		return phand

def drawpairthree(phand,ohand):
	ppairhigh = 0
	for x in phand:
		for y in phand:
			if x!= y and x.value == y.value:
				phigh = VALDICT[x.value]
	opairhigh = 0
	for x in ohand:
		for y in ohand:
			if x!= y and x.value == y.value:
				ohigh = VALDICT[x.value]
	if ppairhigh > opairhigh:
		return phand
	elif opairhigh > ppairhigh:
		return ohand
	else:
		return draws(phand,ohand)

def drawtwopair(phand,ohand):
	ppairs = Set([])
	for x in phand:
		for y in phand:
			if x != y and x.value == y.value:
				ppairs.add(x)
				ppairs.add(y)
	opairs = Set([])
	for x in ohand:
		for y in ohand:
			if x != y and x.value == y.value:
				opairs.add(x)
				opairs.add(y)
	if max(ppairs) > max(opairs):
		return phand
	elif max(opairs) > max(ppairs):
		return ohand
	else:
		if min(ppairs) > min(opairs):
			return phand
		elif min(opairs)>min(ppairs):
			return ohand
		else:
			return draws(phand,ohand)
class Card:
	def __init__(self, suit, value,opens):
		self.suit = suit
		self.value = value
		self.opens = opens



class Player:
	def __init__(self, hand,money):
		self.hand = hand
		self.money = money

class Place:
	def __init__(self,x,y,canvas,card,flips):
		self.x = x
		self.y = y
		self.canvas = canvas
		self.card = card
		self.group = Group(self.canvas)
		self.group.bind('<Button-1>',self.flipcardclick)
		self.flips = flips

		if self.card.opens == True:
			self.showface()
		elif self.card.opens == False:
			self.showback()


	def diamond(self, x, y, outline = 'red', fill = 'white'):
		l1=self.canvas.create_line(x, y - 30, x -30, y, fill = 'red')
		l2=self.canvas.create_line(x -30, y, x, y+30, fill = 'red')
		l3=self.canvas.create_line(x,y+30, x+30, y, fill = 'red')
		l4=self.canvas.create_line(x+30,y, x, y-30, fill = 'red')
		for x in [l1,l2,l3,l4]:
			self.group.addtag_withtag(x)
	def heart(self, x, y, outline = 'red', fill = 'white'):
		l1=self.canvas.create_arc(x-30,y+15, x+3, y-30, fill = 'white', outline = 'red',style='arc', start = 50, extent = 155)
		l2=self.canvas.create_line(x -30, y, x, y+30, fill = 'red')
		l3=self.canvas.create_line(x,y+30, x+30, y, fill = 'red')
		l4=self.canvas.create_arc(x-3,y+15, x+30, y-30, fill = 'white', outline = 'red',style='arc', start = -15, extent = 155)
		for x in [l1,l2,l3,l4]:
			self.group.addtag_withtag(x)

	def clubs(self, x, y, outline = 'black', fill = 'white'):
		l1=self.canvas.create_arc(x-21,y-21, x+9, y, fill = 'white', outline = 'black',style='arc', start = 90, extent = 180)
		l2=self.canvas.create_arc(x-9,y-12, x+9, y-40, fill = 'white', outline = 'black',style='arc', start = 0, extent = 200)
		l3=self.canvas.create_arc(x,y-21, x+21, y, fill = 'white', outline = 'black',style='arc', start = -100, extent = 210)
		l4=self.canvas.create_rectangle(x-6,y, x+6,y+9)
		for x in [l1,l2,l3,l4]:
			self.group.addtag_withtag(x)
	def spade(self, x, y, fill = 'white'):
		l1=self.canvas.create_arc(x-30,y+15, x+3, y-30, fill = 'white',style='arc', start = 200, extent = 145)
		l2=self.canvas.create_line(x +30, y, x, y-30, fill = 'black')
		l3=self.canvas.create_line(x,y-30, x-30, y, fill = 'black')
		l4=self.canvas.create_arc(x-3,y+15, x+30, y-30, fill = 'white',style='arc', start = 200, extent = 140)
		l5=self.canvas.create_rectangle(x-3,y-3,  x+3, y+30)
		for x in [l1,l2,l3,l4,l5]:
			self.group.addtag_withtag(x)

	def flipcard(self):
		if self.card.opens == False:
			self.card.opens = True
			self.canvas.delete(self.group)
			self.showface()
		elif self.card.opens == True:
			self.card.opens = False
			self.canvas.delete(self.group)
			self.showback()

	def flipcardclick(self,event):
		if self.card.suit == '' or self.flips == False:
			return
		else:
			if self.card.opens == False:
				self.card.opens = True
				self.canvas.delete(self.group)
				self.showface()
			elif self.card.opens == True:
				self.card.opens = False
				self.canvas.delete(self.group)
				self.showback()

	def showface(self):
		if self.card.suit == '':
			self.canvas.create_rectangle(self.x,self.y,self.x+CARDWIDTH,self.y+CARDHEIGHT,fill = 'gray')
		else:
			points = [int(self.x), int(self.y)]
			points.append(int(self.x)+CARDWIDTH)
			points.append(int(self.y)+CARDHEIGHT)
			color = 'blue'
			if self.card.suit in ['D','H']:
				color = 'red'
			elif self.card.suit in ['C','S']:
				color = 'black'
			rect = self.canvas.create_rectangle(points, outline = 'black',fill = 'white')
			t1 = self.canvas.create_text(self.x + 30, self.y + 30, text = self.card.value,font=('Helvetica',13), fill = color)
			t2= self.canvas.create_text(points[2] - 30, points[3] - 30, text = self.card.value, font=('Helvetica',13),fill = color)
			for x in [rect,t1,t2]:
				self.group.addtag_withtag(x)
			center_x = points[0] + ((points[2] - points[0])//2)
			center_y = points[1] + ((points[3] - points[1])//2)
			if self.card.suit == 'H':
				self.heart(center_x, center_y)
			elif self.card.suit == 'D':
				self.diamond( center_x, center_y)
			elif self.card.suit == 'S':
				self.spade( center_x, center_y)
			elif self.card.suit == 'C':
				self.clubs( center_x, center_y)

	def showback(self):
		points = [int(self.x),int(self.y)]
		points.append(int(self.x) + CARDWIDTH)
		points.append(int(self.y) + CARDHEIGHT)

		rect1 = self.canvas.create_rectangle(points,fill = 'blue')
		center_x = points[0] + ((points[2] - points[0])//2)
		center_y = points[1] + ((points[3] - points[1])//2)
		text1 = self.canvas.create_text(center_x,center_y,font=('Helvetica',13),text = 'Q-Cards')
		for x in [rect1,text1]:
			self.group.addtag_withtag(x)

emptycard = Card('','',True)



def distance(number):
	return (number*330)+30

class Instrcut(Tkinter.Toplevel):
	def __init__(self,parent):
		Tkinter.Toplevel.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		frame = Tkinter.Frame(self)
		frame.pack()
		self.label = Tkinter.Message(frame ,font=("Helvetica",13), text = '''To play the game first place a bet. The options are to 5, 10, 20, 50, and 100. You begin with 200. After a bet has been placed, you can select the cards to discard. Clicking on a card will flip it over, marking it to be discarded. Once the cards to be discarded have been selected, press the Draw button. This will discard the flipped cards and replace them with cards from the deck. The money that is won depends on the multiplier that is associated with the hand. Check the Hand Ranks in the Instructions Menu. ''')
		self.label.pack()

class HighScore(Tkinter.Toplevel):
	def __init__(self,parent):
		Tkinter.Toplevel.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		f = open('highscore','r')

		frame = Tkinter.Frame(self)
		frame.pack()
		self.label = Tkinter.Label(frame,font=("Helvetica",13), text = 'High Score: ' + str(f.read()) )
		self.label.pack()
		f.close()

class Hands(Tkinter.Toplevel):
	def __init__(self,parent):
		Tkinter.Toplevel.__init__(self,parent)
		self.parent  = parent
		self.initialize()

	def initialize(self):
		# Create a container
		frame = Tkinter.Frame(self)
		scrollbar = Tkinter.Scrollbar(self)
		self.canvas = Canvas(self, width = 2100, height = 2250, bg = python_green, yscrollcommand=scrollbar.set)

		self.canvas.config(scrollregion=(0,0,900, 3900))
		scrollbar.config(command=self.canvas.yview)

		scrollbar.pack(side='right', fill='y')
		self.canvas.pack(side = 'left',expand='yes', fill='both')
		scrollbar.bind('<MouseWheel>',self.scroll)
		h1c1 = Place(distance(0), 30,self.canvas, Card('H','A', True),False)
		h1c2 = Place(distance(1), 30,self.canvas, Card('H','K', True),False)
		h1c3 = Place(distance(2), 30,self.canvas, Card('H','Q', True),False)
		h1c4 = Place(distance(3), 30,self.canvas, Card('H','J', True),False)
		h1c5 = Place(distance(4), 30,self.canvas, Card('H','10', True),False)

		h1text = self.canvas.create_text(distance(5)+200,255, font =('Purisa',17), text = 'Straight Flush')

		h2c1 = Place(distance(0), 510 , self.canvas, Card('H','K',True), False)
		h2c2 = Place(distance(1), 510 , self.canvas, Card('C','K',True), False)
		h2c3 = Place(distance(2), 510 , self.canvas, Card('D','K',True), False)
		h2c4 = Place(distance(3), 510 , self.canvas, Card('S','K',True), False)
		h2c5 = Place(distance(4), 510 , self.canvas, Card('H','3',True), False)

		h2text = self.canvas.create_text(distance(5)+200,735, font =('Purisa',17), text = 'Four of a Kind')

		h3c1 = Place(distance(0), 990,self.canvas, Card('H','2',True), False)
		h3c2 = Place(distance(1), 990,self.canvas, Card('D','2',True), False)
		h3c3 = Place(distance(2), 990,self.canvas, Card('S','2',True), False)
		h3c4 = Place(distance(3), 990,self.canvas, Card('C','J',True), False)
		h3c5 = Place(distance(4), 990,self.canvas, Card('H','J',True), False)

		h3text = self.canvas.create_text(distance(5)+200, 1215, font =('Purisa',17), text = 'Full House')

		h4c1 = Place(distance(0), 1470, self.canvas, Card('C', '3', True), False)
		h4c2 = Place(distance(1), 1470, self.canvas, Card('C', 'K', True), False)
		h4c3 = Place(distance(2), 1470, self.canvas, Card('C', '10', True), False)
		h4c4 = Place(distance(3), 1470, self.canvas, Card('C', '8', True), False)
		h4c5 = Place(distance(4), 1470, self.canvas, Card('C', '4', True), False)

		h4text = self.canvas.create_text(distance(5)+200, 1695, font =('Purisa',17), text = 'Flush')

		h5c1 = Place(distance(0), 1950, self.canvas, Card('H','4',True), False)
		h5c2 = Place(distance(1), 1950, self.canvas, Card('S','5',True), False)
		h5c3 = Place(distance(2), 1950, self.canvas, Card('H','6',True), False)
		h5c4 = Place(distance(3), 1950, self.canvas, Card('C','7',True), False)
		h5c5 = Place(distance(4), 1950, self.canvas, Card('C','8',True), False)

		h5text = self.canvas.create_text(distance(5)+200, 2175, font =('Purisa',17), text = 'Straight')

		h6c1 = Place(distance(0), 2430, self.canvas, Card('D','7',True), False)
		h6c2 = Place(distance(1), 2430, self.canvas, Card('H','7',True), False)
		h6c3 = Place(distance(2), 2430, self.canvas, Card('C','7',True), False)
		h6c4 = Place(distance(3), 2430, self.canvas, Card('D','J',True), False)
		h6c5 = Place(distance(4), 2430, self.canvas, Card('S','3',True), False)

		h6text = self.canvas.create_text(distance(5)+200, 2655, font =('Purisa',17), text = 'Three of a Kind')

		h7c1 = Place(distance(0), 2910, self.canvas, Card('S','4',True), False)
		h7c2 = Place(distance(1), 2910, self.canvas, Card('D','4',True), False)
		h7c3 = Place(distance(2), 2910, self.canvas, Card('H','2',True), False)
		h7c4 = Place(distance(3), 2910, self.canvas, Card('H','Q',True), False)
		h7c5 = Place(distance(4), 2910, self.canvas, Card('C','Q',True), False)

		h7text = self.canvas.create_text(distance(5)+200, 3135, font =('Purisa',17), text = 'Two Pair')

		h8c1 = Place(distance(0), 3390, self.canvas,  Card('D','9',True), False)
		h8c2 = Place(distance(1), 3390, self.canvas,  Card('C','9',True), False)
		h8c3 = Place(distance(2), 3390, self.canvas,  Card('S','4',True), False)
		h8c4 = Place(distance(3), 3390, self.canvas,  Card('D','J',True), False)
		h8c5 = Place(distance(4), 3390, self.canvas,  Card('H','A',True), False)

		h7text = self.canvas.create_text(distance(5)+200, 3615, font =('Purisa',17), text = 'Pair')

		for x in [h1c1,h1c2,h1c3,h1c4,h1c5,h2c1,h2c2,h2c3,h2c4,h2c5,h3c1,h3c2,h3c3,h3c4,h3c5,h4c1,h4c2,h4c3,h4c4,h4c5,h5c1,h5c2,h5c3,h5c4,h5c5,h6c1,h6c2,h6c3,h6c4,h6c5,h7c1,h7c2,h7c3,h7c4,h7c5]:
			x.showface()

	def scroll(self,event):
		self.canvas.yview_scroll(-1*(event.delta/120), "units")


class Menubar(Tkinter.Menu):
	def __init__(self,parent):
		Tkinter.Menu.__init__(self,parent)

		instructionMenu = Tkinter.Menu(self, tearoff= False)
		self.add_cascade(label = 'Instructions', menu = instructionMenu, font=('Helvetica',13))
		instructionMenu.add_command(label = 'Hand Ranks',font=('Helvetica',13), command = self.ranking)
		instructionMenu.add_command(label = 'Instructions', font=('Helvetica',13),command = self.instruct)
		instructionMenu.add_command(label = 'High Score', font=('Helvetica',13),command = self.high)

	def high(self):
		toplevel = HighScore(None)
	def ranking(self):
		toplevel = Hands(None)

	def instruct(self):
		toplevel = Instrcut(None)


class App(Tkinter.Tk):
	def __init__(self,parent,player):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.player = player
		self.deck = []
		self.initialize()

	def initialize(self):
		menubar = Menubar(self)
		self.config(menu= menubar)
		self.canvas = Canvas(self, width = 2300, height = 1500, bg = python_green)
		self.canvas.pack(expand = True, fill = 'both' )
		self.group = Group(self.canvas)

		self.p5 = Place(distance(0),30,self.canvas, emptycard,False)
		self.p6 = Place(distance(1),30,self.canvas, emptycard,False)
		self.p7 = Place(distance(2),30,self.canvas, emptycard,False)
		self.p8 = Place(distance(3),30,self.canvas, emptycard,False)
		self.p9 = Place(distance(4),30,self.canvas, emptycard,False)

		self.pot = 0

		self.myvar = Tkinter.StringVar()
		self.label = Tkinter.Label(self,textvariable = self.myvar, font=('Helvetica',13), width = 75, bg = python_green)
		self.label_window = self.canvas.create_window(1080,600, window = self.label)

		self.myvar.set('')
		button1 = Tkinter.Button(self, text = "Draw", font=('Helvetica',10),command = self.draw)
		button1.configure(width = 30, activebackground = "red")
		button1_window = self.canvas.create_window(distance(5)+225, 1000, window=button1)

		self.button = Tkinter.Button(self, text = 'Bet 5', font=('Helvetica',10),command = lambda: self.deal(5))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 90, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 10',font=('Helvetica',10), command = lambda: self.deal(10))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 180, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 20',font=('Helvetica',10), command = lambda: self.deal(20))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 270, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 50',font=('Helvetica',10), command = lambda: self.deal(50))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 360, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 100',font=('Helvetica',10), command = lambda: self.deal(100))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 450, window=self.button)

		self.button2 = Tkinter.Button(self, text = 'All In',font=('Helvetica',10), command = lambda: self.deal(self.player.money))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance (5) + 225, 750, window = self.button2)

		self.drawvar = Tkinter.StringVar()
		self.drawlabel = Tkinter.Label(self, textvariable = self.drawvar,font=('Helvetica',13), width = 240, bg = python_green)
		self.drawlabel_window = self.canvas.create_window(600,1200,window = self.drawlabel)
		self.drawvar.set('')

		self.var = Tkinter.StringVar()
		self.label = Tkinter.Label(self,textvariable = self.var, font=('Helvetica',13), width = 60, bg = python_green)
		self.label_window = self.canvas.create_window(1875,1350, window = self.label)
		self.var.set('Money: ' +str(self.player.money))

		self.cash = Tkinter.Button(self, text = 'Cash Out',font=('Helvetica',10), command = self.cashout)
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(1500, 13500, window=self.cash)


		# self.chipshape = self.canvas.create_oval(200, 250,400,450, fill = 'white')
		# self.chipinshape = self.canvas.create_oval(225,275, 375,425, fill = 'red', outline = 'white')

		self.drawn = True


	def deal(self,bet):
		if self.drawn == True:
			self.myvar.set('')
			self.drawvar.set('')
			self.player.money = self.player.money - bet
			self.pot = bet
			self.var.set('Money: ' +str(self.player.money))
			self.deck = []
			for x in ['H','D', 'S', 'C']:
				for y in VALS:
					self.deck.append(Card(x,y,True))
			random.shuffle(self.deck)
			if self.player.hand != []:
				self.player.hand = []

			for x in range(5):
				self.player.hand.append(self.deck[x])

			count = 0
			while count < 5:
				self.deck.remove(self.deck[0])
				count = count+1

			self.p5.card = self.player.hand[0]
			self.p5.showface()
			self.p6.card = self.player.hand[1]
			self.p6.showface()
			self.p7.card = self.player.hand[2]
			self.p7.showface()
			self.p8.card = self.player.hand[3]
			self.p8.showface()
			self.p9.card = self.player.hand[4]
			self.p9.showface()

			self.p5.flips = True
			self.p6.flips = True
			self.p7.flips = True
			self.p8.flips = True
			self.p9.flips = True
			self.drawn = False
		elif self.drawn == False:
			self.drawvar.set('You\'ve already made a bet.')



	def draw(self):
		if self.drawn == False:
			self.drawvar.set('')
			count = 0
			for x in [self.p5,self.p6,self.p7,self.p8,self.p9]:
				if x.card.opens == False:
					self.player.hand.remove(x.card)
					x.card = self.deck[count]
					x.showface()
					self.player.hand.append(x.card)
					count = count + 1
				x.flips = False

			dcount = 0
			while dcount <=count:
				self.deck.remove(self.deck[0])
				dcount = dcount + 1
			for x in [self.p5,self.p6,self.p7,self.p8,self.p9]:
				x.showface()
			mon = score(self.player.hand) * self.pot
			self.player.money = self.player.money + mon
			self.var.set('Money: '+str(self.player.money))
			self.myvar.set(printhand(self.player.hand))
			self.drawn = True
			if self.player.money < 1:
				self.canvas.delete('all')
				text = self.canvas.create_text(350,250, font=('Helvetica',13),text = 'TAKE A HIKE')
				self.but = Tkinter.Button(self, text = 'Play Again', font=('Helvetica',13),command = self.again)
				self.but.configure(width = 30, activebackground = "red")
				self.button_window = self.canvas.create_window(350, 400, window=self.but)

		elif self.drawn == True:
			self.drawvar.set('Make a bet first!')

	def cashout(self):

		f = open('highscore', 'r')
		line = f.readlines()
		f.close()
		num = line[0]
		num.strip('\n')
		score = int(num)


		a = 0
		if self.player.money > score:
			a = self.player.money
		elif self.player.money <= score:
			a = score
		g = open('highscore','w')
		g.write(str(a))
		g.close()

		self.canvas.delete('all')
		b = 'Not the Highscore'
		if a == self.player.money:
			b = 'You\'ve got the High Score'
		text = self.canvas.create_text(350,200,font=('Helvetica',13), text = 'Cashed Out')
		text = self.canvas.create_text(350,300, text = b)
		self.button = Tkinter.Button(self, text = 'Play Again',font=('Helvetica',13), command = self.again)
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(350, 400, window=self.button)

	def again(self):

		self.canvas.delete('all')
		self.player.money = 200
		self.p5 = Place(distance(0),10,self.canvas, emptycard,False)
		self.p6 = Place(distance(1),10,self.canvas, emptycard,False)
		self.p7 = Place(distance(2),10,self.canvas, emptycard,False)
		self.p8 = Place(distance(3),10,self.canvas, emptycard,False)
		self.p9 = Place(distance(4),10,self.canvas, emptycard,False)

		self.pot = 0

		self.myvar = Tkinter.StringVar()
		self.label = Tkinter.Label(self,textvariable = self.myvar,font=('Helvetica',13), width = 75, bg = python_green)
		self.label_window = self.canvas.create_window(1050,600, window = self.label)

		self.myvar.set('')
		button1 = Tkinter.Button(self, text = "Draw", font=('Helvetica',10),command = self.draw)
		button1.configure(width = 30, activebackground = "red")
		button1_window = self.canvas.create_window(distance(5)+225, 1000, window=button1)

		self.button = Tkinter.Button(self, text = 'Bet 5', font=('Helvetica',10),command = lambda: self.deal(5))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 90, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 10',font=('Helvetica',10), command = lambda: self.deal(10))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 180, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 20',font=('Helvetica',10), command = lambda: self.deal(20))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 270, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 50',font=('Helvetica',10), command = lambda: self.deal(50))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 360, window=self.button)

		self.button = Tkinter.Button(self, text = 'Bet 100',font=('Helvetica',10), command = lambda: self.deal(100))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance(5)+225, 450, window=self.button)

		self.button2 = Tkinter.Button(self, text = 'All In',font=('Helvetica',10), command = lambda: self.deal(self.player.money))
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(distance (5) + 225, 750, window = self.button2)

		self.drawvar = Tkinter.StringVar()
		self.drawlabel = Tkinter.Label(self, textvariable = self.drawvar,font=('Helvetica',13), width = 240, bg = python_green)
		self.drawlabel_window = self.canvas.create_window(600,1200,window = self.drawlabel)
		self.drawvar.set('')

		self.var = Tkinter.StringVar()
		self.label = Tkinter.Label(self,textvariable = self.var, font=('Helvetica',13), width = 60, bg = python_green)
		self.label_window = self.canvas.create_window(1875,1350, window = self.label)
		self.var.set('Money: ' +str(self.player.money))

		self.cash = Tkinter.Button(self, text = 'Cash Out',font=('Helvetica',10), command = self.cashout)
		self.button.configure(width = 30, activebackground = "red")
		self.button_window = self.canvas.create_window(1500, 13500, window=self.cash)

		self.drawn = True


if __name__ == '__main__':

	app = App(None,Player([],200))
	app.title('Draw Poker')










	app.mainloop()
