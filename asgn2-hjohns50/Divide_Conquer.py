import sys

file = open(str(sys.argv[-1]), "r")
nums = file.read()
nums = nums.strip("\n")
file.close()
num_list = nums.split("\n")
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

def bin_search(start, end):
    if start > end:
        return None
    if start == end:
        return num_list[start]
    
    temp = end - start
    temp = temp // 2
    mid = temp + start

    if (mid % 2 == 0):
        if (num_list[mid] == num_list[mid+1]):
            return bin_search(mid+2, end)
        else:
            return bin_search(start, mid)
    else:
        if (num_list[mid] == num_list[mid-1]):
            return bin_search(mid+1, end)
        else:
            return bin_search(start, mid-1)
def main():
    result = bin_search(0, len(num_list)-1)
    print(result)
if __name__ == "__main__":
    main()