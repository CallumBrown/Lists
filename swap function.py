list_ = ["b","a","c","w","j","y"]



for count in range (len(list_)):
    for count1 in range(count+1, len(list_)):
        
        if list_[count] > list_[count1]:
            temp = list_[count]
            list_[count] = list_[count1]
            list_[count1]=temp
        
print(list_)

    
