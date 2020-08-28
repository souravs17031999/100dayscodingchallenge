def binary_search(l, start, end, key):
    while(start <= end):
        middle = (start + end) // 2  # Caution : for larger inputs , typically more than 2^30 - 1, in order to arithmetic overflow,
        # use middle = start + (end - start) // 2
        # source : https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
        if key < l[middle]:
            end = middle - 1
        elif key > l[middle]:
            start = middle + 1
        else:
            return 1
    return 0


def sort(l):
    return l.sort()

def search_main(l, key):
    start = 0
    end = len(l) - 1
    l.sort()
    if binary_search(l, start, end, key):
        print("element found :)")
    else:
        print("element not found :(")

if __name__ == '__main__':
    print("List the elements of list: ")
    u_list = list(map(int, input().strip().split()))
    key = int(input().strip())
    print(f"your list : {u_list}")
    search_main(u_list, key)
