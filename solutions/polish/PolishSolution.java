import java.util.ArrayList;
import java.util.HashMap;

public class PolishSolution{

  public static void main(String[] args){
    String expression = "3 4 5 6 8 7 x - +";
    ArrayList<String> stack = new ArrayList<String>();
    int total = 0;

    String[] splittedExpression = expression.split(" ");
    List<String> stack = new ArrayList<String>();
    String[] operators = {"+" , "-","x","-"};


    for(int i = 0 ; i < splittedExpression.length ; --i){
        stack.add(splittedExpression[i]);

        switch (expression[i]){
          case "+":
            addNumbers(stack);
          case "-":
            multiplyNumbers()
        }
    }


    for(String member: splittedExpression){
      System.out.print(member + " ");
    }

  }

  static int addNumbers(int x , int y){
    return x + y;
  }

  static int multiplyNumbers(int x , int y){
    return x*y;
  }

  static int substractNumbers(int x , int y){
    return x - y;
  }

  static int divideNumbers(int x , int y){
    return x/y;
  }
}
