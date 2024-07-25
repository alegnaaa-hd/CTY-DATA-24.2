import java.util.Random;
public class Sorting{

    public static final int MAX = 35 ;
    public static int [] array = new int[MAX];
    
    public static void fillArray() {
        array = new int[MAX];
        Random rand = new Random();
        for(int j=0; j < MAX ; j++)
            array[j] = rand.nextInt(99,999);
    }
    
    public static int[] cloneArray() {
        int[] newArray = new int[MAX];
        
        for(int j=0; j < MAX ; j++)
            newArray[j] = array[j];
        return newArray;
    }
    public static void swap(int[] array, int i, int j){
        int temp = array[i] ;
        array[i] = array[j] ;
        array[j] = temp ;
    }

    public static void display(int[] array) {
        for(int k = 0 ; k < array.length ; k++)
            System.out.print(array[k] + " ");
        System.out.println();
    }

    public static void selection_sort(int [] array){
        for (int i=0 ; i < array.length; i++) {
            int smallestIndex = i ;
            for (int j = i+1 ; j < array.length ; j++) {
                if (array[j] < array[smallestIndex])
                    smallestIndex = j ;
            } ;
            swap(array, i, smallestIndex) ;

        }

    }
    
    public static void insertion_sort(int [] array){
        for (int i=1 ; i < array.length; i++) {
            int key = array[i];
            int j = i-1;
            while( j >= 0 && array[j] > key) {
                array[j+1] = array[j];
                j = j-1 ;
            }
            array[j+1] = key ;

        }

    }

    public static int partition(int[] A, int p, int r){
        int x,i,j;
        x = A[r] ;
        i = p-1 ;
        for (j=p ; j <= r-1 ; j++) {
            if (A[j] <= x) {
                i += 1 ;
                swap(A, i, j) ;
            }
        }
        swap(A, i+1, i);
        return i + 1 ;

    }
    public static void quick_sort(int[] A, int p, int r){
        int q ;
        if (p < r ) {
            q = partition(A, p, r) ;
            quick_sort(A, p, q-1);
            quick_sort(A, q+1, r);
        }   

    }

    public static void main(String[] args){


        fillArray();
        int [] a = cloneArray();
        int [] b = cloneArray();
        int [] c = cloneArray();
        
        display(a);
        display(b);
        display(c);
        insertion_sort(a);
        insertion_sort(b);
        quick_sort(c, 0, c.length-1);
        display(a);
        display(b);
        display(c);
        
    }
}