def is_power_balanced(n, party):
    """
    There are n legislators in the State of Confusion, each representing one of the three major parties:

    Future One, Two-gether, and Triple Harmony.

    The founders of the State envisioned a healthy society where the three parties maintain
    the balance of power and no party gets a dictatorial position by having too many legislators.

    Formally, we say that the balance of power is achieved when no one party has strictly
    more legislators than the other two parties combined.

    The function input will have 2 paramaters. The first will be the total number of legislators (n), 
    the second will be n space-separated integers, representing the party aﬃliation of each elected person,
    1 being Futre One, 2 being Two-gether, 3 being Triple Harmony.

    The function will output a string on a single line, representing the headline of the article you will write.

    TODO: If the balance of power is achieved, then print only “Power Balanced” without quotation marks. 
    Otherwise, print only “[Party] Dominates” without quotation marks, where “[Party]” is replaced with the name of the winning party. 
    
    Note that the output is case-sensitive, and must match the format exactly without leading or trailing whitespace.
    """

    # max legsilators for balance
    MaxLegislators = int(n/2)

    # party lists
    FutureOne = []
    TwoGether = []
    TripleHarmony = []

    # reformt string into a list
    PartyAffiliation = party.split()

    # counts vote per party
    for i in PartyAffiliation:
        if i == '1':
            FutureOne.append('1')
        elif i == '2':
            TwoGether.append('2')
        elif i == '3':
            TripleHarmony.append('3')

    # checks for balance of power  
    if len(FutureOne) > MaxLegislators:
        return "Future One Dominates"
    elif len(TwoGether) > MaxLegislators:
        return "Two-gether Dominates"
    elif len(TripleHarmony) > MaxLegislators:
        return "Triple Harmony Dominates"

    # if all powers are balanced
    return "Power Balanced"

# Run pytest test_problem_1.py to test the function