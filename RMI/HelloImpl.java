 import java.rmi.server.*;
   import java.rmi.*;
  
  public class HelloImpl extends UnicastRemoteObject implements Hello {
      public HelloImpl() throws RemoteException {}
      public String sayHello(String name) {
          return "Bonjour " + name + "!";
      }
}
