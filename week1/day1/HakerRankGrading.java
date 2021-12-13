import java.util.Scanner;

public class solution{
    public static void main(String[] args )
    {
        try (Scanner in = new Scanner (System.in)) {
            int n = in.nextInt();
            //your code goes here
            //gor the grading system

            if ( n <38){
                System.out.println(n);
            }else{
                int q = n/5;
                int rem = n%5;
                if (rem >= 3){
                    System.out.println((q+1)*5);
                }
               else{
                   System.out.println(n);
               } 
            }
        }
    }    
}
