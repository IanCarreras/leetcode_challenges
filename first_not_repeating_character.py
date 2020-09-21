def first_not_repeating_character(s):
    hashtable = {}
    non_repeating = []
    
    for char in s:
        if char in hashtable:
            hashtable[char] += 1
            if char in non_repeating:
                non_repeating.remove(char)
        else:
            hashtable[char] = 1
            non_repeating.append(char)
            
    if len(non_repeating) == 0:
        return '_'
    else:
        return non_repeating[0]