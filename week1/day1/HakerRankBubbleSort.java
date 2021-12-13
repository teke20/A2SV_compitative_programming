import java.util.*;

public class HakerRankBubbleSort{

private static void swap(int a[], int element1, int element2 ) {
int temp = a[element1];
a[element1] = a[element2];
a[element2] = temp;
}

private static int bubbleSort(int a[], int n) {
int totalSwaps = 0;
for (int i = 0; i < n; i++) {

int numberOfSwaps = 0;

for (int j = 0; j < n - 1; j++) {
if (a[j] > a[j + 1]) {
swap(a, j, j + 1);
numberOfSwaps++;
}
}

totalSwaps += numberOfSwaps;

if (numberOfSwaps == 0) {
break;
}
}
return totalSwaps;
}

public static void main(String[] args) {
try (Scanner in = new Scanner(System.in)) {
    int n = in.nextInt();
    int a[] = new int[n];
    for(int a_i=0; a_i < n; a_i++){
    a[a_i] = in.nextInt();
    }
    
    int swapCount = bubbleSort(a,n);
    System.out.printf("Array is sorted in %d swaps.\n", swapCount);
    System.out.printf("First Element: %d\n", a[0]);
    System.out.printf("Last Element: %d\n", a[n-1]);
}
}
}

