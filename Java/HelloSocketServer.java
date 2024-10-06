import java.io.*;
import java.net.*;

public class HelloSocketServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12345)) {
            System.out.println("Waiting for connection...");
            try (Socket socket = serverSocket.accept();
                 BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                 PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {
                 
                String message = in.readLine();
                System.out.println("Message from Socket 1: " + message);
                out.println("Hello, this is Socket 2, we greet you back.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
