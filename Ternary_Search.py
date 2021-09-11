#assuming the arr is in ascending order sort
#complexity of this is O(log3n)

def ternary_search(arr,num):
    
    l,r=0,len(arr)-1
    
    while r>=l:
        
        # dividing the arr into three parts
        mid1=l+((r-l)//3)  # finding the first mid
        mid2=r-((r-l)//3)  # Finding the second mid
        
        # if already found, returns the index
        if arr[mid1]==num:
            return mid1
        elif arr[mid2]==num:
            return mid2
        
        # if not found, elimate the part not needed
        
        if num<arr[mid1]:  # if num is in first part
            r=mid1-1
            
        elif num>arr[mid2]:  # if num is in last part
            l=mid2+1
            
        else:  #if num is in middle part
            l=mid1+1
            r=mid2-1

    return "Could not be found"


if __name__=="__main__":
    arr=[2,3,5,6,8,9,12,13,14]
    num=13
    print(ternary_search(arr,num))
    
    
