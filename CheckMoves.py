'''
	defines the sets of all legal moves for varios pieces
	the set of valid moves/captures is given a set of paired tuples

	each set(line) is one valid move for the piece
	each move is composed of 2 parts: the required conditions, and the end state modifications
	the ordered tripples are in the format(x,y,pieceNum)
		the x and y are realive to the piec that is moved
		each piece is given a unique number(eg: white king = 4)
			whites are +
			blacks are -
			0 is empty
			+/- 1 refers any piece of that color
'''
wc_moves =  (
				(((1,1,0),),((1,1,2),(0,0,0))),
				(((-1,1,0),),((-1,1,2),(0,0,0)))
			)
bc_moves = (
				(((1,-1,0),),((1,-1,-2),(0,0,0))),
				(((-1,-1,0),),((-1,-1,-2),(0,0,0)))
			)
wk_moves = (
				(((1,1,0),),((1,1,4),(0,0,0))),
				(((-1,1,0),),((-1,1,4),(0,0,0))),
				(((1,-1,0),),((1,-1,4),(0,0,0))),
				(((-1,-1,0),),((-1,-1,4),(0,0,0)))
			)
bk_moves = (
				(((1,1,0),),((1,1,-4),(0,0,0))),
				(((-1,1,0),),((-1,1,-4),(0,0,0))),
				(((1,-1,0),),((1,-1,-4),(0,0,0))),
				(((-1,-1,0),),((-1,-1,-4),(0,0,0)))
			)
wc_captures = (
				(((2,2,0),(1,1,-1)),((2,2,2),(0,0,0),(1,1,0))),
				(((-2,2,0),(-1,1,-1)),((-2,2,2),(0,0,0),(-1,1,0)))
			)
bc_captures = (
				(((2,-2,0),(1,-1,1)),((2,-2,-2),(0,0,0),(1,-1,0))),
				(((-2,-2,0),(-1,-1,1)),((-2,-2,-2),(0,0,0),(-1,-1,0)))
			)
wk_captures = (
				(((2,2,0),(1,1,-1)),((2,2,4),(0,0,0),(1,1,0))),
				(((-2,2,0),(-1,1,-1)),((-2,2,4),(0,0,0),(-1,1,0))),
				(((2,-2,0),(1,-1,-1)),((2,-2,4),(0,0,0),(1,-1,0))),
				(((-2,-2,0),(-1,-1,-1)),((-2,-2,4),(0,0,0),(-1,-1,0)))
			)
bk_captures = (
				(((2,2,0),(1,1,1)),((2,2,-4),(0,0,0),(1,1,0))),
				(((-2,2,0),(-1,1,1)),((-2,2,-4),(0,0,0),(-1,1,0))),
				(((2,-2,0),(1,-1,1)),((2,-2,-4),(0,0,0),(1,-1,0))),
				(((-2,-2,0),(-1,-1,1)),((-2,-2,-4),(0,0,0),(-1,-1,0)))
			)
def move_dict():
	return {
		-4: bk_moves,
		-2: bc_moves,
		2: wc_moves,
		4: wk_moves,
	}
def cap_dict():
	return {
		-4: bk_captures,
		-2: bc_captures,
		2: wc_captures,
		4: wk_captures,
	}

