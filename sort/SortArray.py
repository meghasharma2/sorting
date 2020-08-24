class Sort():
    def mergeSort(self, arr):
        if len(arr) > 1:
            fh = arr[:len(arr) // 2]
            sh = arr[len(arr) // 2:]
            self.mergeSort(fh)
            self.mergeSort(sh)
            self.__merge(fh, sh, arr)

    def __merge(self, fh, sh, arr):
        i = 0
        j = 0
        k = 0
        while i < len(fh) and j < len(sh):
            if fh[i] < sh[j]:
                arr[k] = fh[i]
                i += 1
            else:
                arr[k] = sh[j]
                j += 1
            k += 1
        while i < len(fh):
            arr[k] = fh[i]
            i += 1
            k += 1
        while j < len(sh):
            arr[k] = sh[j]
            j += 1
            k += 1

    def selectionSort(self, arr):
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]

    def quickSort(self, arr):
        self.__quickSort(arr, 0, len(arr)-1)

    def __quickSort(self, arr, low, high):
        if low < high:
            pivot_index = self.__partition(arr, low, high)
            self.__quickSort(arr, low, pivot_index-1)
            self.__quickSort(arr, pivot_index+1, high)

    def __partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def bubbleSort(self, arr):
        for i in range(0, len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            low = arr[i]
            j = i-1
            while j>=0 and low < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = low





