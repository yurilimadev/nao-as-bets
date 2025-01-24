// Dinâmica dos Botões de Depoimentos
document.addEventListener("DOMContentLoaded", ()=>{
    const botaoSeisPorUm = document.querySelector('#seis-por-um');
    const botaoBets = document.querySelector('#bets');
    const areaDocumentos = document.querySelector('#area-depoimento');

    botaoSeisPorUm.addEventListener('click',()=>{
        fetch('static/templates/depoimento-seis-por-um.html')
        .then(response =>{
            if (!response.ok){
                throw new Error('Não foi possível carregar o conteúdo');
            }
            return response.text();
        }).then(html => {
            areaDocumentos.innerHTML = html;
          })
          .catch(error => {
            console.error(error);
            areaDocumentos.innerHTML = `<p style="color: red;">Erro ao carregar conteúdo.</p>`;
          });
    })

    botaoBets.addEventListener('click', ()=>{
        fetch('static/templates/depoimento-bets.html')
        .then(response =>{
            if (!response.ok){
                throw new Error('Não foi possível carregar o conteúdo');
            }
            return response.text();
        }).then(html => {
            areaDocumentos.innerHTML = html;
          })
          .catch(error => {
            console.error(error);
            areaDocumentos.innerHTML = `<p style="color: red;">Erro ao carregar conteúdo.</p>`;
          });
    })
})
