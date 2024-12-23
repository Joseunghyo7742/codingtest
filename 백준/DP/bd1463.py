# 1로 만들기
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
#연산을 사용하는 횟수의 최솟값

# 점화식 찾기 - 초기값정의하기 

# n= int(input())
# d=[0]*10000005
# d[1]=0

# for i in range(2,n+1):
#   d[i]= d[i-1]+1
#   if(i%2==0): d[i]=min(d[i], d[i//2]+1)
#   if(i%3==0): d[i]=min(d[i],d[i//3]+1)

# print(d[n])

n= int(input())

d=[0,0]

for i in range(2,n+1):
  d.append(d[i-1]+1)
  if(i % 2 ==0):
    min_value= min(d[i//2]+1, d[i])
    d[i]=min_value
  if( i % 3 ==0):
    min_value=min(d[i//3]+1,d[i])
    d[i]= min_value  
print(d[n]) 
  
