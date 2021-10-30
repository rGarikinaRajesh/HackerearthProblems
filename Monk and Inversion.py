for _ in range(int(input())):
    n=int(input())
    lis=[]
    lis2=[]
    for i in range(n):
        k=list(map(int,input().split()))
        lis.append(k)
        lis2+=k
    count=0
    if(sorted(lis2)==lis2):
        print(0)
    else:
        for i in range(n):
            for j in range(n):
                p=i
                print(lis[i][j],end="->")
                while(p<n):
                    q=j
                    while(q<n):
                        print(lis[p][q])
                        if((lis[i][j]>lis[p][q]) and (i<=p and j<=q)):
                            count+=1
                        q+=1
                    p+=1
        print(count)
            



            
    
