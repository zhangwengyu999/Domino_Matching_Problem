# Made by Mike_Zhang
# https://ultrafish.cn
# Domino Matching Problem
def isMatchedDomino(inDomino):
    """
    function to check whether this Domino is matched

    parameter:
        - inDomino: Domino to check
    return:
        - True: it is matched
        - False : it is NOT matched
    """
    upperList = []
    lowerList = []
    for d in inDomino:
        upperList.append(d[0])
        lowerList.append(d[1])
    upper = "".join(upperList)
    lower = "".join(lowerList)
    if (len(upper)==len(lower)):
        if (upper == lower):
            return True
        else:
            return False
    return False

def isPartialMatched(inDomino):
    """
    function to check whether a part of this Domino is matched, part refers to the longest part of a Domino having same lenth of upper half and lower half part
    e.g., [["a","ab"],["b","ca"]] is Partially Matched, [["a","ab"],["b","ca"],["ca","a"],["abc","c"]] is NOT Partially Matched

    parameter:
        - inDomino: Domino to check
    
    return: 
        - mark:
            - True: Partially Matched
            - False: NOT Partially Matched
    """
    upperList = []
    lowerList = []
    for d in inDomino:
        upperList.append(d[0])
        lowerList.append(d[1])
    upper = "".join(upperList)
    lower = "".join(lowerList)
    i = min(len(upper),len(lower))-1
    mark = True
    while(mark == True and i >= 0):
        if (upper[i] != lower[i]):
            mark = False
        i=i-1
    return mark

def getStartDominoList(inDominoList):
    """
    function to get a list of Dominos that each one is partially matched Domino
    e.g. getStartDominoList([["010","0"],["111","000"],["001","0101"],["11","10110"]]) = [["010","0"]]
    getStartDominoList([["b","ca"],["abc","c"],["a","ab"],["ca","a"]]) = [["a","ab"]]
    
    the first Domino in a matched Domino must be selected from that list of Dominos

    parameter:
        - inDominoList: a list of Dominos to check
    return:
        - a list of required Dominos
    """
    resultList = []
    for d in inDominoList:
        if (isPartialMatched([d])):
            resultList.append(d)
    return resultList

def isNextDominoValid(inDomino,inNext,Dominos):
    """
    the CORE function 
    to recursively check whether next Domino can generate a matched Domino after appending to the original Domino,
    and finally modify the original Domino to a matched Domino, if can generate.

    parameter:
        - inDomino: the original Domino
        - inNext: the next Domino 
        - Dominos: all given Dominos
    return:
        - flag: 
            - True: can generate a matched Domino
            - False: can NOT generate a matched Domino
    """
    flag = False
    inDomino.append(inNext)
    if (isMatchedDomino(inDomino) == True):
        flag = True
    elif (isPartialMatched(inDomino) == False):
        flag = False
        inDomino.pop()
    else:
        for d in Dominos:
            if (isNextDominoValid(inDomino,d,Dominos)):
                flag = True
                break
    return flag

def main():
    Dominos = [["b","ca"],["abc","c"],["a","ab"],["ca","a"]]
    #Dominos = [["010","0"],["111","000"],["001","0101"],["11","10110"]]
    #Dominos = [["001","00"],["0","100"]]

    flag = False
    resultDominos = list()
    startDominoList = getStartDominoList(Dominos)

    if (len(startDominoList) == 0):
        flag = False
    else:
        for startDomino in startDominoList:
            tmpList = list()
            tmpList.append(startDomino)
            for d in Dominos:
                if (isNextDominoValid(tmpList,d,Dominos)):
                    resultDominos = tmpList
                    flag = True
                    break
    if (flag == True):
        print("Yes, exist a solution:")
        print(resultDominos)
    else:
        print("No, not exist any solutions")

main()
# Made by Mike_Zhang
# https://ultrafish.cn
# Domino Matching Problem