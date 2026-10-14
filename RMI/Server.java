import java.rmi.Naming; 
import java.rmi.registry.*;
   
  public class Server {
      public static void main(String[] args) throws Exception {
          HelloImpl obj = new HelloImpl();
          LocateRegistry.createRegistry(1099);
          Naming.rebind("rmi://localhost/Hello", obj);
          System.out.println("Serveur prêt !");
      }
}
