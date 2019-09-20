# AStar
A* is a pathfinding algorithm that uses heuristics to find the shortest path from a start to a goal. 
This project implements various versions of A* from scratch to help a computer agent solve a previously unseen maze. 

## Using the code 

### Relevant Files
#### 1. Maze.py
##### generate_actual_maze(self, size):
Generates a random maze of inputted size, where on average 30% of cells are blocked and 70% are open. 
##### generate_blank_maze(self, size):
A blank maze is generated where all cells are marked as open. This maze represents the computer agent's initial knowledge of the actual maze.
#### 2. RepeatedAlgo.py
RepeatedAlgo.py not only finds the quickest path on the agent's map, but then tests this path on the actual maze. If an obstacle is found on the actual maze using  the calculated path, the agent moves to the obstacle, marks this obstacle on it's own maze, and then recalculates another path using it's newly improved map. 
#### 3. SolveMaze.py
This code contains two types of A* algorithms:
##### forward_A_star(self, start_node,  goal_node, w):
A modification on breadth/depth first search where cells with the lowest f-values are visited first. F-values are the sum of the distance from the start to current cell and Manhattan distance estimate from current cell to the goal.
```
f = g+h
g = sum of cell costs from start to current cell
h = | cell.x - goal.x | + | cell.y - goal.y | = Manhattan distance
f in effect estimates the path's length
```
##### adaptive_A_star(self, start_node, goal_node, lastClosedList, w):
Distance from the start to goal of the previous A* search is saved.
A modification on forward A* where cells where f-values are the sum of the distance from start to current cell and distance to goal (calculated as previous search's distance from start to goal minus distance from start to current cell). 
```
f = g+h
g = sum of cell costs from start to current cell
For the first search: 
h = | cell.x - goal.x | + | cell.y - goal.y | = Manhattan distance 
For consecutive searches: 
h = (last search's path length) - g
f in effect estimates the path's length, taking into account any obstacle's encountered in the previous searches
```
#### 2. Metrics.py 
This code processes the raw images and labels from the Images file. Additionally, it pickles (serializes) the processed images and labels to be instantly used during runtime without having to process them ever again. These processed images and labels are saved under ProcessedData in Images. 
#### 8. Visual.py
Perceptron.py does is the core of this project as it is the learning algorithm itself. It not only trains the algorithm to classify the training images based on training labels, but also tests the algorithm's "knowledge" on a separate set of test images and test labels. 
#### 9. UserInterface.py
Perceptron.py does is the core of this project as it is the learning algorithm itself. It not only trains the algorithm to classify the training images based on training labels, but also tests the algorithm's "knowledge" on a separate set of test images and test labels. 

### Installation and Running
- Download as zip
- Unzip file
- Open file in your preferred source code editor that supports Python 
- Run Interactive.py
- Follow the commands in the terminal window to see results 

### Dependencies
Numpy (should already be included in the zip) 
If you receive an error which states that numpy module cannot be found, download numpy by typing the following in the terminal using: 
```
pip install numpy
```

## Theory
### Feature Extraction in ProcessData.py
The raw partially processed images are represented using 3 characters: ' ', '+', '#'.
##### Digit Example
```
                            
             ++###+         
             ######+        
            +######+        
            ##+++##+        
           +#+  +##+        
           +##++###+        
           +#######+        
           +#######+        
            +##+###         
              ++##+         
              +##+          
              ###+          
            +###+           
            +##+            
           +##+             
          +##+              
         +##+               
         ##+                
        +#+                 
        +#+                 
                            
```
##### Face Example
```
                                                            
 ####                                                       
     ###                      #                             
        ####                ## #                            
            ######         #    #                           
                  #########      ######                     
 #                                     ##                   
  #                #         ##          #                  
  #               #         #  #          #                 
  #               #         #   #          #                
 #                 #  ######    #          #                
 #                  ##          #           #               
 #                 #            #            #              
 #             ####                           #             
                                              #             
             #                                #             
            #      ###############            #             
           #      #               ####       #              
           #     #                    #     #               
          #     #                      #    #    #          
          #     #                       #        #          
          #    #                         #       #          
          #    #                         #        #         
         #     #                          #       #         
         #    #                           #       #         
         #    #                           #       #         
 #       #    #                           #      #          
 #       #   #                   ######   #      #          
 #       #   #   #    ##      ###          #     #          
 #        #  #    #     ###  #             #     #          
 #        #  #     ##       #       #      #     #          
 #        #  #    #  #      #     ##       #    #           
  #       #  #       #      #    #         #    #           
  #       #   #   #  #      #    #         #    #           
  #       #   #  # ##       #     #####   #    #            
  #           #             #   #         #   ##            
  #           #        #    #   #         #  #  #           
  #           #        #    #   #        #   #  #        ## 
  #            #      #     #   #        #  #   #       #   
               #      #     #   #        #  #  #       #    
               #      #    #   #        #   #  #       #    
               #      #    #   #        #  #   #       #    
             # #      #    #  ##        #  #  #        #    
 #          #  #      #     ##  #       #     #        #    
 #          #        #                  #    #         #    
 #           #       #                  #   #           #   
 #            #      #   ########       # ##            #   
 #             #     #           #      #               #   
 #              #     #         #      #        #       #   
 #              #      ##     ##      #         #       #   
 #              #        #####       #    #     #       #   
 #               #                  #     #    #       #    
 #               #                 #      #    #       #    
 #                ####           ##        #   #       #    
 #                    ##      ###          #   #       #    
                  #     ######         #   #           #    
                  #                   #     #          #    
                 ###                  #   #  #         #    
                #                     #   #  #          #   
               #     #               #     #  #         #   
               #     #              #          #        #   
              #       #  ######    #        #   #           
             #         ##      ####        #     ##         
             #   #                         #       ###      
           ##    #                        #           ##    
         ##      #                        #             #   
        #         #                      #               ## 
      ##          #                      #                  
    ##             #                    #                   
                                                            
```
For both the faces and digits, I scanned each line of the respective .txt file, and matched each character present with a numerical value:
‘ ‘   =  0
‘+’  = .5
‘#’  =  1
The numbers from 0 to 1 represent the darkness of the image at that point. 0 means it is completely white, 1 means it is completely black. 
I simply took the numerical value of each character in the file and added it to a numpy vector. For the digits, each digit was represented in the .txt file using 28x28 characters, therefore our feature was a 784x1 vector (28x28=784) filled with 0,.5, and 1 at the appropriate location. Similarly, for the faces, which were represented using 70x60 characters, we had a 4200x1 vector.

### How the computer learns in Perceptron.py
Perceptron uses linear regression techniques to properly classify images. We train the computer to make a line that takes an x value, and passes it through a linear function to output an y value. The x value is the extracted feature, and the y value is the computer’s prediction of the label. The learning algorithm continuously changes this line’s placement in space and its slope in a multidimensional coordinate system until the error between the prediction and label is minimized. 

###
For a more detailed explanation and analysis of this project click [here](Perceptron.pdf). 

## Author
Bharti Mehta
