import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class HelloWorld {
    public static void main(String[] args) throws IOException {
        BufferedReader b = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(b.readLine()); 
        
        for (int i = 0; i < n; i++) {
            String output = b.readLine(); 
            System.out.println("Hello, " + output + "!");
        }
    }
}
