
n, m , k = map(int, input().split()) # n,m,k map함수로 int로 입력받기

list = list(map(int,input().split())) # 리스트로 입력받기
cnt = 0
sol = []

for i in range(m) :
    if cnt >= k :
        list.remove(sol[-1])
        sol.append(max(list))
        list.append(sol[-2])
        cnt = 1
    
    else:    
        sol.append(max(list))
        cnt += 1
        

print(sum(sol))
    

