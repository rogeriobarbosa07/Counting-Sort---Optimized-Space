def build_sup(arr, sup):
    for i in arr:
        try:
            sup[i] = sup[i] + 1
        except:
            sup[i] = 1

# modificar essa função para que atue no primeiro vetor!
# terá que remover o arr2
def sort(arr, sup, arr2):
    for i in range(min(arr), max(arr)):
        try:
            sup[i]
        except:
            continue

        for _ in range(sup[i]):
            arr2.append(i)

def counting_sort(arr):
    support = {}
    arr2 = []
    build_sup(arr, support)
    sort(arr, support, arr2)
    return arr2

# exemplo
print(counting_sort([1, 2, 1, 2, 7, 5, 5, 7, 8, 7]))