# CMPT 317, Assignment 1, Question 5
# Paolo Fenu, 10281648
# Sept 27th, 2019
#
# Mac OS Mojave Version 10.14.6
# Python

import InformedSearch as iSearch
import Problem as P

# create variables to track/calculate stats for tables
totalUcssNodes = 0.0
totalUcssSpace = 0.0
totalUcssSuccess = 0.0
totalUcsstime = 0.0
aveUcssDepth = 0.0
counter = 0.0

totalGbfNodes = 0.0
totalGbfSpace = 0.0
totalGbfSuccess = 0.0
totalGbftime = 0.0
aveGbsDepth = 0.0

totalAssNodes = 0.0
totalAssSpace = 0.0
totalAssSuccess = 0.0
totalAsstime = 0.0
aveAssDepth = 0.0

# open and read file. Put each line into a list then pass the values of each line through respective serch
file = open("c_hard.txt", "r")
p = P.Problem()
parameters = []
for lin in file.readlines():
    #print lin
    for val in lin.split():
        parameters.append(int(val))
    print "problem ", parameters[0]
    getN = parameters[1]
    getM = parameters[2]
    getList1 = []
    getList2 = []
    listLength = getN * getM
    for x in range(3, listLength + 3):
        getList1.append(parameters[x])
    for x in range(3, listLength + 3):
        getList2.append(parameters[x + listLength])
    parameters = []
    s = P.State(getList1, getList2, getN, getM)

    #Pass tests through various searches. Tally info for space, time, successes and depth
    searcher = iSearch.InformedSearch(p, 10)
    result = searcher.UCSSearch(s)
    counter +=1.0
    print "UCS: ", (str(result))
    totalUcsstime += result.time
    totalUcssNodes += result.nodes
    totalUcssSpace += result.space
    parent = result.result
    if(result.success is True):
        totalUcssSuccess += 1.0
        aveUcssDepth += P.SearchNode(s, parent, 1).depth

    result = searcher.BestFirstSearch(s)
    print "GBF:, ", (str(result))
    parent = result.result
    totalGbfNodes += result.nodes
    totalGbfSpace += result.space
    totalGbftime += result.time
    if (result.success is True):
        totalGbfSuccess += 1.0
        aveGbsDepth += P.SearchNode(s, parent, 1).depth

    result = searcher.AStarSearch(s)
    print "A-star: ", (str(result))
    parent = result.result
    totalAssNodes += result.nodes
    totalAssSpace += result.nodes
    totalAsstime += result.time
    if (result.success is True):
        totalAssSuccess += 1.0
        aveAssDepth += P.SearchNode(s, parent, 1).depth

# Calculate various values for table and display them
print "Average Space UCSSearch: ", (totalUcssSpace/counter), " Average depth UCSSearch: ", \
      0 if totalUcssSuccess == 0 else aveUcssDepth/totalUcssSuccess, " Total Successes UCSSearch: ", totalUcssSuccess,\
    "Total A-Star time: ", totalAsstime/counter

print "Average Space Greedy Search: ", (totalGbfSpace/counter), " Average depth BestFirstSearch: ", \
      0 if totalGbfSuccess == 0 else aveGbsDepth/totalGbfSuccess, " Total Successes BestFirstSearch: ", totalGbfSuccess, \
    "Total GBFS time: ", totalGbftime/counter

print "Average Space AStarSearch: ", (totalAssSpace/counter), " Average depth AStarSearch: ", \
      0 if totalAssSuccess == 0 else aveAssDepth/totalAssSuccess, " Total Successes AStarSearch: ", totalAssSuccess, \
    "Total A-Star time: ", totalAsstime/counter


file.close()



