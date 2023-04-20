def merge(a, b):
        # if first linked list is empty then second
        # is the answer
    if(a == None):
        return b

    # if second linked list is empty then first
    # is the result
    if(b == None):
        return a

    # compare the data members of the two linked lists
    # and put the larger one in the result
    result = None

    if (a.data < b.data):
        result = a
        result.bottom = merge(a.bottom, b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)

    result.next = None
    return result

def flatten(root):
 
    if(root == None or root.next == None):
        return root
    # recur for list on right

    root.next = flatten(root.next)

    # now merge
    root = merge(root, root.next)

    # return the root
    # it will be in turn merged with its left
    return root
