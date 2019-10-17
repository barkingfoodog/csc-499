def sort(list):
    if list is None:
        return None

    # partition list into groups by length
    grouped = group_by_len(list)

    # sort each group alphabetically
    for list in grouped:
        list.sort()
    
    # concatenate all lists into one, 1-D list
    sorted_len_alpha = []
    for list in grouped:
        sorted_len_alpha = sorted_len_alpha + list
    return sorted_len_alpha

def group_by_len(list):
    # mapping length to list of strings
    len_map = dict()

    # for each word in the list
    for word in list:
        # length = the length of given word in list
        length = len(word)
        
        # if the map doesn't contain the key for given length, add it
        if length not in len_map:
            len_map[length] = []
        
        '''append the word in the correct list identified by the length of the word
           for example, if the word was 'aaa', it would be appeneded to the list 
           in our map identified by the key '3'
           len_map[length].append(word)
        '''
    
    # unpack the keys into a list and sort
    len_keys = [*len_map]
    len_keys.sort()
    
    # rearranging the groups in ascending order
    len_in_order = [] # new list
    for key in len_keys: 
        # append the list to our new list
        len_in_order.append(len_map[key])
    return len_in_order