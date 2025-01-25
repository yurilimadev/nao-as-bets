
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