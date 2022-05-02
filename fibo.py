def recursive_nth_fibo(n):
    fibo_list = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n+1):
            if i == 0:
                fibo_list.append(i)
            elif i == 1:
                fibo_list.append(i)
            else:
                fibo_list.append(fibo_list[i-2] + fibo_list[i-1])
        return fibo_list[n]

def recursive_nth_fibo_1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_nth_fibo_1(n - 1) + recursive_nth_fibo_1(n - 2)

def main():
    print(recursive_nth_fibo_1(7))


if __name__ == "__main__":
    main()
