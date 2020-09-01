# Program for computing minimum number of chars to be deleted for the string to be having all unique number of occurence of chars.
# We only care about the characters that occured at least once.
# EX.
# Input: "eeeeffff"
# Output: 1
# Explanation:
# We can delete one occurence of 'e' or one occurence of 'f'. Then one letter will occur four times and the other three times.
# Input: "aabbffddeaee"
# Output: 6
# Explanation:
# For example, we can delete all occurences of 'e' and 'f' and one occurence of 'd' to obtain the word "aabbda".
# Note that both 'e' and 'f' will occur zero times in the new word, but that's fine, since we only care about the letter that appear at least once.
# Input: "llll"
# Output: 0
# Explanation:
# There is no need to delete any character.
# Input: "example"
# Output: 4
# --------------------------------------------------------------------------------------------------------------------------------------------
# This is a greedy problem as to find the minimum deletions we need to start deleting from maximum length strings.
# So, we will maintain a max heap to containing occurence of chars in the string.
# We don't actually want to delete the chars in the string but simply we can count the frequency and update the frequency as we go.
# TIME : 0(N), SPACE : 0(N)


from heapq import heapify, heappush, heappop

def compute_min_deletion(s):

    freq = [0] * 26
    for i in s:
        freq[ord(i) - ord('a')] += 1
    count = 0
    heap = []
    for i in freq:
        if i != 0:
            heappush(heap, -i)

    while heap:
        curr = -heappop(heap)
        if not heap:
            return count
        if curr == -heap[0]:
            if curr > 1:
                heappush(heap, -(curr - 1))
            count += 1

    return count


# driver test function
if __name__ == '__main__':
    print(compute_min_deletion("eeeeffff"))
    print(compute_min_deletion("aabbffddeaee"))
    print(compute_min_deletion("llll"))
    print(compute_min_deletion("example"))
