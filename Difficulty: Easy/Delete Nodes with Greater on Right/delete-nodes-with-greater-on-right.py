class Solution:
    def compute(self, head):
        arr = []

        curr = head
        while curr:
            arr.append(curr.data)
            curr = curr.next

        keep = []
        maxi = float('-inf')

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= maxi:
                keep.append(arr[i])
                maxi = arr[i]

        keep.reverse()

        dummy = Node(0)
        curr = dummy

        for val in keep:
            curr.next = Node(val)
            curr = curr.next

        return dummy.next