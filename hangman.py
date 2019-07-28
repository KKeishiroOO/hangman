Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hangman(word):
	wrong=0
	stages=["",
		"_________        ",
		"|                ",
		"|        |       ",
		"|        0       ",
		"|      / | \     ",
		"|       / \      ",
		]

	
>>> def hangman(word):
	wrong=0
	stages=["",
		"_________        ",
		"|                ",
		"|        |       ",
		"|        0       ",
		"|      / | \     ",
		"|       / \      ",
		]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print ("welcome to hangman!")

	
>>> def hangman(word):
	wrong=0
	stages=["",
		"_________        ",
		"|                ",
		"|        |       ",
		"|        0       ",
		"|      / | \     ",
		"|       / \      ",
		]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print ("welcome to hangman!")

	
>>> while wrong <len(stages) -1:
	print("\n")
	msg=" guess first letter "
	char = input(msg)
	if char in rletters:
		cind=rletters.index(char)
		board[cind]=char
		rletter[cind]='$'
	else:
		wrong+=1
	print(" ".join(board))
	e =wrong+1
	print("\n".join(stages[0:e]))
	if "_" not in board:
		print (" you win! ")
		print(" ".join(board))
		win=True
		break

	
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    while wrong <len(stages) -1:
NameError: name 'wrong' is not defined
>>> def hangman(word):
	wrong=0
	stages=["",
		"_________        ",
		"|                ",
		"|        |       ",
		"|        0       ",
		"|      / | \     ",
		"|       / \      ",
		]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print ("welcome to hangman!")while wrong <len(stages) -1:
		print("\n")
		msg=" guess first letter "
		char = input(msg)
		if char in rletters:
			cind=rletters.index(char)
			board[cind]=char
			rletter[cind]='$'
		else:
			wrong+=1
		print(" ".join(board))
		e =wrong+1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print (" you win! ")
			print(" ".join(board))
			win=True
			break
		
SyntaxError: invalid syntax
>>> def hangman(word):
	wrong=0
	stages=["",
		"_________        ",
		"|                ",
		"|        |       ",
		"|        0       ",
		"|      / | \     ",
		"|       / \      ",
		]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print ("welcome to hangman!")
	while wrong <len(stages) -1:
		print("\n")
		msg=" guess first letter "
		char = input(msg)
		if char in rletters:
			cind=rletters.index(char)
			board[cind]=char
			rletter[cind]='$'
		else:
			wrong+=1
		print(" ".join(board))
		e =wrong+1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print (" you win! ")
			print(" ".join(board))
			win=True
			break

		
>>> 
>>> def hangman(word):
	wrong=0
	stages=["",
		"_________        ",
		"|                ",
		"|        |       ",
		"|        0       ",
		"|      / | \     ",
		"|       / \      ",
		]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print ("welcome to hangman!")
	while wrong <len(stages) -1:
		print("\n")
		msg=" guess first letter "
		char = input(msg)
		if char in rletters:
			cind=rletters.index(char)
			board[cind]=char
			rletter[cind]='$'
		else:
			wrong+=1
		print(" ".join(board))
		e =wrong+1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print (" you win! ")
			print(" ".join(board))
			win=True
			break

		
>>> 
