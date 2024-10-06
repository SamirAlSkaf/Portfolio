import java.io.*;
import java.net.*;

public class HelloSocketClient {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {
             
            out.println("Hello, this is Socket 1, I greet Socket 2.");
            String response = in.readLine();
            System.out.println("Response from Socket 2: " + response);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
