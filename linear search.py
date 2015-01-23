
#Callum Brown

##list_ = ["h","j","a","y","k","m","q"]    
##def swap_function(list_):
##    NoMoreSwap = False
##    while NoMoreSwap == False:
##        NoMoreSwap = True
##        for count in range(len(list_)-1):
##            if list_[count] > list_[count +1]:
##                NoMoreSwap = False
##                temp = list_[count]
##                list_[count] = list_[count+1]
##                list_[count+1] = temp
##    list2 = list_
##    return list2
##
##list1 = ["Kav","George","Callum"]
##def linear_search(list1,item_search):
##    found = False
##    count = 0
##    while not found and count <len(list1):
##        if list1[count] == item_search:
##            print("Found")
##            found = True
##        else:
##            print("Not Found")
##        count = count+1
##    return list1
##    
##
##def main():
##    item_search = input("Please enter the item you're searching for: ")
##    linear_search(list1,item_search)
##
##list2 = swap_function(list_)
##print(list2)
##    
##
##main()


string = input("Please input a sting: ")
character = input("Please enter a character: ")


count = 0
while count < len(string):
    if string[count] == character:
        print(character)
        
    else:
        print("-")
    count = count + 1




                      
                    

    



                  
        
