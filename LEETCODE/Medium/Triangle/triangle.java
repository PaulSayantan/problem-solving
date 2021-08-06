import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

/*
    Problem:
        Given a triangle array, return the minimum path sum from top to bottom.

        For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
*/

public class triangle {
    public static void main(String[] args) {
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(Arrays.asList(2));
        triangle.add(Arrays.asList(3, 4));
        triangle.add(Arrays.asList(6, 5, 7));
        triangle.add(Arrays.asList(4, 1, 8, 3));
        System.out.println(minimumTotal(triangle));
        
    }

    public static int minimumTotal(List<List<Integer>> triangle) {
        int[] memo = new int[triangle.size()];

        for (int i = 0; i < triangle.size(); i++) {
            memo[i] = triangle.get(triangle.size() - 1).get(i);
        }

        for (int i = triangle.size() - 2; i >= 0; i--) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                memo[j] = triangle.get(i).get(j) + min(memo[j], memo[j + 1]);
            }
        }

        return memo[0];
    }

    public static int min(int a, int b) {
        return a < b ? a: b;
    }
}
