import numpy as np
import random
import time
import os

def random_state(height,width):
#Creares a random board of 0s and 1s with the input dimensions heightxwidth
    dead_state=np.zeros((height,width),dtype=int)
    random_state=dead_state
    for i in range(height):
        for j in range(width):
            random_state[i][j]=random.randint(0,1)
    return random_state

def load_state(filepath):
#Creates a board of 0s and 1s from input file
    with open(filepath,'r') as f:
        lines=[l.rstrip() for l in f.readlines()]
    height=len(lines)
    width=len(lines[0])
    board=np.zeros((height,width),dtype=int)
    for x,line in enumerate(lines):
        for y,char in enumerate(line):
            board[x][y]=int(char)
    return board
                   
def render(state):
#Prints a nice looking rendered board of the input state
    print ("- " * state.shape[1])
    rendered_state=np.zeros((state.shape[0],state.shape[1]),dtype=str)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if state[i][j]==0:
                rendered_state[i][j]=" "
            else:
                rendered_state[i][j]=u"\u2588"
    row_counter=0
    while row_counter<state.shape[0]:
        print(*rendered_state[row_counter])
        row_counter+=1
    print ("- " * state.shape[1])

def next_state(state):
#Calculates de following board based in the input state with same dimensions
    next_state=np.zeros((state.shape[0],state.shape[1]),dtype=int)
    expanded_state=np.zeros((state.shape[0]+2,state.shape[1]+2),dtype=int)
    for i in range(1,state.shape[0]+1):
        for j in range(1,state.shape[1]+1):
            expanded_state[i][j]=state[i-1][j-1]
    for i in range(next_state.shape[0]):
        for j in range(next_state.shape[1]):
            neighbour_list=[]
            neighbour_list.append(expanded_state[(i+1)-1][(j+1)-1])
            neighbour_list.append(expanded_state[(i+1)-1][(j+1)])
            neighbour_list.append(expanded_state[(i+1)-1][(j+1)+1])
            neighbour_list.append(expanded_state[(i+1)][(j+1)-1])
            neighbour_list.append(expanded_state[(i+1)][(j+1)+1])
            neighbour_list.append(expanded_state[(i+1)+1][(j+1)-1])
            neighbour_list.append(expanded_state[(i+1)+1][(j+1)])
            neighbour_list.append(expanded_state[(i+1)+1][(j+1)+1])
            n_neighbour_alive=0
            for x in neighbour_list:
                if x==1:
                    n_neighbour_alive+=1
            
            if state[i][j]==1:
                if n_neighbour_alive<=1:
                    next_state[i][j]=0
                elif n_neighbour_alive>1 and n_neighbour_alive<=3:
                    next_state[i][j]=1
                elif n_neighbour_alive>3:
                    next_state[i][j]=0
            else:
                if n_neighbour_alive==3:
                    next_state[i][j]=1
    return next_state
         
            
    
#BEGINNING OF GAME

user_choice=input("Do you want initial state as a random state (press 1) or load from file (press 2):\n")    

while user_choice!="1" and user_choice!="2":
    print("Input not valid")
    user_choice=input("Do you want initial state as a random state (press 1) or load from file (press 2):\n")
    
if user_choice=="1":
#User manually introduces the size of the board
    height=int(input("Please introduce height of board:\n"))
    width=int(input("Please intoduce width of board:\n"))
#An initial random board is created
    board_state=random_state(height,width)
elif user_choice=="2":
#An initial board from file is created
    filepath=input("Please introduce name of file:\n")
    board_state=load_state(filepath)

#Print initial board
render(board_state)

n_games=0

while n_games<100:
    next_board_state=next_state(board_state)
    render(next_board_state)
    board_state=next_board_state
    time.sleep(0.005)
    n_games+=1
    clear = lambda: os.system('cls')
    clear()
    