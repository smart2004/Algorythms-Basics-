# algorythms-Basics- by smart200481 <Mikhail Sutormin>

## builgings.py  
### Brief Task Description

Tim is looking for a place to build a house. The street he wants to live on has length n, it consists of n identical consecutive sections. Each plot is either empty or house already built on the place.
Sociable Tim does not want to live far away from other people on this street. Therefore, it is important for him to know for each plot the distance to the nearest empty plot. If the plot is empty, this value will be equal to zero - the distance to itself.
Help Tim calculate the required distances. For this putrpose you have a street map. Houses in the city of Timo were numbered in the order in which they were built, so their numbers on the map are not ordered in any way. Empty areas are marked with zeros.

### Input Format
  
The first line contains value, the length of the street —– n (1 ≤ n ≤ 106). 
The next line contains n non-negative integers — the numbers of houses and designations of empty plots on the map (zeroes). 
It is guaranteed that there is at least one zero in the sequence. House numbers (positive numbers) are unique and do not exceed 109.

### Output Format
  
For each segment, print the distance to the nearest zero. Output the numbers on one line, separating them with spaces.


### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Basics-.git
```

##### Switch to the folder:

```
cd algorythms-basics-
```

##### Launch python task:

```
python buildings.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
6
0 4 1 10 0 8
```
  
##### Example for output:
```
0 1 2 1 0 1
```
  

## hands_agility.py
### Brief Task Description

The "Speed Typing Trainer" is a sixteen-key 4x4 square keyboard. Each key can display either a dot or a number from 1 to 9.
The exercise on the simulator is divided into rounds:
- each round consists of several games;
- in different rounds, the number of games may be different;
- the number of each game in the round is indicated by the counter t.
  
For each round, certain values are set on the keys, which remain unchanged during all the games of the round.
The value of the game counter t cannot exceed the value of the largest number displayed on the keyboard in the current round.
Two players take part in the exercise on the simulator, they play together on the same keyboard. For each round, the maximum number of keys that one player can press is set (it is denoted by the variable k and does not change during the round).
In each individual game, the participants must press the keys together, on which the number corresponding to the number of the game t is displayed. For example, in the second game of a round, players must press all those keys that show a deuce.
There may be games in the round where you do not need to press buttons: for example, in the above version of the round in games from t = 4 to t = 8, you do not need to press buttons: there are no numbers from 4 to 8 on the keyboard.
If in the next game the participants have the opportunity to press all the necessary keys, they press them and get 1 point.
Let's assume that for the round a set of buttons is given, as in the picture, and k = 3 (each of the participants can press no more than three buttons). Then in the second game (t = 2), where twos must be pressed, two players can only press 6 keys together (k * 2 = 6). But there are seven twos on the keyboard; participants will not be able to click all of them and will not receive a point.
  
Write a program that will receive data for a specific round:
- k value,
- values for buttons,
and calculate the number of points that will be earned in this round.
  
### Input Format
  
The first line contains an integer k (1 ≤ k ≤ 5).

The next four lines set the values for the buttons—4 characters per line. Each character is either a dot or a number from 1 to 9. The characters on the same line are consecutive and are not separated by spaces.

### Output Format
  
Print a single integer, the number of points the players will score in the round.

### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Basics-.git
```

##### Switch to the folder:

```
cd algorythms-basics-
```

##### Launch python task:

```
python hands_agility.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
3
1231
2..2
2..2
2..2
```
  
##### Example for output:
```
2
```  
