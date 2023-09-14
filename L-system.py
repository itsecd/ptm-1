import turtle
from random import randint


def init_pythagoras_tree():
	genome = '0'
	width = 20
	length = 1
	iter_number = 10
	return genome, length, width, iter_number


def init_branch1():
	genome = 'X'
	length = 7
	angle = 25
	iter_number = 6
	return genome, length, angle, iter_number


def init_branch2():
	genome = 'F'
	length = 4
	angle = 25.7
	iter_number = 5
	return genome, length, angle, iter_number


def init_branch3():
	genome = 'F'
	length = 9
	angle = 20
	iter_number = 5
	return genome, length, angle, iter_number


def init_branch4():
	genome = 'F'
	length = 9
	angle = 22.5
	iter_number = 4
	return genome, length, angle, iter_number


def init_branch5():
	genome = 'X'
	length = 7
	angle = 20
	iter_number = 6
	return genome, length, angle, iter_number


def init_branch6():
	genome = 'X'
	length = 7
	angle = 25.7
	iter_number = 6
	return genome, length, angle, iter_number


def init_tree():
	genome = '222220'
	angle = 14
	length = 10
	iter_number = 11
	width = 16
	return genome, length, angle, iter_number, width


def pythagoras_tree_rules(prev_genome):
	new_genome = ''
	for i in range(len(prev_genome)):
		if prev_genome[i] == '0':
			new_genome = new_genome + '1[0]0'
		elif prev_genome[i] == '1':
			new_genome = new_genome + '11'
		elif prev_genome[i] == '[':
			new_genome = new_genome + '['
		elif prev_genome[i] == ']':
			new_genome = new_genome + ']'
	return new_genome


def branch_rules1(prev_genome):
	new_genome = ''
	for i in range(len(prev_genome)):
		if prev_genome[i] == 'X':
			new_genome = new_genome + 'F-[[X]+X]+F[+FX]-X'
		elif prev_genome[i] == 'F':
			new_genome = new_genome + 'FF'
		elif prev_genome[i] == '[':
			new_genome = new_genome + '['
		elif prev_genome[i] == ']':
			new_genome = new_genome + ']'
		elif prev_genome[i] == '+':
			new_genome = new_genome + '+'
		elif prev_genome[i] == '-':
			new_genome = new_genome + '-'
	return new_genome


def branch_rules2(prev_genome):
	new_genome = ''
	for i in range(len(prev_genome)):
		if prev_genome[i] == 'F':
			new_genome = new_genome + 'F[+F]F[-F]F'
		elif prev_genome[i] == '[':
			new_genome = new_genome + '['
		elif prev_genome[i] == ']':
			new_genome = new_genome + ']'
		elif prev_genome[i] == '+':
			new_genome = new_genome + '+'
		elif prev_genome[i] == '-':
			new_genome = new_genome + '-'
	return new_genome


def branch_rules3(prev_genome):
	new_genome = ''
	for i in range(len(prev_genome)):
		if prev_genome[i] == 'F':
			new_genome = new_genome + 'F[+F]F[-F][F]'
		elif prev_genome[i] == '[':
			new_genome = new_genome + '['
		elif prev_genome[i] == ']':
			new_genome = new_genome + ']'
		elif prev_genome[i] == '+':
			new_genome = new_genome + '+'
		elif prev_genome[i] == '-':
			new_genome = new_genome + '-'
	return new_genome


def branch_rules4(prev_genome):
	new_genome = ''
	for i in range(len(prev_genome)):
		if prev_genome[i] == 'F':
			new_genome = new_genome + 'FF-[-F+F+F]+[+F-F-F]'
		elif prev_genome[i] == '[':
			new_genome = new_genome + '['
		elif prev_genome[i] == ']':
			new_genome = new_genome + ']'
		elif prev_genome[i] == '+':
			new_genome = new_genome + '+'
		elif prev_genome[i] == '-':
			new_genome = new_genome + '-'
	return new_genome


def branch_rules5(prev_genome):
	new_genome = ''
	for i in range(len(prev_genome)):
		if prev_genome[i] == 'X':
			new_genome = new_genome + 'F[+X]F[-X]+X'
		elif prev_genome[i] == 'F':
			new_genome = new_genome + 'FF'
		elif prev_genome[i] == '[':
			new_genome = new_genome + '['
		elif prev_genome[i] == ']':
			new_genome = new_genome + ']'
		elif prev_genome[i] == '+':
			new_genome = new_genome + '+'
		elif prev_genome[i] == '-':
			new_genome = new_genome + '-'
	return new_genome


def branch_rules6(prev_genome):
	new_genome = ''
	for i in range(len(prev_genome)):
		if prev_genome[i] == 'X':
			new_genome = new_genome + 'F[+X][-X]FX'
		elif prev_genome[i] == 'F':
			new_genome = new_genome + 'FF'
		elif prev_genome[i] == '[':
			new_genome = new_genome + '['
		elif prev_genome[i] == ']':
			new_genome = new_genome + ']'
		elif prev_genome[i] == '+':
			new_genome = new_genome + '+'
		elif prev_genome[i] == '-':
			new_genome = new_genome + '-'
	return new_genome


def tree_rules(prev_genome):
	new_genome = ''
	level = 0
	for i in range(len(prev_genome)):
		if prev_genome[i] == '0':
			new_genome = new_genome + '1[-20]+20'
		elif prev_genome[i] == '1':
			new_genome = new_genome + '21'
		elif prev_genome[i] == '[':
			new_genome = new_genome + prev_genome[i]
			level += 1
		elif prev_genome[i] == ']':
			new_genome = new_genome + prev_genome[i]
			level -= 1
		elif prev_genome[i] == '2':
			if randint(0, 100) < 7 and level > 2:
				new_genome = new_genome + '3[^30]'
			else:
				new_genome = new_genome + prev_genome[i]
		else:
			new_genome = new_genome + prev_genome[i]
	return new_genome


def run_pythagoras_tree(genome, length, width):
	stack = []
	for i in range(len(genome)):
		turtle.width(width)
		if genome[i] == '0':
			turtle.color('green')
			turtle.forward(length+20)
			turtle.color('black')
		if genome[i] == '1':
			turtle.forward(length)
		if genome[i] == '[':
			width -= 2
			stack.append(str(turtle.xcor()) + ' ' + str(turtle.ycor()) + ' ' + str(turtle.heading()) + ' ' + str(width))
			turtle.seth(turtle.heading() + 30)
		if genome[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			width = t[3]
			turtle.penup()
			turtle.setpos(t[0], t[1])
			turtle.pendown()
			turtle.seth(t[2]-30)


def run_branch(genome, length, angle):
	stack = []
	for i in range(len(genome)):
		if genome[i] == 'F':
			turtle.forward(length)
		elif genome[i] == '[':
			stack.append(str(turtle.xcor()) + ' ' + str(turtle.ycor()) + ' ' + str(turtle.heading()))
			turtle.seth(turtle.heading())
		elif genome[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			turtle.penup()
			turtle.setpos(t[0], t[1])
			turtle.pendown()
			turtle.seth(t[2])
		elif genome[i] == '-':
			turtle.left(angle)
		elif genome[i] == '+':
			turtle.right(angle)
	

def run_tree(genome, length, angle, width):
	stack = []
	for i in range(len(genome)):
		turtle.width(width)
		if genome[i] == '0':
			q = turtle.pensize()
			turtle.width(4)
			r = randint(0, 10)
			if r < 3:
				turtle.pencolor('#009900')
			elif r > 6:
				turtle.pencolor('#667900')
			else:
				turtle.pencolor('#20BB00')
			turtle.forward(length-2)
			turtle.width(q)
			turtle.color('black')
		elif genome[i] == '^':
			tmp_angle = randint(-30, 30)
			if tmp_angle < 0:
				turtle.left(tmp_angle - 25)
			else:
				turtle.left(tmp_angle + 25)
		elif genome[i] == '1':
			if randint(0, 10) > 4:
				turtle.forward(length)
		elif genome[i] == '2':
			if randint(0, 10) > 4:
				turtle.forward(length)
		elif genome[i] == '[':
			width *= 0.75
			stack.append(str(turtle.xcor()) + ' ' + str(turtle.ycor()) + ' ' + str(turtle.heading()) + ' ' + str(width))
		elif genome[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			turtle.penup()
			turtle.setpos(t[0], t[1])
			turtle.pendown()
			turtle.seth(t[2])
			width = t[3]
		elif genome[i] == '+':
			turtle.right(angle+randint(-13, 13))
		elif genome[i] == '-':
			turtle.left(angle+randint(-13, 13))
		else:
			if randint(0, 10) > 4:
				turtle.forward(length)


def run_apple(genome, length, angle, width):
	stack = []
	for i in range(len(genome)):
		turtle.width(width)
		if genome[i] == '0':
			q = turtle.pensize()
			turtle.width(4)
			r = randint(0, 10)
			if r < 3:
				turtle.pencolor('#009900')
			elif r > 6:
				turtle.pencolor('#667900')
			else:
				turtle.pencolor('#20BB00')
			if 7 > len(stack) > 2 and randint(0, 100) < 7:
				w = turtle.heading()
				turtle.seth(-90)
				turtle.width(2)
				turtle.color('black')
				turtle.forward(5)
				turtle.pencolor('#992200')
				turtle.width(7)
				turtle.forward(length-9)
				turtle.seth(w)
			else:
				turtle.forward(length-2)
			turtle.width(q)
			turtle.color('black')
		elif genome[i] == '^':
			tmp_angle = randint(-30, 30)
			if tmp_angle < 0:
				turtle.left(tmp_angle - 25)
			else:
				turtle.left(tmp_angle + 25)
		elif genome[i] == '1':
			if randint(0, 10) > 4:
				turtle.forward(length)
		elif genome[i] == '2':
			if randint(0, 10) > 4:
				turtle.forward(length)
		elif genome[i] == '[':
			width *= 0.75
			stack.append(str(turtle.xcor()) + ' ' + str(turtle.ycor()) + ' ' + str(turtle.heading()) + ' ' + str(width))
		elif genome[i] == ']':
			t = list(map(float, stack[-1].split()))
			stack.pop(-1)
			turtle.penup()
			turtle.setpos(t[0], t[1])
			turtle.pendown()
			turtle.seth(t[2])
			width = t[3]
		elif genome[i] == '+':
			turtle.right(angle+randint(-13, 13))
		elif genome[i] == '-':
			turtle.left(angle+randint(-13, 13))
		else:
			if randint(0, 10) > 4:
				turtle.forward(length)


if __name__ == "__main__":
	turtle.hideturtle()
	turtle.color('black')
	turtle.tracer(0)
	turtle.seth(90)
	turtle.penup()
	turtle.setpos(0, -250)
	turtle.pendown()
	turtle.width(1)
	tree_genome, tree_length, tree_angle, tree_iter_number, tree_width = init_tree()
	for j in range(tree_iter_number):
		tree_genome = tree_rules(tree_genome)
	run_apple(tree_genome, tree_length, tree_angle, tree_width)
	turtle.done()
