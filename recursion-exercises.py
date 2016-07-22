#Write a function print_numbers(n) to print the numbers from 1 to n.
def print_numbers(times):
    if times > 0:
        print "The number is %d" % times
        print_numbers(times - 1)
print_numbers(5)

#Write a function say_hello(names) that takes a list of names and says hello to each name in the list (prints them out using print statement).

def say_hello(names, i = 0):
    if i < len(names):
        print "Hello %s" % names[i]
        say_hello(names, i + 1)
say_hello(["Johnny", "Bobby", "Susie"])

# Given this LLNode definition:
#
# class LLNode(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# And some setup code to create a linked list, for example:
#
# one = LLNode(1)
# two = LLNode(2)
# one.next = two
# three = LLNode(3)
# two.next = three
# four = LLNode(4)
# three.next = four
#
#Write a function ll_lookup(node, target) that returns a LLNode whose data equals target. For example, given the above setup, ll_lookup(one, 3) should return the LLNode associated with 3, while ll_lookup(one, 5) should return None, and ll_lookup(three, 1) should return None.

class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

one = LLNode(1)
two = LLNode(2)
three = LLNode(3)
four = LLNode(4)

one.next = two
two.next = three
three.next = four

def ll_lookup(node, target):
    if node:
            if node.data == target:
                print "ll_lookup %r" % node.data
                return node
            else:
                return ll_lookup(node.next, target)

ll_lookup(one, 3)
