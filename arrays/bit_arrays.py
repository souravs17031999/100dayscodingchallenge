# Program for bit efficient arrays
# Since, array elements can take upto 32 bits (assuming 32 bit machine) for just one int num
# but we actually need just one bit to represent the int num, so in just one index of arr
# that is one bucket of array, we can actually store information for 32 int by setting the
# particular bit of that int num and same can be done for checking the set bits.
# So, we can get actually which bucket the int goes is given by pos / 32 (pos >> 32)
# and now, which actual bit pos to set or test is given by pos % 32 (as total 32 bits : 0...31)
# So, we can get the mask to set the num, by left shifting k bits for initial flag = "1",
# and ORing this with arr[index] will set the bit at pos.
# Also a good way to get modulus of 32 is also by ANDing by 0x1F.
# Potential applications would include but not limited to finding duplicates in the array in very
# efficient way.


class bitArray:

    def __init__(self, n):

        # divide by 32 because 1 index (1 bucket) will store upto 32 bits => info for 32 num
        self.arr = [0] * ((n >> 5) + 1)

    def get(self, pos):

        self.index = pos >> 5 # index of array (bucket of array) will be pos / 32
        self.bitpos = pos & 0x1F # actual bit pos in the selected bucket (index) , i % 32 = i & 0x1F

        flag = 1   # flag = 0000.....00001
        flag = flag << self.bitpos  # flag = 0000...010...000

        return self.arr[self.index] & flag  != 0 # this will return 1 or 0 depending on set or not

    def set(self, pos):

        self.index = pos >> 5 # index of array (bucket of array) will be pos / 32
        self.bitpos = pos & 0x1F # actual bit pos in the selected bucket (index), i % 32 = i & 0x1F

        flag = 1
        flag = flag << self.bitpos

        self.arr[self.index] |= flag   # Oring with mask will set at the given pos

    def pretty_print(self):
        print(self.arr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    ba = bitArray(5)
    for i in range(len(arr)):
        ba.set(i)
    print(ba.get(10))
    ba.pretty_print()
