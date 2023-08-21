# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    l, r = headOne, headTwo
    prev = None
    while l and r:
        if l.value < r.value:
            prev = l
            l = l.next
        else:
            if prev:
                prev.next = r
            prev = r
            r = r.next
            prev.next = l
    if l is None:
        prev.next = r
    return headOne if headOne.value < headTwo.value else headTwo
