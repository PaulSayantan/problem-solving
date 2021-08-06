import java.util.ArrayList;
import java.util.List;

/*
    Problem:
        Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

        In Pascal's triangle, each number is the sum of the two numbers directly above it
*/

public class pascalTriangle {
    public static void main(String[] args) {
        System.out.println("7th row from pascal triangle: " + getRow(7).toString());
    }

    public static List<Integer> getRow(int rowIndex) { 
        long c = 1l;
        List<Integer> row = new ArrayList<>();
        for (int i = 1; i <= rowIndex + 1; i++) {
            row.add((int)c);
            c = c * (rowIndex - i + 1) / i;
        }
        
        return row;
    }
}