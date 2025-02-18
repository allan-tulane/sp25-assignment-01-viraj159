"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb
    

def longest_run(mylist, key):
    max_run = 0
    current_run = 0

    for num in myarray:
        if num == key:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0  # Reset counter if different number is found

    return max_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    n = len(mylist)
    
    #  Base cases
    if n == 0:
        return Result(0, 0, 0, True)
    if n == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    
    #  Divide
    mid = n // 2
    left_res = longest_run_recursive(mylist[:mid], key)
    right_res = longest_run_recursive(mylist[mid:], key)

     #  Combine Results
    is_entire_range = left_res.is_entire_range and right_res.is_entire_range
    if left_res.is_entire_range:
        left_size = left_res.left_size + right_res.left_size
    else:
        left_size = left_res.left_size

    
    if right_res.is_entire_range:
        right_size = right_res.right_size + left_res.right_size
    else:
        right_size = right_res.right_size


    crossing_run = left_res.right_size + right_res.left_size
    longest_size = max(left_res.longest_size, right_res.longest_size, crossing_run)

    # If the entire sublist is key, simplify
    if is_entire_range:
        left_size = n
        right_size = n
        longest_size = n

    return Result(left_size, right_size, longest_size, is_entire_range)




