from collections import Counter

nhas = int(input())
hcases = []
for x in range(nhas):
    hcases.append(input())

ncons = int(input())
ccases = []
for y in range(ncons):
    case = input()
    for hcase in hcases:
        #print(Counter(case), Counter(hcase))
        if Counter(case.replace(" ", "")) == Counter(hcase.replace(" ", "")):
            print("Yes: {}".format(hcase))
            break
    else:
        print("No: No matching case")

