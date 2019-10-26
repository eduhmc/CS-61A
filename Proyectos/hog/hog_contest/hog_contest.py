"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""
from hog import *
from decimal import *

PLAYER_NAME = 'Eduardo Huerta-Mercado' # Change this line!
GOAL = 100

MAX = 10

def memoize(f):
    memo = {}
    def helper(*args):
        key = (f, args)
        if not key in memo:
            memo[key] = f(*args)
        return memo[key]
    return helper

@memoize
def how_possible_to_win_now(score, opponent_score):
	result = Decimal(0)
	possibility = Decimal(0)
	aux_score = 0
	opponent_possibility = Decimal(0) # will apply to get my possibility with: opponent_possibility + my_possibility = 1
	opponent_n = 0
	if (score >= GOAL): #win game
		result =  1
	elif(opponent_score >= GOAL): #lose game
		result = 0
	else: #keep trying to win 
		if (is_swap(score,opponent_score) and (opponent_score > score)): #swap is benefitial
			aux_score = score
			score = opponent_score
			opponent_score = aux_score
			if (score >= GOAL): #win game
				result =  1
			else:
				opponent_n = highest_possibility(score, opponent_score)
				opponent_possibility = can_win_game(opponent_n, opponent_score, score)
				result = 1 - opponent_possibility
	return result


@memoize
def ways_to_score_x(x,n):
	if (x<=0):
		return pow(5,n)
	elif (n == 0):
		return 0
	else:
		sum_total = 0 
		i = 2
		while ( i <= 6 ):
			sum_total += ways_to_score_x(x - i, n - 1)
			i += 1
		return sum_total

@memoize
def how_possible_to_roll_x(x, n):
	return ways_to_score_x(x,n) / pow(6,n) #chance to score x rolling n = number of ways to score x / number of possible rolls


def time_trot(k,n):
	if (n % 5 == k):
		return True
	else:
		return False
def estimated_turn(n,score, opponent_score):
	estimated_1 = score / n
	estimated_2 = opponent_score / n

	return (estimated_1 + estimated_2) / 2

@memoize
def can_win_game(n, score, opponent_score):
	result = 0
	possibility = Decimal(0)
	#Verify exceptions
	if (n == 0): # free bacon case
		result = free_bacon(opponent_score)
		possibility = how_possible_to_win_now(result + score, opponent_score)
	elif(n>0): #all other cases
		#check time trot
		if (time_trot(n, estimated_turn(n,score, opponent_score))):
			score += roll_dice(1)
			can_win_game(n,score,opponent_score)
		#possibility = possibility to get number * possibility to win with that number
		for desired_score in range (1, (n*6) + 1 ):
			p_to_get_number = how_possible_to_roll_x(desired_score, n)
			p_to_win_with_number = how_possible_to_win_now(desired_score + score , opponent_score )
			possibility = possibility + (Decimal(p_to_get_number) * (p_to_win_with_number))  
	return possibility
	

@memoize
def highest_possibility(score, opponent_score):
	max_possibility =Decimal(0) 
	max_n = 0
	for n in range(0,MAX):
		final_possibility = can_win_game(n, score, opponent_score)
		if (final_possibility > max_possibility):
			max_possibility = final_possibility
			max_n = n
	return max_n


def final_strategy(score, opponent_score):
	#1: find amount of dice to get highest possibility to get a winning score  
	# Situations to consider: 
	# 	First exception: You take the lead, and the # of dice default will probably make you change your score with the opponent. 
	#					 Better to avoid that risk.
	# 	Second exception: You are losing, and there is another # of dice that will probably make you change your score with the opponent. 
	#					  It would be better to choose that # of dice.
	# 	Third exception: You have little to reach 100. Better to secure it using a few dice.
	#	Fourth exception: You are SO far behind in terms of the opponent that your only hope of winning is to exchange points. 
	#					  Better to choose your # of dice to achieve that at all costs.
	#	Fifth exception: You are SO ahead in scoring with respect to the opponent that his only hope of winning is to exchange scores with you. 
	#					  Better to avoid that at all costs, and choose your dice well to minimize that possibility.
	n = highest_possibility(score, opponent_score)
	
	#2: since you cant count turns, you can try to predict the actual turn (n) based on the actual scores. Take score and divide it by the average expected in each turn
	#	It will be helpful to apply the same with opponent_score to help predict the actual turn
	#	If n%5 equals 3 or 4, roll the dice n times to try to get an extra turn
	return n