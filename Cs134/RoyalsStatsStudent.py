#@author First Last

def main():
    pass

# Search for a given value in a list
# @param list The list to search
# @param value The value to match
# @return The index of value if found or -1 if not found.
def linearSearch(list, value) :
    for i in range(len(list)) :
        if (list[i] == value) :
            return i
    return -1

main()