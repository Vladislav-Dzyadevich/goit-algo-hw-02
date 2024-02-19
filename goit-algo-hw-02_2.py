from collections import deque

def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ", "")
    
    char_queue = deque(input_string)
    
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # Виведе: True