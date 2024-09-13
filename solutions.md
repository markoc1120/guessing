## Exercise: Prove that all three strategies terminate and with the correct answer, i.e. they are algorithms for solving this problem. + Exercise: Would you judge all three approaches to be equally efficient in finding the right number? If not, how would you order the three strategies such that the method most likely to get the correct number first is ranked highest, and the algorithm most likely to get the right number last is rated lowest. Justify your answer.

1. Start with one. If it isn't the right number, it has to be too low--there are no smaller numbers the right one could be. So if it isn't one, you guess it is two. If it isn't, you have once again guessed too low, so now you try three. You continue by incrementing your guess by one until you get the right answer.

- Obviously this algorithm would get the right answer, but it has a O(n), so there is a more efficient way to handle it.

2. Alternatively, you start at 20. If the correct number is 20, great, you got it in one guess, but if it is not, your guess must be too high it cannot possibly be too small. So, you try 19 instead, and this time you work your way down until you get the right answer.

- The same problem occurs here like in the first one, O(n) not the most efficient.

3. Tired of trying all numbers from one end to the other, you can pick this strategy: you start by guessing 10. If this is correct, you are done, if it is too high, you know the real number must be in the interval [1,9], and if the guess is too low, you know the right answer must be in the interval [11,20]—so for your next guess, you pick the middle of the interval it must be. With each new guess, you update the range where the real number can hide and choose the middle of the previous range.

- This is the most efficient way to guess the number, O(log2(n))
