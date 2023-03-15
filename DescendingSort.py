A = [21,4,25,36,2,5,5,1]
def DescendingSort(text) :
    text.insert(0,0)
    #[0, 21,4,25,36, 2,5, 5,1]
    j = 1
    #key = 21
    for j in range (len(text)) :
        key = text[j] 
        i = j - 1
        while (text[i] < key and i > 0) :
            #1st run 21 > 4 j = 2
            text[i+1] = text[i]
            #text[1] = text[2]
            #text[1] = 4
            i = i-1 
        text[i+1] = key
    return(text)
print(DescendingSort(A))