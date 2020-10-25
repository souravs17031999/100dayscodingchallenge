def first_occurence(self, arr, key):
    
        start, end = 0, len(arr) - 1
        pos = -1
        while start <= end:
            mid = start + (end - start) // 2
            if key < arr[mid]:
                end = mid - 1

            elif key > arr[mid]:
                start = mid + 1

            else:
                pos = mid 
                end = mid - 1

        return pos

    def last_occurence(self, arr, key):

            start, end = 0, len(arr) - 1
            pos = -1
            while start <= end:
                mid = start + (end - start) // 2
                if key < arr[mid]:
                    end = mid - 1

                elif key > arr[mid]:
                    start = mid + 1

                else:
                    pos = mid 
                    start = mid + 1

            return pos
  
