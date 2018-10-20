_ = input()
seq = list(map(int,input().split()))
 
seq1 = seq[::2]
seq2 = seq[1::2]
 
if len(set(seq)) == 1:
    print(len(seq2))
    exit()
    
def count_dictonary(seq):
    ret_dict={}
    for item in seq:
        if item not in ret_dict:
            ret_dict[item] = 1
        else:
            ret_dict[item]+=1
    return ret_dict
 
def modes(counting_dict):
    #(11,2),(2,1),(3,3)
    ret={}
    for item in counting_dict.items():
        no, count = item
        if counting_dict[no] in ret:
            ret[count].append(no)
        else:
            ret[count]=[no]
            
    return ret
 
 
counting1 = count_dictonary(seq1)
counting2 = count_dictonary(seq2)
 
modes1 = sorted(modes(counting1).items(),reverse=True)
modes2 = sorted(modes(counting2).items(),reverse=True)
 
min_change=len(seq)
if modes1[0][1] != modes2[0][1] or len(modes1[0][1]) >=2 or len(modes2[0][1]) >=2:
    min_change = (len(seq1) - modes1[0][0]) + (len(seq2) - modes2[0][0])
else:
    m01=len(seq)
    m10=len(seq)
    if len(modes2) !=1:
        m01 =  (len(seq1) - modes1[0][0]) + (len(seq2) - modes2[1][0])
    if len(modes1) !=1:
        m10 =  (len(seq1) - modes1[1][0]) + (len(seq2) - modes2[0][0])
    min_change = min(m01,m10)
    
print(min_change)