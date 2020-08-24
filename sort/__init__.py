from sort.SortArray import Sort
if __name__ == '__main__':
    sa = Sort()
    # us_arr = [7,9,2,0,4,9,23,7,25]
    us_arr = [1, 5, 3, 6, 2]
    # us_arr = [1,3,5,2,6,4]
    print("unsorted: ", us_arr)
    sa.mergeSort(us_arr)
    print("sorted: ", us_arr)