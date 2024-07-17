input_str = s

char_set = set()
left = 0
result = 0

for right in range(len(input_str)):
    if input_str[right] in char_set:
        while input_str[right] in char_set:
            char_set.remove(input_str[left])
            left += 1
    
    char_set.add(input_str[right])
    result = max(result, right-left+1)

return result
