[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/aNJ3798x)
# PS6

Hello and welcome to your **FINAL PROBLEMSET**

This one will be very different from the others for a few reasons. Firstly, this ps is **optional** and will replace the lowest grade of your ps catagory.

Additionally, this will not give you partial code to go off of, just an empty function and tests. 
The point of this is to give you all a chance to use your new programming skills to solve some real world problems
and make judgments on how to best do it! There is no one correct way.




## Problem 1 Balancing Power:


There are n legislators in the State of Confusion, each representing one of the three major parties:

**Future One**, **Two-gether**, and **Triple Harmony**.


The founders of the State envisioned a healthy society where the three parties maintain the balance
of power and no party gets a dictatorial position by having too many legislators. 

Formally, we say that the balance of power is achieved when no one party has strictly more legislators than the other two parties
combined.

For example:

If **Future One** has **3**, **Two-gether** has **2**, then **Triple Harmony** must have no more than **4** to be balanced.


As the major election cycle for the State of Confusion is wrapping up, every journalist from the media
is rushing to be the first to report the outcome. Fortunately, you, a journalist from the Profound Confusion
Network, have some programming experience. 

Instead of counting and doing the math on paper, you decide
to write a program to help you write an article. You will simply provide the party aﬃliation of the election
winners, and the program will report whether the balance of power is achieved or not.

The function input will have **2** paramaters. The first will be the total number of legislators (n), the second will be n space-separated
integers, representing the party aﬃliation of each elected person, 1 being Futre One, 2 being Two-gether, 3 being Triple Harmony.

The function will output a string on a single line, representing the headline of the article you will write. 

If the balance of power is achieved, then print only “Power Balanced” without quotation marks. Otherwise,
print only “[Party] Dominates” without quotation marks, where “[Party]” is replaced with the name of the
winning party. Note that the output is case-sensitive, and must match the format exactly without leading
or trailing whitespace.


Sample Use:


is_power_balanced(5, "1 2 1 3 1")

This should return 


"Future One Dominates"

## Problem 2 Intuitive Abbreviations:

Brandon is learning the periodic table! 

However, he **doesn’t like** some of the elements because the symbol of the element **contains
letters which are not present in the name of the element**. He finds this to be
unintuitive, especially because in other contexts, he expects abbreviations to not introduce random letters.


Given a string and a proposed abbreviation, determine if Brandon **would** find it intuitive. 

Brandon finds an abbreviation intuitive if and only if:

Every letter that appears in the abbreviation appears in the original string. 


Brandon **does not look at the abbreviation carefully**, so it is acceptable for a letter to appear more
times in the abbreviation than in the original string, or for the letters to appear in a diﬀerent order between
the string and the abbreviation.

Any letter could be lower or uppercase to start, but your return statement will be case sensitive.

The first paramater of the function will be a string with an element name. The second will be a proposed abbreviation.


For each test case, if all the letters in the abbreviation appear in the name, return a line containing the string “YES”. Otherwise,
return a line containing the string “NO”.

Sample Use:

is_intuitive("Oxygen", "Ogn")

This should return "YES"

is_intuitive("Oxygen", "Od")

This should return "NO"


## Problem 3 Xylophone:

A xylophone is a musical instrument made of wooden bars, each of which makes a specific pitch when
struck with a mallet. 

The wooden bars must have contiguous integer lengths from the longest to the shortest,
without duplicates. In other words, every bar except for the rightmost one must have a length exactly 1
longer than the one immediately to its right. 

For example, a xylophone may have bars of lengths [7, 6, 5, 4]
or [10, 9, 8], but not [7, 5, 4] nor [3, 3, 2, 1].


You already have 3 wooden bars of diﬀerent lengths, and want to create a xylophone using all of them.


You may **not** cut the bars or alter them in any way, but you **may buy additional wooden bars** as necessary.
The cost of buying a wooden bar is equal to its length. 

**Find the minimum cost to build a xylophone**

The only paramater is a string with three space-separated integers, each number is the length of a bar you already have.

You are guaranteed that the three integers are distinct.

Your program must return a single integer that represents the minimum cost to make a xylophone using
all three given wooden bars.

Sample Use:

cost_of_bars("1 4 2")

This should return **3** as the cost


## GRADING

Only **2** problems need to be completed for full credit. Pick the ones that stand out to you most!

Same as usual where your passing tests will be how you are graded!

DELETE THE FILE AND THE TEST FILE FOR THE PROBLEM YOU DO NOT WANT TO COMPLETE