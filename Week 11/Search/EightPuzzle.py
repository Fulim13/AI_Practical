# -*- coding: utf-8 -*-
"""
Best-first search and A* Search

This code is modified from the following source:
@author: Ghazanfar Ali, 2012. 8-Puzzle solving using the A* algorithm using Python and PyGame. 
Available at http://www.codeproject.com/Articles/365553/Puzzle-solving-using-the-A-algorithm-using-Pytho

Algorithm
==========
Get the current state of the scenario (refers to the puzzle).
Find the available moves and their cost using best-first or A*.
Choose the move with the least cost and set it as the current state.
Check if it matches the goal state, if yes terminate, if no move to step 1.
"""
##-----------------------------------------------------------------------------
## Setting up the puzzle
##----------------------------------------------------------------------------- 

import random

class Puzzle:
    def __init__(self):
        # self.StartNode = ['1', '2', '3', '5', '6', '8', '4', '0', '7'] # default, h(n) = 6
        # self.StartNode = ['7', '0', '2', '5', '8', '3', '1', '4', '6', 9] # default, h(n) = 9
        self.StartNode = ['1', '2', '3', '4', '5', '6', '0', '7', '8'] # Default, h(n) = 3
        self.GoalNode = ['1', '2', '3', '4', '5', '6', '7', '8', '0']  # default, h(n) = 0
        self.PreviousNode = [] # To store the expanded nodes
        self.Fringe = []       # To store the leaf nodes (or to be expanded nodes)
        self.Parent = []
       
    # location holds the location of the empty tile '0'
    def boundaries(self, location): 
        
        # location of each tile in the puzzle (assumption: the first location = 1 but not 0)
        rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
        
        low = 0
        high = 0
        
        # To determine the left/right boundaries of the empty tile '0' 
        # E.g., 0 is at the position of 9, then its left boundary is 7 and right boundary is 9
        for i in rows:  
            if location in i: # If the empty tile is on the row
                low = i[0]  # The left boundary
                high = i[2] # The right boundary
                break
        
        return [low, high] # Return the left and right boundary of the row that contains '0'
      
    # Successor function where self refers to the object that calls this function
    def successor(self, node = [], search = 'sahc'):

        subNode = []
        p = [] # The parent node list
        c = [] # The child node list
        
        # To get the location of the empty tile '0' which begins from 1 and end at 9
        getZeroLocation = node.index('0') + 1 
        
        # To join node to the end of subNode with node 
        # For instance, if subNode = ['a', 'b'] and node = [1, 2, 3], then the resulting subNode = ['a', 'b', 1, 2]
        # This is to ensure that the last item (which is the heuristic cost) is removed
        subNode.extend(node[0:-1]) 
        
        # To determine the left/right boundaries of the empty tile '0'
        boundary = self.boundaries(getZeroLocation)
        
        # To join node list to the end of p with the entire node
        p.extend(node)
        
        
        # Which strategy to be used, best first search or steepest ascent?
        if search == 'sahc':
            # Without this line turns the search to best first search because SAHC only looks at the surrounding nodes
            # The reason is the sahc will only consider the nearest surrounding neighbouring nodes as the next move
            # Whereas best first search will consider all possible nodes for the next move
            self.Fringe = [] 
        else:
            pass
        
        # The following 4 if-blocks are used to generate all possible successors of the current state/node
        # E.g., a node with '0' at 5 will have 4 child nodes, whereas a node with '0' at 1 will have 2 child nodes only
        
        # If the empty tile is at the top 2 rows, then move the empty tile DOWN [stop at here.....]
        if getZeroLocation + 3 <= 9:
            c = [] # Create an empty child list
            
            # Swap the location of 2 tiles: '0' and the tile right below it
            temp = subNode[node.index('0')] # Before swap happens, get a copy of the index value of the tile '0' 
            subNode[node.index('0')] = subNode[node.index('0') + 3] # Replace '0' with the tile right below '0'
            subNode[node.index('0') + 3] = temp # Replace the tile right below '0' with '0'
            
            # To join node to the end of c with node (excluding its last item)
            # Calling heuristics will return a node with the cost appended to the end of the list
            c.extend(self.heuristic(subNode))
            
            # Add the child node c to the fringe (which is also the frontier) to be expanded later 
            self.Fringe.append(c)
            
            # Reprocess subNode before it is processed in the following if-block
            subNode = [] 
            subNode.extend(node[0:-1])
            
            # Create a tuple with a pair of child and parent
            # E.g., c = [1, 2, 3] and p = [7, 8, 9]. then cp = (c, p) will create ([1, 2, 3], [7, 8, 9])
            cp = (c, p)           
            if (cp not in self.Parent):
                # Since there is only one object (referred to as self), all cp is appended to self.Parent from root node to goal node
                self.Parent.append(cp)
            # print("child-parent-pair:", cp)
        
        # If the empty tile is at the bottom 2 rows, then move the empty tile UP
        if getZeroLocation - 3 >= 1: 
            c = []
            
            temp = subNode[node.index('0')]
            subNode[node.index('0')] = subNode[node.index('0') - 3]
            subNode[node.index('0') - 3] = temp
            
            c.extend(self.heuristic(subNode))            
            self.Fringe.append(c)
            
            subNode = []
            subNode.extend(node[0:-1])
            
            cp = (c, p)            
            if (cp not in self.Parent):
                self.Parent.append(cp)
            # print("child-parent-pair:", cp)
        
        # If the empty tile is on the last 2 columns, then move the empty tile LEFT
        if getZeroLocation - 1 >= boundary[0]: 
            c = []
            
            temp = subNode[node.index('0')]
            # Swap the location of 2 tiles
            subNode[node.index('0')] = subNode[node.index('0') - 1]
            subNode[node.index('0') - 1] = temp
            
            c.extend(self.heuristic(subNode))
            self.Fringe.append(c)
            
            subNode = []
            subNode.extend(node[0:-1])
            
            cp = (c,p)
            if(cp not in self.Parent):
                self.Parent.append(cp)
            # print("child-parent-pair:", cp)
        
        # If the empty tile is on the first 2 columns, then move the empty tile RIGHT
        if getZeroLocation + 1 <= boundary[1]: 
            c = []
            
            temp = subNode[node.index('0')]
            subNode[node.index('0')] = subNode[node.index('0') + 1]
            subNode[node.index('0') + 1] = temp
            
            c.extend(self.heuristic(subNode))
            self.Fringe.append(c)
            
            subNode = []
            subNode.extend(node[0:-1])
            
            cp = (c,p)
            if(cp not in self.Parent):
                self.Parent.append(cp)
            # print("child-parent-pair:", cp) 

    # The heuristic function is used to calculate the number of misplacedTile (all of the 9 tiles including '0') as the cost
    # The goalNode has 0 misplaced tile
    def heuristic(self, node):
        misplacedTile = 0
        
        for i in range(9):
            # Compare the tile between the current node and the goalNode location by location
            if node[i] != self.GoalNode[i]:
                # If the tile is misplaced, increase the value one
                misplacedTile += 1 
        
        # Append the heuristic cost to the last place of node
        node.append(misplacedTile) 
        
        return node

##----------------------------------------------------------------------------- 
## Steepest-ascent hill climbing
##----------------------------------------------------------------------------- 
    def steepestAscentHillClimbing(self):
        print("STEEPEST ASCENT HILL CLIMBING\n" + "_"*60 + "\n")
        level = 0
        
        # The following two lines will add the heuristic cost to the end of the list
        currentNode = self.heuristic(self.StartNode) # Make the initial state as current state
        goalNode = self.heuristic(self.GoalNode) # Append the goal node heuristic cost
        
        #-------------------------------------------------------------------------------------------------
        
        # Check if the goal state is achieved or not, if not, generate child nodes from the current node
        if currentNode != goalNode:
            print("---------", "\nLEVEL", level, "\n---------")
            self.successor(currentNode) 
            level += 1 # Every time child nodes are generated, level is increased by 1
  
        print("CURRENT NODE:")
        print(currentNode)
        print("\nOPEN LIST:") # This is the frontier
        for i in self.Fringe:
            print(i) # This is the frontier
        
        # Pass the current heuristic cost as the argument by accessing the last element of the node
        nxNode = self.SAHC(currentNode[-1])
        
        #-------------------------------------------------------------------------------------------------
        
        # This loop begins from the child node of the ultimate first node, until either a goal node is found or no solution is found         
        while nxNode != [] and currentNode != goalNode and currentNode != nxNode:
            # The node that represents the best move is now the current node
            currentNode = nxNode
            
            print("\n---------", "\nLEVEL", level, "\n---------")
            self.successor(currentNode)
            level += 1
            
            print("CURRENT NODE:")
            print(currentNode)
            print("\nOPEN LIST:")
            for i in self.Fringe:
                print(i) # This is the frontier
            
            nxNode = self.SAHC(currentNode[-1])
            
            # Goal node is found, break out of the loop to stop generating child node
            if nxNode[-1] == 0:
                break        
                
        # print("\n", "-" * 60)
        # print("Initial State:", self.StartNode)
        # print("Goal State:", self.GoalNode)

        if nxNode != []:
            print()
            print("-" * 63)
            print("Goal Path (The best path)")
            print("-" * 63)
            self.printSolution()
        else:
            print("LOCAL MAXIMUM: There is no solution")

    # This function will return the best move as the next move (from all choices in the frontier)
    def SAHC(self, hrCost):
        nxNode = [] # The next node
        isBetter = False
        
        # Loop through frontier to search for the best successor based on hrCost (the lower the better)
        while True:   
            # temp = hrCost
            for i in self.Fringe: # Fringe (or frontier) contains all successors of the node (refer to successor function)
                if (i[-1] < hrCost): # If the cost of a child node is lesser (better) than the current node's one (which is the hrCost)
                    hrCost = i[-1]  # Then update the value of hrCost
                    nxNode = i    # Set the best node
                    isBetter = True 
            
            # if the best successor is chosen but it has already been chosen in the past...
            if nxNode in self.PreviousNode and nxNode in self.Fringe:
                # Then, remove it from frontier and go then through frontier to look for the second best successor
                self.Fringe.remove(nxNode) 
            # if the best successor is available and it is not in the PreviousNode list
            elif nxNode != []:
                if nxNode[-1] == 0:
                    print("\nSolution:", nxNode)
                else:
                    print("\nSelected:", nxNode)
                
                # The list of nodes in PreviousNode indicates how nodes are expanded from the beginning until the end
                self.PreviousNode.append(nxNode)
                
                # The best move is returned as the next move
                return nxNode 
            # if the best successor is not available            
            else:
                if isBetter == False:
                    print("\nThere is no better move")
                # An empty list is returned as the next move, indicating there is no better move
                return nxNode
        
##-----------------------------------------------------------------------------               
## Best first search
##----------------------------------------------------------------------------- 
    def bestFirstSolve(self):
        
        print("GREEDY BEST FIRST SEARCH\n" + "_"*60 +"\n")
        count = 0
        
        # The following two lines will add the heuristic cost to the end of the list
        currentNode = self.heuristic(self.StartNode)
        goalNode = self.heuristic(self.GoalNode)
        
        # To generate all successors, the 2nd argument will replace the default value of sahc
        self.successor(currentNode, 'bfs') 
        
        print("\n---------", "\nSTEP:", count, "\n---------")
        print("Current Node:", currentNode)
        print("\nOpen List:", self.Fringe) 
        
        nxNode = self.bestFirstSearch()
        count += 1
        
        while nxNode != [] and nxNode != goalNode and nxNode != currentNode:
            currentNode = nxNode
            print("\n---------", "\nSTEP:", count, "\n---------")
            print("Current Node:", currentNode)
            print("\nOpen List:", self.Fringe) # to display open nodes
            self.successor(nxNode, 'bfs')       # to generate next successor states
            nxNode = self.bestFirstSearch()    # search next best node
            count += 1                         # go to next step
       
        print("Final Goal:", nxNode, "\n")    # print the final goal
        print("-"*60, "\nHow the nodes are expanded\n", "-"*60)
        self.printSolutionSteps()
       
        print("\n", "-"*60)
        
        print("Initial State:", self.StartNode)
        print("Goal State:", self.GoalNode)
        print("\nGoal Path (the best path)")
        print("-"*60)
        self.printSolution()

    # Best first seach will select child node with the lowest heuristic cost from the fringe nodes
    def bestFirstSearch(self):
        nxNode = [] 
        
        while True:
            # The default value set for heuristic cost, the highest cost is still lower than this value
            hrCost = 100000
            
            for i in self.Fringe:    # For each open node in the fringe list
                if (i[-1] < hrCost): # The heuristic cost is the last member
                    hrCost = i[-1]   # Update heuristic cost
                    nxNode = i       # Set the best node to temporary node
            
            # If the temporary node is already in the PreviousNode list
            if nxNode in self.PreviousNode and nxNode in self.Fringe:
                self.Fringe.remove(nxNode) # Remove the temporary node from the open list
            # If it is not in the PreviousNode list  
            else:
                self.PreviousNode.append(nxNode) # Add the temporary node to PreviousNode list
                return nxNode  # Return the next node

##-----------------------------------------------------------------------------               
## Print solutions
##-----------------------------------------------------------------------------   

    # Functions to display output by showing how to yield the solution by observing the expanded nodes
    def printSolutionSteps(self):
        count = 1
        for i in self.PreviousNode:
            print("step ", count, i[0:-1], "(", i[-1], ")")
            count += 1
        
    # To show the final path
    def printSolution(self):
        
        # The path list will begin with a goal node
        # pathList = [goalNode]
        goal = self.GoalNode
        pathList = [goal] 
        
        # Reverse the sequence of the Parent list 
        # Before reverse: self.Parent = [(child-root-pair), (child-root-pair), ..., (goal-parentnode-pair)]
        # After reverse: self.Parent = [(goal-parentnode-pair), ..., (child-root-pair), (child-root-pair)]
        self.Parent.reverse()      
        
        # This loop will append parent of a node to pathList beginning from goal until root
        for i in self.Parent:  
            child, parent = i  # Unpack the child-parent pair
            if(child == goal): # If the first node is the goal node
                goal = parent  # Get its parent and set it as new goal
                pathList.append(goal) # Append the node to the path from the parent of goal node to the root node
            if parent == self.StartNode: # Stop when reach the startNode (the end of the list)
                break
        
        # Reverse the path list so that it begins with the startNode
        pathList.reverse() 
        
        count = 0
        for node in pathList:
            print("LEVEL", count, ":", node[0:-1], "(", node[-1], ")")
            count += 1
