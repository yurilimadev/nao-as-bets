// Dinâmica dos Botões de Depoimentos
document.addEventListener("DOMContentLoaded", ()=>{
    const botaoSeisPorUm = document.querySelector('#seis-por-um');
    const botaoBets = document.querySelector('#bets');
    const areaDocumentos = document.querySelector('#area-depoimento');

    botaoSeisPorUm.addEventListener('click',()=>{
        const rodape = document.querySelector('footer');
        if (rodape.classList.contains('fixed')){
            rodape.classList.remove('fixed');
        }
        fetch('/depoimento/seis-por-um')
        .then(response =>{
            if (!response.ok){
                throw new Error('Não foi possível carregar o conteúdo');
            }
            return response.text();
        }).then(html => {
            areaDocumentos.innerHTML = html;
            rodape.classList.add('fixed');
            
          })
          .catch(error => {
            console.error(error);
            areaDocumentos.innerHTML = `<p style="color: red;">Erro ao carregar conteúdo.</p>`;
          });
    })

    botaoBets.addEventListener('click', ()=>{
        const rodape = document.querySelector('footer');
        if (rodape.classList.contains('fixed')){
            rodape.classList.remove('fixed');
        }
        fetch('/depoimento/bets')
        .then(response =>{
            if (!response.ok){
                throw new Error('Não foi possível carregar o conteúdo');
            }
            return response.text();
        }).then(html => {
            areaDocumentos.innerHTML = html;
            rodape.classList.add('fixed');
          })
          .catch(error => {
            console.error(error);
            areaDocumentos.innerHTML = `<p style="color: red;">Erro ao carregar conteúdo.</p>`;
          });
    })
})
