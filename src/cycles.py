#!/usr/bin/python

from datetime import datetime

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Cycle:
	__date_format = "%d/%m/%Y"

	def __init__(self, begin, end, color='Blue'):
		self.begin = datetime.strptime(begin, self.__date_format)
		self.end = datetime.strptime(end, self.__date_format)
		self.days = (self.end - self.begin).days
		self.color = color
		self.events = []

	def getEventRepresentation(self, event):
		if event.eventType == 0:
			return 'r.'
		elif event.eventType == 1:
			return 'y+'
		else:
			return 'r+'

	def addEvent(self, event):
		ev_repr = self.getEventRepresentation(event)
		ev_tuple = ((event.date - self.begin).days, ev_repr)
		self.events.append( ev_tuple )


class Event:
	__date_format = "%d/%m/%Y"

	def __init__(self, date, eventType=0):
		self.date = datetime.strptime(date, self.__date_format)
		self.eventType = eventType


c1 = Cycle('1/1/2014', '31/1/2014')
c2 = Cycle('4/2/2014', '20/2/2014')
c3 = Cycle('2/3/2014', '28/3/2014', 'Green')

cycles = [c1, c2, c3]

e1 = Event('6/1/2014', eventType=1)
e11 = Event('21/1/2014')
c1.addEvent(e1)
c1.addEvent(e11)

e2 = Event('15/2/2014')
c2.addEvent(e2)

e3 = Event('12/3/2014', eventType=2)
c3.addEvent(e3)

fig, ax = plt.subplots()
width = .5
distance = 1

for x in range(len(cycles)):
	c = cycles[x]
	r = matplotlib.patches.Rectangle((x*distance, 0), width, c.days, color=c.color)
	ax.add_patch(r)

	for i, e in enumerate(c.events):
		ax.plot(x*distance + width/2, e[0], e[1])


ax.set_xlim([0, len(cycles)])
ax.set_ylim([0, 35])
plt.show()