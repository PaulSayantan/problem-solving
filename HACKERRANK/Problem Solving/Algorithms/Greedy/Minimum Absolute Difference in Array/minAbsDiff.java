import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

/*
  Problem:
    Given an array of integers, find the minimum absolute difference between any two elements in the array.
*/

public class minAbsDiff {
  public static void main(String[] args) {
    List<Integer> arr1 = Arrays.asList(-2, 2, 4);
    System.out.println("Minimum Absolute Difference in "+ arr1.toString() + ": " + minimumAbsoluteDifference(arr1));

    List<Integer> arr2 = Arrays.asList(3, -7, 0);
    System.out.println("Minimum Absolute Difference in "+ arr2.toString() + ": " + minimumAbsoluteDifference(arr2));

    List<Integer> arr3 = Arrays.asList(1, -3, 71, 68, 17);
    System.out.println("Minimum Absolute Difference in "+ arr3.toString() + ": " + minimumAbsoluteDifference(arr3));

    List<Integer> arr4 = Arrays.asList(-59, -36, -13, 1, -53, -92, -2, -96, -54, 75);
    System.out.println("Minimum Absolute Difference in "+ arr4.toString() + ": " + minimumAbsoluteDifference(arr4));
  }

  public static int minimumAbsoluteDifference(List<Integer> arr) {
    // Sort the array
    Collections.sort(arr);

    int min = Integer.MAX_VALUE;

    // iterate through every pair of integers in the array and store the minimum
    for (int i = 0; i <= arr.size() - 2; i++) {
        int temp = Math.abs(arr.get(i) - arr.get(i + 1));
        if (temp < min)
          min = temp;
    }

    return min;
  }
}
