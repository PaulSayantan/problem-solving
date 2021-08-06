/*
    Problem:
        Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.
*/

public class minimumPathSum {
    public static void main(String[] args) {
        int[][] grid = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
        System.out.println("Output: " + minPathSum(grid));
    }
    
    public static int minPathSum(int[][] grid) {
        int rows = grid[0].length;
        int cols = grid.length;
        int[][] memo = new int[rows][cols];

        return findPaths(grid, rows - 1, cols - 1, memo);
    }
    
    public static int findPaths(int[][] grid, int m, int n, int[][] memo) {
        if (m == 0 && n == 0)
            return grid[m][n];

        if (memo[m][n] != 0)
            return memo[m][n];

        if (m == 0) {
            memo[m][n] = grid[m][n] + findPaths(grid, m, n - 1, memo);
            return memo[m][n];
        }

        if (n == 0) {
            memo[m][n] = grid[m][n] + findPaths(grid, m - 1, n, memo);
            return memo[m][n];
        }

        else {
            memo[m][n] = min(findPaths(grid, m, n - 1, memo), findPaths(grid, m - 1, n, memo)) + grid[m][n];
            return memo[m][n];
        }

        
    }

    public static int min(int a, int b) {
        return a < b ? a: b;
    }
}
