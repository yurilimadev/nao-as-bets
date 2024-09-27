<?php
      // configurando horário
      date_default_timezone_set('America/Sao_Paulo');
      // conectando com bando de dados
      class MyDB extends SQLite3 {
        function __construct(){
          $this->open('depoimentos.db');
        }
      }
      // ativando o modo de erro
      $db = new MyDB();
      // criando tabela
      $sql =<<<EOF
        CREATE TABLE IF NOT EXISTS `depoimentos` (
          id INTEGER PRIMARY KEY AUTOINCREMENT, 
          depoimento TEXT NOT NULL,
          estado TEXT NOT NULL,
          data_de_cadastro TEXT NOT NULL
      );
      EOF;
      $ret1 = $db->exec($sql);
      
    
      
?>