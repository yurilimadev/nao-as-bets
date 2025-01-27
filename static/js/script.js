
function onToggleMenu(e){
    const navLinks = document.querySelector('.nav-links');
    
    if (e.name === 'menu'){
        navLinks.classList.remove('hidden' , 'opacity-0', 'scale-95');
        navLinks.classList.add('block', 'opacity-100', 'scale-100');
        e.name = 'close';
        
    }else if (e.name === 'close'){
        navLinks.classList.add('opacity-0', 'scale-95');
        e.name = 'menu';
    }


}
window.addEventListener('resize', () => {
    const navLinks = document.querySelector('.nav-links');

    if (window.innerWidth >= 768) {
        // Restaura a visibilidade no modo desktop
        navLinks.classList.remove('hidden', 'opacity-0', 'scale-95');
        navLinks.classList.add('block', 'opacity-100', 'scale-100');
    } else if (document.querySelector('ion-icon').name === 'menu') {
        // Reaplica `hidden` no menu no modo mobile
        navLinks.classList.add('hidden', 'opacity-0', 'scale-95');
    }
});



document.addEventListener('DOMContentLoaded', () =>{
    const botaoFormulario = document.querySelector("#form-botao");
    const formulario = document.querySelector('.form-depo');
    const botaoCancelar = document.querySelector('.close-form');
    const botaoEnviar = document.querySelector('#form-submit');
    botaoFormulario.onclick = function(){
        formulario.showModal();
    }
    botaoCancelar.onclick = function(){
        formulario.close();
    }
})


// Modais


function openModal(id) {
    const modal = document.getElementById(`textModal-${id}`);
    modal.showModal();
}

function closeModal(id) {
    const modal = document.getElementById(`textModal-${id}`);
    modal.close();
}


function abrirFormulario(){
    const editarBotoes = document.querySelectorAll(".editar");

    editarBotoes.forEach((botao) => {
        botao.addEventListener("click", async (event) => {
            console.log("Clicado no botão Editar");
            function closeForm(idDepoimento) { // Aceita o ID como parâmetro
                const dialog = document.querySelector(`#textModal-${idDepoimento}`);
                if (dialog) {
                    dialog.close();
                }
            }
        
            // Captura o ID do depoimento a partir do atributo data-id
            const idDepoimento = botao.dataset.id;

            // Seleciona o dialog correspondente
            const dialog = document.querySelector(`#textModal-${idDepoimento}`);

            if (dialog) {
                console.log(`Abrindo modal para o depoimento com ID: ${idDepoimento}`);

                // Substitui o conteúdo do modal pelo formulário de edição
                try{
                    const response = await fetch(`/get-form`);
                    const data = await response.json();
                    dialog.innerHTML = data.html;
                    dialog.showModal();
                    dialog.classList.add(`form-remover-${idDepoimento}`)


                    const botaoFechar = dialog.querySelector('.close-form'); // Seletor para o botão fechar
                    if (botaoFechar) {
                        botaoFechar.addEventListener('click', () => closeForm(idDepoimento));
                    }
                }

                catch(error){
                    console.error("Erro ao abrir modal:", error);
                }
            } else {
                console.error(`Dialog com ID textModal-${idDepoimento} não encontrado.`);
            }
            
        });
    });
    
}




