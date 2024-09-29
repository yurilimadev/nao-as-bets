// Funções Dinâmicas
function selecionarEstados(){
	const estados = ["Selecione uma opção","AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", 
        "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PE", 
        "PI", "PR", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "SP"
    ];
    let select = document.getElementById('estados');
    estados.forEach(estado => {
    	const option = document.createElement('option');
    	option.value = estado;
    	option.textContent = estado;
    	select.appendChild(option);
    });
}

//W3scholl - Referencias



document.addEventListener('DOMContentLoaded', () => {
  const galeria = document.querySelector('.galeria');
  const iframes = galeria.querySelectorAll('iframe');
  const btnPrev = document.querySelector('.btn-prev');
  const btnNext = document.querySelector('.btn-next');

  if (!galeria || iframes.length === 0 || !btnPrev || !btnNext) {
    console.error("Não foi possível encontrar os elementos necessários.");
    return;
  }

  let currentSlide = 0;

  // Função para rolar para o iframe atual
  function scrollToIframe(index) {
    iframes[index].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
  }

  btnPrev.addEventListener('click', () => {
    currentSlide = (currentSlide - 1 + iframes.length) % iframes.length;
    scrollToIframe(currentSlide);
  });

  btnNext.addEventListener('click', () => {
    currentSlide = (currentSlide + 1) % iframes.length;
    scrollToIframe(currentSlide);
  });
});