


MAX=99001
index_computed = 1
saved_computations =[0 for i in range(MAX)]
saved_computations[0] = 0
saved_computations[1] = 1
def smart_fibo(n):
    # global index_computed
    if n >= 0 and n <= index_computed:
        return saved_computations[n]

    else:
        for new_index in range(index_computed+1, n+1):
            N = new_index + 1
            saved_computations[new_index] = saved_computations[new_index-1] + saved_computations[new_index-2]

        new_index = n
        return saved_computations[n]
    
print("fibo(99000)",smart_fibo(99000))