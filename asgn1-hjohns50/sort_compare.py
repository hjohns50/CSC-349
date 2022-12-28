import time
import sys


def selection_sort(lst):
    start_time = time.time() 
    for i in range(len(lst) - 1):
        min_spot = i
        for j in range(i+1, len(lst)):
            #cmp += 1
            if lst[j] < lst[min_spot]:
                   min_spot = j
        if i != min_spot:
            swap(lst, i, min_spot)
    stop_time = time.time()
    return str(1000* (stop_time - start_time))
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    
def insertion_sort(alist): 
    start_time = time.time() 
    if len(alist) == 0:
        return 0
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            #comparisons += 1
            alist[position] = alist[position-1]
            position = position-1

        #if alist[position-1] < currentvalue:
            #comparisons += 1
        alist[position] = currentvalue
    stop_time = time.time()
    return str(1000 * (stop_time - start_time))
def merge(alist, left, right):
    i = 0
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right [r]:
            alist[i] = left[l]
            l += 1
        else:
            alist[i] = right[r]
            r += 1
        i += 1
    while l < len(left):
        alist[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        alist[i] = right[r]
        r += 1
        i += 1

def merge_sort(alist):
    start_time = time.time()
    if len(alist) == 0 or len(alist) == 1:
        return
    mid = len(alist)//2
    left = alist[0:mid]
    right = alist[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(alist, left, right)
    stop_time = time.time()
    return str(1000 * (stop_time - start_time))

def main():
    file = open(str(sys.argv[-1]), "r")
    nums = file.read()
    file.close()
    nums = nums.replace(",", "")
    nums = nums.replace("\n", "")
    num_list = nums.split(" ")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    num_list2 = num_list.copy()
    num_list3 = num_list.copy()
    sel_time = selection_sort(num_list)
    in_time = insertion_sort(num_list2)
    me_time = merge_sort(num_list3)
    str1 = ""
    str2 = ""
    str3 = ""
    for e in range(len(num_list)):
        str1 += str(num_list[e])
        if(e == len(num_list) - 1):
            #str1 += "\n"
            break
        else:
            str1 += ", "
    for n in range(len(num_list2)):
        str2 += str(num_list2[n])
        if(n == len(num_list2) - 1):
            #str2 += "\n"
            break
        else:
            str2 += ", "
    for c in range(len(num_list3)):
        str3 += str(num_list3[c])
        if(c == len(num_list3) - 1):
            #str2 += "\n"
            break
        else:
            str3 += ", "
    print("Selection Sort: (" + sel_time[:5] +  " ms) " + str1)
    print("Insertion Sort: (" + in_time[:5] +  " ms) " + str2)
    print("Merge Sort:     (" + me_time[:5] + " ms) " + str3) 
if __name__ == "__main__":
    main()