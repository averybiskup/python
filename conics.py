#*! users/avery/temp

import math
import time
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

python = sys.executable

x = 50

# Basically what the program does.

#x = (p1, p1n, p1a, p1an, p1b, p1bn, p1c, p1cn)
	
#y = (p2, p2n, p3, p3n, p4, p4n, p5, p5n)

#y = ax^2 + hx + k

#y - k = ax^2 + hx

#y - k = a(x^2 + hx)

#h/2 = _^2

##y - k + {h/2 = _^2} = a(x^2 + hx + {h/2 = _^2})

#y - k = a(x + h)x(x + {h/2 = _^2})

#y - k = a(x + h)^2


#End
#y - k = a(x - h)^2 -/ final




print "Welcome to the Conic equation transformer!"
print "if ready type p"

user_input = raw_input(":")



if user_input=="p":
	
	num_a = float (raw_input("a:"))
	
	num_b = float (raw_input("b:"))
	
	num_c = float (raw_input("c:"))
	
	#y = ax^2 + hx + k
	print ('Your form is y = %sx^2 + %sx + %s...correct? [yes/no]') % (num_a, num_b, num_c)
	
user_input = raw_input(":")	
	
if user_input=="yes":
	print ("Great! Here you go!")
	print"=" * x
		
	numb = (num_b / 2.0)
	
	numb2 = (numb ** 2)
	
	numcb = (num_c + numb2)
	
	ts = time.sleep
	
	num_c_2 = (0 - num_c)
		
	ts(1)	
	
	#y - k = ax^2 + hx
	print ("y %s = %sx^2 + %sx") % (num_c_2, num_a, num_b)
	
	print"=" * x
	
	num_a2 = (num_b / num_a)
	
	numb = (num_a2 / 2.0)
	
	numb2 = (numb ** 2)
	
	numc = (0 - num_c)
	
	numcb = (numc + numb2)
	
	numcb_2 = ((numb2 * num_a) + num_c_2)
	
	ts(1)
	
	#y - k = a(x^2 + hx)
	print ("y %s = %s(x^2 + %sx + %s)") % (numcb_2, num_a, num_a2, numb2)
	
	print"=" * x
	
	numb2_2 = (numb2 / 2.0)
	
	num_b2 = (num_b / 2.0)
	
	final = (num_a2 / 2.0)
	
	ts(1)
	
	#y - k = a(x + h)^2 final
	print ("y %s = %s(x + %s)^2" ) % (numcb_2, num_a, final)
	
	print"=" * x
	
	vy = (numcb_2 * -1.0)
	
	vx = (final * -1.0)
	
	ts(1)
	
	print ("Vertex = (%s, %s)") % (vx, vy)
	
	print"=" * x
	
	yfocus = (num_a + final)
	
	ts(1)
	
	print ("Focus = (%s, %s)") % (vx, yfocus)
	
	print"=" * x
	
	ts(1)
	
	p1 = (vx + 1.0) #go over 1, and see what y equals then.
	
	p2 = (num_a * p1**2 + num_b * p1 + num_c)
	
	p1a = (vx + 2.0)
	
	p3 = (num_a * p1a**2 + num_b * p1a + num_c)
	
	p1b = (vx + 3.0)
	
	p4 = (num_a * p1b**2 + num_b * p1b + num_c)
	
	p1c = (vx + 4.0)
	
	p5 = (num_a * p1c**2 + num_b * p1c + num_c)
	
	
	
	p1n = (vx - 1.0)
	
	p2n = (num_a * p1**2 + num_b * p1 + num_c)
	
	p1an = (vx - 2.0)
	
	p3n = (num_a * p1a**2 + num_b * p1a + num_c)
	
	p1bn = (vx - 3.0)
	
	p4n = (num_a * p1b**2 + num_b * p1b + num_c)
	
	p1cn = (vx - 4.0)
	
	p5n = (num_a * p1c**2 + num_b * p1c + num_c)
	
	
	print ("Points of your Parabola: \n(%s, %s), (%s, %s) \n(%s, %s), (%s, %s) \n(%s, %s), (%s, %s) \n(%s, %s), (%s, %s)") % (p1, p2, p1n, p2n, p1a, p3, p1an, p3n, p1b, p4, p1bn, p4n, p1c, p5, p1cn, p5n)
	
	print"=" * x
	
	print ("Your x-intercepts are the two points where y = 0.0\n\nif it's not there, the point is not a whole number.\n\nHowever, these are all points on the parabola.")
	
	print"=" * x
	
	ts(1)
	
	print ("Want another transformation? [y/n]")
	
	x = [p1, p1n, p1a, p1an, p1b, p1bn, p1c, p1cn]
	y = [p2, p2n, p3, p3n, p4, p4n, p5, p5n]
	focus = (vx, yfocus)
	vertex = (vx, vy)

	plt.scatter(x,y, label="Scatter", color="c", marker='+', s=100,)
	plt.scatter(vx, yfocus, label="Focus", color="k", marker='^', s=200)
	plt.scatter(vx, vy, label="Vertex", color="m", marker='*', s=200)

	plt.xlabel("X")
	plt.ylabel("Y")
	plt.title("Parabola")
	plt.legend()
	plt.show()

elif user_input=='no':
	print ("Oops, try again.")
	sys.exit()

user_input = raw_input(":")	
	
if user_input=='y':
	
	def restart_program():
		"Restarts program"
    	
	os.execl(python, python, *sys.argv)	
	
elif user_input=='n':
	quit
	

