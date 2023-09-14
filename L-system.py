from turtle import *
from random import randint
hideturtle()
color('black')
tracer(0)
seth(90)
penup()
setpos(0, -250)
pendown()
width(1)


def init_tree():
	width(16)
	oak = '222220'
	angle = 14
	length = 10
	n = 11
	wid = 16
	return oak, length, angle, n, wid


def init_branch1():
	oak = 'X'
	length = 7
	angle = 25
	n = 6
	return oak, length, angle, n


def init_branch2():
	oak = 'F'
	length = 4
	angle = 25.7
	n = 5
	return oak, length, angle, n


def init_branch3():
	oak = 'F'
	length = 9
	angle = 20
	n = 5
	return oak, length, angle, n


def init_branch4():
	oak = 'F'
	length = 9
	angle = 22.5
	n = 4
	return oak, length, angle, n


def init_branch5():
	oak = 'X'
	length = 7
	angle = 20
	n = 6
	return oak, length, angle, n


def init_branch6():
	oak = 'X'
	length = 7
	angle = 25.7
	n = 6
	return oak, length, angle, n


def init_pythagoras_tree():
	oak = '0'
	wid = 20
	length = 1
	n = 10
	return oak, length, wid, n


def pythagoras_tree_rules(s):
	s1 = ''
	for i in range(len(s)):
		if s[i] == '0':
			s1 = s1 + '1[0]0'
		elif s[i] == '1':
			s1 = s1 + '11'
		elif s[i] == '[':
			s1 = s1 + '['
		elif s[i] == ']':
			s1 = s1 + ']'
	return s1


def run_pythagoras_tree(s, length, wid):
	stack = []
	for i in range(len(s)):
		width(wid)
		if s[i] == '0':
			color('green')
			forward(length+20)
			color('black')
		if s[i] == '1':
			forward(length)
		if s[i] == '[':
			wid -= 2
			stack.append(str(xcor()) + ' ' + str(ycor()) + ' ' + str(heading()) + ' ' + str(wid))
			seth(heading() + 30)
		if s[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			wid = t[3]
			penup()
			setpos(t[0], t[1])
			pendown()
			seth(t[2]-30)


def branch_rules1(s):
	s1=''
	for i in range(len(s)):
		if s[i] == 'X':
			s1 = s1 + 'F-[[X]+X]+F[+FX]-X'
		elif s[i] == 'F':
			s1 = s1 + 'FF'
		elif s[i] == '[':
			s1 = s1 + '['
		elif s[i] == ']':
			s1 = s1 + ']'
		elif s[i] == '+':
			s1 = s1 + '+'
		elif s[i] == '-':
			s1 = s1 + '-'
	return s1


def branch_rules2(s):
	s1 = ''
	for i in range(len(s)):
		if s[i] == 'F':
			s1 = s1 + 'F[+F]F[-F]F'
		elif s[i] == '[':
			s1 = s1 + '['
		elif s[i] == ']':
			s1 = s1 + ']'
		elif s[i] == '+':
			s1 = s1 + '+'
		elif s[i] == '-':
			s1 = s1 + '-'
	return s1


def branch_rules3(s):
	s1 = ''
	for i in range(len(s)):
		if s[i] == 'F':
			s1 = s1 + 'F[+F]F[-F][F]'
		elif s[i] == '[':
			s1 = s1 + '['
		elif s[i] == ']':
			s1 = s1 + ']'
		elif s[i] == '+':
			s1 = s1 + '+'
		elif s[i] == '-':
			s1 = s1 + '-'
	return s1


def branch_rules4(s):
	s1 = ''
	for i in range(len(s)):
		if s[i] == 'F':
			s1 = s1 + 'FF-[-F+F+F]+[+F-F-F]'
		elif s[i] == '[':
			s1 = s1 + '['
		elif s[i] == ']':
			s1 = s1 + ']'
		elif s[i] == '+':
			s1 = s1 + '+'
		elif s[i] == '-':
			s1 = s1 + '-'
	return s1


def branch_rules5(s):
	s1 = ''
	for i in range(len(s)):
		if s[i] == 'X':
			s1 = s1 + 'F[+X]F[-X]+X'
		elif s[i] == 'F':
			s1 = s1 + 'FF'
		elif s[i] == '[':
			s1 = s1 + '['
		elif s[i] == ']':
			s1 = s1 + ']'
		elif s[i] == '+':
			s1 = s1 + '+'
		elif s[i] == '-':
			s1 = s1 + '-'
	return s1


def branch_rules6(s):
	s1 = ''
	for i in range(len(s)):
		if s[i] == 'X':
			s1 = s1 + 'F[+X][-X]FX'
		elif s[i] == 'F':
			s1 = s1 + 'FF'
		elif s[i] == '[':
			s1 = s1 + '['
		elif s[i] == ']':
			s1 = s1 + ']'
		elif s[i] == '+':
			s1 = s1 + '+'
		elif s[i] == '-':
			s1 = s1 + '-'
	return s1


def run_branch(s, length, angle):
	stack = []
	for i in range(len(s)):
		if s[i] == 'F':
			forward(length)
		elif s[i] == '[':
			stack.append(str(xcor()) + ' ' + str(ycor()) + ' ' + str(heading()))
			seth(heading())
		elif s[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			penup()
			setpos(t[0], t[1])
			pendown()
			seth(t[2])
		elif s[i] == '-':
			left(angle)
		elif s[i] == '+':
			right(angle)


def tree_rules(s):
	s1 = ''
	level = 0
	for i in range(len(s)):
		if s[i] == '0':
			s1 = s1 + '1[-20]+20'
		elif s[i] == '1':
			s1 = s1 + '21'
		elif s[i] == '[':
			s1 = s1 + s[i]
			level += 1
		elif s[i] == ']':
			s1 = s1 + s[i]
			level -= 1
		elif s[i] == '2':
			if randint(0, 100) < 7 and level > 2:
				s1 = s1 + '3[^30]'
			else:
				s1 = s1 + s[i]
		else:
			s1 = s1 + s[i]
	return s1
	

def run_tree(s, length, angle, wid):
	stack = []
	for i in range(len(s)):
		width(wid)
		if s[i] == '0':
			q = pensize()
			width(4)
			r = randint(0, 10)
			if r < 3:
				pencolor('#009900')
			elif r > 6:
				pencolor('#667900')
			else:
				pencolor('#20BB00')
			forward(length-2)
			width(q)
			color('black')
		elif s[i] == '^':
			ug = randint(-30, 30)
			if ug < 0:
				left(ug - 25)
			else:
				left(ug + 25)
		elif s[i] == '1':
			if randint(0, 10) > 4:
				forward(length)
		elif s[i] == '2':
			if randint(0, 10) > 4:
				forward(length)
		elif s[i] == '[':
			wid *= 0.75
			stack.append(str(xcor()) + ' ' + str(ycor()) + ' ' + str(heading()) + ' ' + str(wid))
		elif s[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			penup()
			setpos(t[0], t[1])
			pendown()
			seth(t[2])
			wid = t[3]
		elif s[i] == '+':
			right(angle+randint(-13, 13))
		elif s[i] == '-':
			left(angle+randint(-13, 13))
		else:
			if randint(0, 10) > 4:
				forward(length)


def run_apple(s, length, angle, wid):
	stack = []
	for i in range(len(s)):
		width(wid)
		if s[i] == '0':
			q = pensize()
			width(4)
			r = randint(0,10)
			if r < 3:
				pencolor('#009900')
			elif r > 6:
				pencolor('#667900')
			else:
				pencolor('#20BB00')
			if 7 > len(stack) > 2 and randint(0, 100) < 7:
				w = heading()
				seth(-90)
				width(2)
				color('black')
				forward(5)
				pencolor('#992200')
				width(7)
				forward(length-9)
				seth(w)
			else:
				forward(length-2)
			width(q)
			color('black')
		elif s[i] == '^':
			ug = randint(-30, 30)
			if ug < 0:
				left(ug - 25)
			else:
				left(ug + 25)
		elif s[i] == '1':
			if randint(0, 10) > 4:
				forward(length)
		elif s[i] == '2':
			if randint(0, 10) > 4:
				forward(length)
		elif s[i] == '[':
			wid *= 0.75
			stack.append(str(xcor()) + ' ' + str(ycor()) + ' ' + str(heading()) + ' ' + str(wid))
		elif s[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			penup()
			setpos(t[0], t[1])
			pendown()
			seth(t[2])
			wid = t[3]
		elif s[i] == '+':
			right(angle+randint(-13, 13))
		elif s[i] == '-':
			left(angle+randint(-13, 13))
		else:
			if randint(0, 10) > 4:
				forward(length)


if __name__ == "__main__":
	oak, length, angle, n, wid = init_tree()
	for i in range(n):
		oak = tree_rules(oak)
	run_apple(oak, length, angle, wid)
	update()
	mainloop()
