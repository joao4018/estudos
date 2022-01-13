import java.io.*;
        import java.math.*;
        import java.security.*;
        import java.text.*;
        import java.util.*;
        import java.util.concurrent.*;
        import java.util.regex.*;

public class ArrayDoisD {

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
        int[][] arr2 = new int[3][3];
        int soma = -9999;

        for (int lin = 0; lin < 4; lin++) {
            for (int col = 0; col < 4; col++) {
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        arr2[i][j] = arr[i + lin][j + col];
                    }
                }
                soma =  (soma < somaAmpulheta(arr2)) ? somaAmpulheta(arr2) : soma;

            }
        }

        return soma;

    }

    public static int somaAmpulheta(int[][] arr) {
        int soma = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                soma = soma + arr[i][j];
            }
        }
        soma = soma - arr[1][0] - arr[1][2];
        return soma;
    }


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int result = hourglassSum(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
