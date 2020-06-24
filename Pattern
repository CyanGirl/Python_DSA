def print_rangoli(size):
    
    max_length,max_width=(4*size)-3,2*size-1
    index_pos=max_width
    move=index_pos
    times=count=1
    
    for i in range(1,max_width+1):
        alphabet=96+size
        for j in range(1,max_length+1):
            if(move==j and count>0):
                print(chr(alphabet),end="")
                move,count=move+2,count-1
                alphabet=(alphabet-1) if count>int(times/2) else (alphabet+1)
            else:
                print("-",end="")
            
        index_pos,times=(index_pos-2,times+2) if i<size else (index_pos+2,times-2)
        move,count=index_pos,times
        
        print()
    

print_rangoli(8)
