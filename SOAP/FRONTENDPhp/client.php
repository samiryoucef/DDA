<?php 
$wsdl = "http://localhost:8000/?wsdl";
 
 try {
      $client = new SoapClient($wsdl, [
          'trace' => 1,
          'exceptions' => true
      ]);
 
      echo "Connexion réussie au service SOAP\n";

      // afficher toutes les méthodes fournis par le service ....
      // il peut être utiliser pour ne pas se tromper sur les noms des méthodes
      echo "<pre>";
    print_r($client->__getFunctions());
    echo "</pre>";
 
 } catch (Exception $e) {
     echo "Erreur : " . $e->getMessage();
 }
