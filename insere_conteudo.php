<?php 
    include('criacao_banco.php');        
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