def find_min(arr):
    if len(arr) == 0: 
        return -1
    min_element = arr[0]    
    for element in arr:
        if min_element > element:
           min_element = element
    return min_element 


def average(arr):
    if len(arr) == 0:
        return -1
        
    for elmassiv in arr:
        summ += elmassiv   
    return summ / len(arr) 


def main():
    a = []
    print(find_min(a))
    print(average(1))
    

if __name__ == '__main__':
    main()
