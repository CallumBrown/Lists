#Callum

scores = ["18","23","36","21","58","40","45","59"]
count1 = 0
count2 = 1
max = "8"
for count1 in range (len(scores)-1):
    for count2 in range (len(scores)-1):
        if scores[count2] > scores[count2 + 1]:
            temp = scores[count2]
            scores[count2] = scores[count2 + 1]
            scores[count2 + 1] = temp
count = 0
for each in scores:
    print( "{0}.{1}".format(count+1,each))
    count = count + 1

        
