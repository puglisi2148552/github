'challenge 1'

def maximumPerimeterTriangle(sticks):
    # Step 1: Sort the stick lengths in descending order
    sticks.sort()
    i= len(sticks) -3
    while i >= 0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
        i -= 1
    
    if i >= 0:
        return [sticks[i], sticks[i+1], sticks[i+2]]
    else:
        return[-1]
