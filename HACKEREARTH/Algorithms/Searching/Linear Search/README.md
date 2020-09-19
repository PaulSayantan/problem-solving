<h1 align="center">Linear Search</h1>

Linear search is used on a collections of items. It relies on the technique of traversing a list from start to end by exploring properties of all the elements that are found on the way.

For example, consider an array of integers of size . You should find and print the position of all the elements with value . Here, the linear search is based on the idea of matching each element from the beginning of the list to the end of the list with the integer , and then printing the position of the element if the condition is `True'.

## Implementation:

The pseudo code for this example is as follows :

```
for(start to end of array)
{
    if (current_element equals to 5)  
    {
        print (current_index);
    }
}
```

## Time Complexity:

The time complexity of the linear search is `O(N)` because each element in an array is compared only once.


## Python Source Code

```python
def linearSearch(arr: List[int], target: int) -> int:
    
    # if only one element in the arr -> return the arr
    if len(arr) == 1:
        return arr[0]

    # check if target is found or not
    found = False
    
    # loop through the whole array
    for i in range(len(arr)):
        # when target is found
        if arr[i] == target:
            # return position of the target
            return i
            # declare that target is found
            found = True
            # break out of the loop to ignore unecessary traversing 
            break
    
    # when target is not found -> return None 
    if not found:
        return None
```

---