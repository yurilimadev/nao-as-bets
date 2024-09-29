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
      //validação
      if(isset($_POST['cadastrar_depoimento'])){
        $depo = $_POST['depoimento'];
        $momento_registro = date('Y-m-d H:i:s');
        $estado = $_POST['estado'];
        if (!empty($depo) && $estado != "Selecione uma opção") {
            $stmt = $db->prepare('INSERT INTO depoimentos (depoimento, estado, data_de_cadastro) VALUES (:depoimento, :estado, :data_de_cadastro)');
            $stmt->bindValue(':depoimento', $depo, SQLITE3_TEXT);
            $stmt->bindValue(':estado', $estado, SQLITE3_TEXT);
            $stmt->bindValue(':data_de_cadastro', $momento_registro, SQLITE3_TEXT);
            $ret = $stmt->execute();
            echo "<script>alert('Depoimento enviado com sucesso!');</script>";
            header("Location: index.html");
            exit();
        } else {
          echo "<script>alert('Por favor, insira um depoimento. Ele é muito importante para conscientização do projeto!');</script>";
            
        }
      }
    /*
    // Consulta para excluir os registros de teste 
    $sql = "DELETE FROM depoimentos WHERE depoimento LIKE '%Meu%'";
    $db->query($sql);
    */
?>
    
<?php 
            
    $sql = "SELECT * FROM depoimentos ORDER BY id DESC";
    
    // Executa a consulta e obtém os resultados
    $ret = $db->query($sql);
    
    // Verifica se há resultados
    if ($ret) {
        // Itera sobre os resultados e os exibe
        while ($relato = $ret->fetchArray(SQLITE3_ASSOC)) {
            echo "<p>".$relato['data_de_cadastro']." - ".$relato['estado']."</p>";
            echo "<p>".$relato['depoimento']."</p>";
            echo "<hr>";
        }
    } else {
        echo "<p>Nenhum depoimento encontrado.</p>";
    }
    $db->close();

?>