#Callum

def frequencey_array():
    list1 = []
    return list1


def simulate_throw(list1):
    for count in range(6):
        import random
        number = random.randlist(1,6)
        list1.append(number)
    return list1



def display(list1,number):
    count = 0
    count1 = 0
    print("{0:2} {1:2}".format("Scores","Frequency"))
    for each in list1:
        print("{0>:3} {0<:7}".format(count+1,list1[count1]))
        count = count1
        count1 = count1 + 1
    

def main():
    list1 = frequencey_array()
    number = simulate_throw(list1)
    display(list1,number)


main()


    












