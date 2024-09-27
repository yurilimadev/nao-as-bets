<?php
    include('criacao_banco.php');
    if(isset($_POST['acao'])){
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
            header("Location: " . $_SERVER['PHP_SELF']);
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