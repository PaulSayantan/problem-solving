import java.util.Arrays;
import java.util.List;
import java.util.Collections;

/*
  Problem:
    Given the individual calorie counts for each of the cupcakes,
    determine the minimum number of miles Marc must walk to maintain his weight.

    Note that he can eat the cupcakes in any order.
*/

public class cakewalk {
  public static void main(String[] args) {
    List<Integer> calorie1 = Arrays.asList(1, 3, 2);
    System.out.println("For calories intake " + calorie1.toString() + ": " + marcsCakewalk(calorie1));
  }

  public static long marcsCakewalk(List<Integer> calorie) {
    Collections.sort(calorie, Collections.reverseOrder());

    long min_miles = 0;

    for(int i = 0; i < calorie.size(); i++) {
      min_miles += calorie.get(i) * (1 << i);
    }

    return min_miles;
  }
}
