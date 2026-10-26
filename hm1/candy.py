def kidsWithCandies(candies: list[int], extraCandies: int):
    tr=[]
    for i in range(len(candies)):
        if i==0:
            tr.append(True)
        elif candies[i]+extraCandies>max(candies):
            tr.append(True)
        else:
            tr.append(False)
    return tr

