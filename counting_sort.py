def build_sup(arr, sup):
    for i in arr:
        try:
            sup[i] = sup[i] + 1
        except:
            sup[i] = 1


def counting_sort(arr):
    support = {}
    build_sup(arr, support)

    # verificação do support
    print(support) 

# exemplo
counting_sort([1, 2, 1, 2, 7, 5, 5, 7, 8, 7])