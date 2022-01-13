import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class MakingAnagram {

    // Complete the makeAnagram function below.
    static int makeAnagram(String a, String b) {
        char[] as = a.toCharArray();
        char[] bs = b.toCharArray();

        int sizeA = a.length();
        int sizeB = b.length();
        int soma = 0;
        int fim = 0;



        for (int i = 0; i < sizeA; i++) {
            for (int j = 0; j < sizeB ; j++) {
                if (as[i] == bs[j]){
                    soma = soma + 1;
                    as[i] = 0;
                    bs[j] = 0;
                    j = sizeB;
                }
            }
        }

        fim = (sizeA + sizeB) - (2 * soma);

        return fim;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String a = scanner.nextLine();

        String b = scanner.nextLine();

        int res = makeAnagram(a, b);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
