
import java.io.*;
/*import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;*/

public class Counting {

    public static void main(String[] args) {
        
        try{
            BufferedReader buf=new BufferedReader(new InputStreamReader(System.in));
            int n=Integer.parseInt(buf.readLine());
            int[] count=new int[100];
            String[] str=buf.readLine().split(" ");
            for(int i=0;i<n;i++){
                count[Integer.parseInt(str[i])]++;
            }
            for(int i=0;i<99;i++){
                System.out.print(count[i]+" ");
            }
            System.out.println(count[99]);
        }catch(Exception e){}
    }
}

