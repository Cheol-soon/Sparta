test = int(input())


def calc(n, i,current_cal, max_cal,taste_rank):
    if i>n or current_cal >max_cal:
        return taste_rank[i][0]
    result1 = current_cal + calc(n,i+1,result1,max_cal,taste_rank)
    
    pass


for _ in range(test):
    #n : 음식의 수  , l : 최대 칼로리
    n, l = list(map(int, input().split()))
    
    #t : 음식에 대한 점수 , k : 칼로리
    tk = []  # t and k
    
    for i in range(n):
        tk.append(list(map(int, input().split())))
    print(tk)

    print()
    calc(n, 0, 0, l, tk)
