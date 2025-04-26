def cost_of_bars(bars):
    """
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

    TODO: Find the minimum cost to build a xylophone

    The only paramater is a string with three space-separated integers, each number is the length of a bar you already have.

    You are guaranteed that the three integers are distinct.

    Your program must return a single integer that represents the minimum cost to make a xylophone using
    all three given wooden bars.
    """
    # Hint: The python sort() method can be used to sort a list of integers in ascending order.
    bars = bars.split()
    bars = [int(bar) for bar in bars] # looked online to find a way to convert a string of integers to a proper list / methods that I did prior didn't work
    bars = sorted(bars)
    
    total_cost = 0
    count = int(bars[0]) # starts our counter to the lowest integer in our given order

    while count < bars[2]: # continues until we reach the highest integer in our given order
        if count not in bars: # checks if integer is present in list
            total_cost += count # adds to total cost if integer is not in list
        count += 1
        
    return total_cost

# Run pytest test_problem_3.py to test the function