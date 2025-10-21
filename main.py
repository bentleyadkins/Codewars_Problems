def solution(array_a, array_b):
    
    # If not equal, then print error
    if len(array_a) != len(array_b):
        print("These lengths aren't equal.")
    else:
        pass
    
    def mean_square_error(list_a, list_b):
        
        # converts values to absolute in each list
        
        # list_a = [abs(i) for i in list_a]
        # list_b = [abs(j) for j in list_b]
        
        # Can use either list since they have to be equal anyways 
        len_lista = len(list_a)
        len_listb = len(list_b)
        
        v_sqr_error = 0
        for value in range(len_lista):
            v_sqr_error += (list_b[value] - list_a[value]) ** 2
        
        return v_sqr_error / len_lista
    
    answer = mean_square_error(array_a, array_b)
    return answer
