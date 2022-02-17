##m번 더할 수 있고 같은 수 k 까지 더할 수 있다면 가장 큰 수는 m//(k+1) + m%(k+1)번 만큼 더해진다.
#기본적으로 이문제에서는 걍 젤큰수 -두번째 큰수만 필요!

n,m,k = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
first = data[-1]
second = data[-2]

sol = 0
sol += (m//(k+1)*k + m%(k+1))*first
print(sol)
sol += (m//(k+1))*second
print(sol)

print(second)