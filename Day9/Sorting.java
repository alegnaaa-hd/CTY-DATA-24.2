public class Sorting{

    public static boolean isLessThan(int a, int b){
        return a < b ;

    }

    public static void swap(int [] array, int i, int j){

        if (i >= 0 && i < array.length && j>=0 && j< array.length) {
            int temp = array[i] ;
            
            array[i] = array[j] ;
            array[j] = temp ;
        }

    }

    public static void selectionSort(int [] array){
        int n = array.length ;
        for (int i = 0 ; i < n ; i++) {
            int indexWithSmallest = i ;

            for (int j=i+1; j < n ; j++) {

                /* if(array[j] < array[indexWithSmallest]) */
                if (isLessThan(array[j], array[indexWithSmallest]))
                    indexWithSmallest = j ;

            }

            swap(array, i, indexWithSmallest);
        }

    }

    public static void displayArray(int[] array){
        if(array == null)
            return ;

        for(int k=0 ; k < array.length; k++) {
            System.out.print(" "+array[k]);
        }
        
    }

    public static void main(String[] args){
        int[] array = {9,0,4,2,1,11};
        selectionSort(array);
        displayArray(array);
    }
}