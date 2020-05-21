
from CheckMoves import *
import copy
import random as rng
RED = '\33[37;41m'
BLK = '\33[37;40m'
GRY = '\33[39;47m'
REG = '\33[39;49m'
NUM_MVS = 8


def get_white_valid(board):
	def get_white_moves(board):
		move_list=[]
		for y in range(len(board)):
			for x in range(len(board[y])):
				if board[y][x] > 1:
					for m in move_dict()[board[y][x]]:
						for c in m[0]:
							x1 = x+c[0]
							y1 = y+c[1]
							v = c[2]
							if(x1 < 0 or y1 < 0 or x1 >= len(board[y]) or y1 >= len(board) or not(v==board[y1][x1])):
								break
						else:
							move_list.append((x,y,m[1]))
		return move_list
	def get_white_captures(board):
		move_list=[]
		for y in range(len(board)):
			for x in range(len(board[y])):
				if board[y][x] > 1:
					for m in cap_dict()[board[y][x]]:
						for c in m[0]:
							x1 = x+c[0]
							y1 = y+c[1]
							v = c[2]

							if x1 < 0 or y1 < 0 or x1 >=  len(board[y]) or y1 >= len(board) or not(v==board[y1][x1] or (v==-1 and board[y1][x1] <v)):
								break
						else:
							move_list.append((x,y,m[1]))
		return move_list
	def get_white_multicaps(board):
		def get_white_subcaps(board,move):
			make_move(board,move)
			move_list = []
			x=move[0]+move[2][0][0]
			y=move[1]+move[2][0][1]
			for m in cap_dict()[board[y][x]]:
				for c in m[0]:
					x1 = x+c[0]
					y1 = y+c[1]
					v = c[2]

					if x1 < 0 or y1 < 0 or x1 >=  len(board[y]) or y1 >= len(board) or not(v==board[y1][x1] or (v==-1 and board[y1][x1] <v)):
						break
				else:
					move_list.append((x,y,m[1]))
			if len(move_list) ==0:
				return [move]
			return_list = []
			for m in move_list:
				return_list += merge_moves(move,get_white_subcaps(copy.deepcopy(board),m))
			return return_list
		move_list = []
		for m in get_white_captures(board):
			move_list+=get_white_subcaps(copy.deepcopy(board),m)
		return move_list
	valid_list = get_white_moves(board) if len(get_white_captures(board)) == 0 else get_white_multicaps(board)
	rng.shuffle(valid_list)
	return valid_list
def get_black_valid(board):
	def get_black_moves(board):
		move_list=[]
		for y in range(len(board)):
			for x in range(len(board[y])):
				if board[y][x] < -1:
					for m in move_dict()[board[y][x]]:
						for c in m[0]:
							x1 = x+c[0]
							y1 = y+c[1]
							v = c[2]
							if(x1 < 0 or y1 < 0 or x1 >= len(board[y]) or y1 >= len(board) or not(v==board[y1][x1])):
								break
						else:
							move_list.append((x,y,m[1]))
		return move_list
	def get_black_captures(board):
		move_list=[]
		for y in range(len(board)):
			for x in range(len(board[y])):
				if board[y][x] < -1:
					for m in cap_dict()[board[y][x]]:
						for c in m[0]:
							x1 = x+c[0]
							y1 = y+c[1]
							v = c[2]

							if x1 < 0 or y1 < 0 or x1 >=  len(board[y]) or y1 >= len(board) or not(v==board[y1][x1] or (v==1 and board[y1][x1] >v)):
								break
						else:
							move_list.append((x,y,m[1]))
		return move_list
	def get_black_multicaps(board):
		def get_black_subcaps(board,move):
			make_move(board,move)
			move_list = []
			x=move[0]+move[2][0][0]
			y=move[1]+move[2][0][1]
			for m in cap_dict()[board[y][x]]:
				for c in m[0]:
					x1 = x+c[0]
					y1 = y+c[1]
					v = c[2]
					if x1 < 0 or y1 < 0 or x1 >=  len(board[y]) or y1 >= len(board) or not(v==board[y1][x1] or (v==1 and board[y1][x1] >v)):
						break
				else:
					move_list.append((x,y,m[1]))
			if len(move_list) ==0:
				return [move]
			return_list = []
			for m in move_list:
				return_list += merge_moves(move,get_black_subcaps(copy.deepcopy(board),m))
			return return_list
		move_list = []
		for m in get_black_captures(board):
			move_list+=get_black_subcaps(copy.deepcopy(board),m)
		return move_list
	valid_list =   get_black_moves(board) if len(get_black_captures(board)) == 0 else get_black_multicaps(board)
	rng.shuffle(valid_list)
	return valid_list
def merge_moves(move,move_list):
	merge_list = []
	x = move[0]
	y = move[1]
	vals = list(move[2])
	for m in move_list:
		dx = m[0]-x
		dy = m[1]-y
		newvals = []
		for c in m[2]:
			lc = list(c)
			lc[0]+=dx
			lc[1]+=dy
			newvals.append(tuple(lc))
		newvals=tuple(vals+newvals)
		merge_list.append((x,y,newvals))
	return merge_list 
def get_val(board):

	return sum(map(sum,board))
def minmax(board,lvl= NUM_MVS,alpha= -(51+NUM_MVS),beta=51+NUM_MVS):
	min_val = (50+lvl)
	move = 0
	if lvl < 0:
		min_val = get_val(board)	
	else:
		for m in get_black_valid(board):
			new  = maxmin(do_move(copy.deepcopy(board),m),lvl-1,alpha,beta)[0]
			if new < min_val :
				move = m
				min_val = new
			beta = min(beta,min_val)
			if(alpha>=beta):
				break
	return (min_val,move)
def maxmin(board,lvl= NUM_MVS,alpha= -(51+NUM_MVS),beta=51+NUM_MVS):
	max_val = -(50+lvl)
	move = 0
	if lvl < 0:
		max_val = get_val(board)
	else:
		for m in get_white_valid(board):
			new  = minmax(do_move(copy.deepcopy(board),m),lvl-1,alpha,beta)[0]
			if new > max_val :
				move = m
				max_val = new
			alpha = max(alpha,max_val)
			if(alpha>=beta):
				break
	return (max_val,move)
def do_move(board,move):
	def upgrade(board):
		board[0] = [ -4 if v==-2 else v for v in board[0] ]
		board[-1] = [ 4 if v==2 else v for v in board[-1] ]
	make_move(board,move)
	upgrade(board)
	return board
def make_move(board,move):
	for m in move[2]:
		board[move[1]+m[1]][move[0]+m[0]] = m[2]
def display(board):
	for y in range(len(board)):
		for x in range(len(board[y])):
			if(board[y][x]) >0:
				print(RED,board[y][x],REG,end="")
			
			elif(board[y][x])<0:
				print(BLK,abs(board[y][x]),REG,end="")
			elif (y+x)%2 == 1:
				print(GRY," ",REG,end="")
			else:
				print(REG," ",REG,end="")
		print("")
	print("\n\n")
def run():
	def selfPlay():
		board =	[
					[0,2,0,2,0,2,0,2],
					[2,0,2,0,2,0,2,0],
					[0,2,0,2,0,2,0,2],
					[0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0],
					[0,-2,0,-2,0,-2,0,-2],
					[-2,0,-2,0,-2,0,-2,0],
					[0,-2,0,-2,0,-2,0,-2]
			]

		display(board);
		while True:
			b_move = maxmin(copy.deepcopy(board))
			print(b_move,end = "\n\n")
			if b_move[1] == 0:
				print(BLK,"Black Wins!",REG)
				break;
			display(do_move(board,b_move[1]))	
			b_move = minmax(copy.deepcopy(board))
			print(b_move,end = "\n\n")
			if b_move[1] == 0:
				print(RED,"Red Wins!",REG)
				break;
			display(do_move(board,b_move[1]))
	def vsWhite():
		board =	[
					[0,2,0,2,0,2,0,2],
					[2,0,2,0,2,0,2,0],
					[0,2,0,2,0,2,0,2],
					[0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0],
					[-2,0,-2,0,-2,0,-2,0],
					[0,-2,0,-2,0,-2,0,-2],
					[-2,0,-2,0,-2,0,-2,0]
			]

		display(board);
		while True:
			i =0;
			for m in get_white_valid(board):
				print(i,m,sep = ": ")
				i+=1
			w_move = get_white_valid(board)[int(input("Pick a move: "))]
			print("Moving...")
			display(do_move(board,w_move))

			b_move = minmax(copy.deepcopy(board))
			print(b_move,end = "\n\n")
			if b_move[1] == 0:
				print(RED,"Red Wins!",REG)
				break;
			display(do_move(board,b_move[1]))
	def testPlay():
		board =	[
					[0,0,0,0,0,0,0,0],
					[4,0,0,0,0,0,0,0],
					[0,-2,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0],
					[0,-2,0,-2,0,-2,0,0],
					[0,0,0,0,0,0,0,0],
					
			]

		display(board);
		while True:	
			
			b_move = maxmin(copy.deepcopy(board))
			print(b_move,end = "\n\n")
			if b_move[1] == 0:
				print(BLK,"Black Wins!",REG)
				break;
			display(do_move(board,b_move[1]))

			b_move = minmax(copy.deepcopy(board))
			print(b_move,end = "\n\n")
			if b_move[1] == 0:
				print(RED,"Red Wins!",REG)
				break;
			display(do_move(board,b_move[1]))

	vsWhite()

run()









