import random
import AB_kai as ab
import sys

DEPTH = 3
SIZE = 8

"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""

def getAction(board, moves):
	sorted_move = ab.sort(board, moves, DEPTH)
	print(sorted_move)
	puttable = len(sorted_move)
	move_candidate = sorted_move[-1]

	corner = [[0, 0], [0 ,7], [7, 0], [7, 7]]
	x_point = [[1, 1], [1, 6], [6, 1], [6, 6]]
	c_point = [ [1, 0], [0, 6], [6, 0], [0, 1],
				[7, 1], [1, 7], [6, 7], [7, 6]]

	is_x = (move_candidate in x_point) and (puttable >= 2)
	is_c = (move_candidate in c_point) and (puttable >= 2)
	print("Is candidate X? " + str(is_x))
	print("Is candidate C? " + str(is_c))

	if is_x:
		for p in sorted_move:
			if p not in x_point:
				move_candidate = p
				print("candidate updated to " + str(p))
				is_c = (move_candidate in c_point) and (puttable >= 2)
				print("Is candidate C? " + str(is_c))

	elif is_c:
		for p in sorted_move:
			if p not in c_point:
				return p
	else:
		for i in range(len(sorted_move)):
			p = sorted_move[i]
			print(p)
			print("Can AI get corner? " + str(p in corner))
			if p in corner:
				return p
			else:
				continue

		return move_candidate