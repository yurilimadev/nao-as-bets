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