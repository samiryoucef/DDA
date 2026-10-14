 import java.rmi.*;
   
  public class Client {
      public static void main(String[] args) throws Exception {
          Hello stub = (Hello) Naming.lookup("rmi://localhost/Hello");
          System.out.println(stub.sayHello("Samir"));
      }
  }
