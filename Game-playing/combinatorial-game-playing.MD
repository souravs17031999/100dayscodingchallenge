# Game of Piles (NIM-GAME)
# PART - I
So, we can conclude that this game depends on two factors-

The player who starts first.
The initial configuration of the piles/heaps.
In fact, we can predict the winner of the game before even playing the game !

Nim-Sum : The cumulative XOR value of the number of coins/stones in each piles/heaps at any point of the game is called Nim-Sum at that point.

“If both A and B play optimally (i.e- they don’t make any mistakes), then the player starting first is guaranteed to win if the Nim-Sum at the beginning of the game is non-zero. Otherwise, if the Nim-Sum evaluates to zero, then player A will lose definitely.”

# PART - II
What is Mex?
‘Minimum excludant’ a.k.a ‘Mex’ of a set of numbers is the smallest non-negative number not present in the set.
How to calculate Grundy Numbers?
We use this definition- The Grundy Number/ nimber is equal to 0 for a game that is lost immediately by the first player and is equal to Mex of the nimbers of all possible next positions for any other game.

Below are three example games and programs to calculate Grundy Number and Mex for each of them.
# PART -III
Example 1
The game starts with a pile of n stones, and the player to move may take any positive number of stones. Calculate the Grundy Numbers for this game. The last player to move wins. Which player wins the game?

Since if the first player has 0 stones, he will lose immediately, so Grundy(0) = 0

If a player has 1 stones, then he can take all the stones and win. So the next possible position of the game (for the other player) is (0) stones

Hence, Grundy(1) = Mex(0) = 1 [According to the definition of Mex]

Similarly, If a player has 2 stones, then he can take only 1 stone or he can take all the stones and wins. So the next possible position of the game (for the other player) is (1, 0) stones respectively.

Hence, Grundy(2) = Mex(0, 1) = 2 [According to the definition of Mex]



Similarly, If a player has ‘n’ stones, then he can take only 1 stone, or he can take 2 stones…….. or he can take all the stones and win. So the next possible position of the game (for the other player) is (n-1, n-2,….1) stones respectively.

Hence, Grundy(n) = Mex (0, 1, 2, ….n-1) = n [According to the definition of Mex]
# PART - IV
Suppose we change the classic Nim game a bit. This time each player can only remove 1, 2 or 3 stones only (and not any number of stones as in the classic game of Nim). Can we predict who will win?

Yes, we can predict the winner using Sprague-Grundy Theorem.

Suppose there is a composite game (more than one sub-game) made up of N sub-games and two players, A and B. Then Sprague-Grundy Theorem says that if both A and B play optimally (i.e., they don’t make any mistakes), then the player starting first is guaranteed to win if the XOR of the grundy numbers of position in each sub-games at the beginning of the game is non-zero. Otherwise, if the XOR evaluates to zero, then player A will lose definitely, no matter what.
# PART - V
We can apply Sprague-Grundy Theorem in any impartial game and solve it. The basic steps are listed as follows:

Break the composite game into sub-games.
Then for each sub-game, calculate the Grundy Number at that position.
Then calculate the XOR of all the calculated Grundy Numbers.
If the XOR value is non-zero, then the player who is going to make the turn (First Player) will win else he is destined to lose, no matter what. 
