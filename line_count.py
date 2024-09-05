def line_count():
    file = open('file.txt', 'r') # opens the text file that need the lines counted
    lines = file.readlines() # puts all the lines into a list
    length = len(lines) # counts the length of the list (same as amount of lines)
    file.close() # closes file
    return length # returns the value