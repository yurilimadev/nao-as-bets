<html>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="style.css">
    <meta name="description" content="Dê seu relato sobre sua experiência com jogos de azar, bets, casas de apostas. Não precisa ter sido com você.">
    <meta name="keywords" content="projeto+social, bet, bets, tigrinho, jogos+de+azar">
    <meta name="robots" content="noindex,nofollow">
    <title>#Não Às Bets</title>
  </head>
  <body>
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
    <div class="container">
      <h1>Conte Sua História Com as Bets de Forma Anônima</h1>
      <p style="text-align:center;">Essa é uma iniciativa para ajudar na <b>conscientização dos perigos psicológicos e físicos</b> que as casas de apostas e jogos de azar podem causar na mente de crianças, jovens e adultos. Esse é um projeto simples, mas feito de coração para ajudar os projetos de lei contra às bets. Caso, não saiba do impacto, o vídeo abaixo do <a href="https://iclnoticias.com.br/">Instituto Conhecimento Liberta - Nóticias</a> sobre o tema posso te ambientar na situação. Assista o vídeo e tire suas próprias conclusões! </p>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ik20buWjiYE?si=l-CVD9r2lgIWbRhs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      <h2>Faça um depoimento e ajude essa mensagem a chegar em mais pessoas!</h2>
      <h4 style="color:red;">Deixe no mural sua opinião e relato sincero. Só que pedimos.</h4>
      <form class="formulario" method="POST">
        <textarea name="depoimento" placeholder="Digite Seu Depoimento..."></textarea>
        <label style="width:100%; ;">Estado:
          <select name="estado">">
            <?php
            $estados = array(
                "Selecione uma opção","AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", 
                "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PE", 
                "PI", "PR", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "SP"
            );
              foreach ($estados as $estado) {
                echo "<option value='$estado'>$estado</option>";
              }
            ?>
          </select>
        </label>
        <input type="submit" name="acao" value="Cadastrar" />
      </form>
      <h2 style="text-align:center;">Depoimentos:</h2>
      <div class="conteudo-depoimento">
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
      </div>
      
    </div>
    
    <footer style="text-align:center; background-color:#a3d1a6;">
      <p>2024 - Feito para uma causa social</p>
    </footer>
  </body>
</html>