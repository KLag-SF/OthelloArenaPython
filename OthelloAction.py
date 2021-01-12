import random
import AlphaBeta as ab
import sys

DEPTH = 6
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

	print("Candidate:" + str(move_candidate))

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
				print("Candidate updated to " + str(p))
				is_x = (move_candidate in x_point) and (puttable >= 2)
				if is_x:
					continue
				else:	
					is_c = (move_candidate in c_point) and (puttable >= 2)
					print("Is candidate C? " + str(is_c))
					break
			else:
				sorted_move.remove(p)
				print("Removed X from puttable table. :" + str(p))
				is_x = (move_candidate in x_point) and (puttable >= 2)

	if is_c:
		for p in sorted_move:
			if p not in c_point:
				move_candidate = p
				print("Candidate updated to " + str(p))
				is_c = (move_candidate in c_point) and (puttable >= 2)
				is_x = (move_candidate in x_point) and (puttable >= 2)
				if is_c:
					continue
				elif is_x:
					continue
				else:
					break
	
	for i in range(len(sorted_move)):
		try:
			p = sorted_move[i]
			print(p)
			print("Can AI get corner? " + str(p in corner))
			is_x = (move_candidate in x_point) and (puttable >= 2)
			if p in corner:
				return p
			elif is_x:
				sorted_move.remove(p)
			else:
				continue
		except IndexError:
			break

	return move_candidate