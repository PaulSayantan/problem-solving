<h1 align="center">Binary Search</h1>

Binary search is the most popular Search algorithm. It is efficient and also one of the most commonly used techniques that is used to solve problems.

If all the names in the world are written down together in order and you want to search for the position of a specific name, binary search will accomplish this in a maximum of  iterations.

__Binary search works only on a sorted set of elements. To use binary search on a collection, the collection must first be sorted.__

When binary search is used to perform operations on a sorted set, the number of iterations can always be reduced on the basis of the value that is being searched.

## Implementation

```
int binarySearch(int low,int high,int key)
{
   while(low<=high)
   {
     int mid=(low+high)/2;
     if(a[mid]<key)
     {
         low=mid+1;
     }
     else if(a[mid]>key)
     {
         high=mid-1;
     }
     else
     {
         return mid;
     }
   }
   return -1;                //key not found
 }
```

## Time Complexity

As we dispose off one part of the search case during every step of binary search, and perform the search operation on the other half, this results in a worst case time complexity of `O(log(n))`.


## Python Source Code

_Using while-loop_

```python
def BinarySearch(sorted_arr: List[int], low: int, high: int, target: int) -> int:
    while(low <= high):
        # get the middle position in the sorted_arr
        mid = (high + low) // 2
        # if target is less than element in the middle -> check for target at the left side of the sorted_arr
        if sorted_arr[mid] > target:
            high = mid - 1
        # if target is more than element in the middle -> check for target at the right side of the sorted_arr
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            return mid
    
    # target doesn't exist in the arr
    return -1
```

---