for _ in xrange(input()):
    n = map(int, raw_input().split()); price_of_flat = map(int, raw_input().split())
    gold_value = n[1]
    def my_sum(list_element):
        return (len(list_element) * gold_value) - (sum(list_element))
    all_sequential_combinations = [price_of_flat[start:start+l+1] for l in range(len(price_of_flat))[::-1] for start in xrange(len(price_of_flat)-l)]
    sum_of_each_combination = map(my_sum, all_sequential_combinations)
    if max(sum_of_each_combination) <=0:
        print "0"
    else:
        print max(sum_of_each_combination)
        
        
 
 
 
 
 
