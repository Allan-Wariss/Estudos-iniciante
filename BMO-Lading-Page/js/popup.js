//Script para Submenu na visão Mobile
var subMenu = document.querySelector (".sub-menu-icon")
var subMenuAcao = document.querySelector (".sub-menu-fechado")
subMenu.addEventListener("click", function(event){

    subMenuAcao.classList.toggle("sub-menu-aberto")
})


//Script para Abrir Popup Endereço
var endereco = document.querySelector("#endereco")
var enderecoAcao = document.querySelector(".mapa-popup-fechada")
endereco.addEventListener("click",function(){

    enderecoAcao.classList.toggle("mapa-popup-aberta")
})
var enderecoSub = document.querySelector("#sub-endereco")
var enderecoSubAcao = document.querySelector(".mapa-popup-fechada")
enderecoSub.addEventListener("click",function(){

    enderecoSubAcao.classList.toggle("mapa-popup-aberta")
})

var fecharEndereco = document.querySelector(".fechar-mapa-popup")
fecharEndereco.addEventListener("click",function(){

    enderecoAcao.classList.toggle("mapa-popup-aberta")
})


//Script para Abrir Popup Contato
var contato = document.querySelector("#contato")
var contatoAcao = document.querySelector(".contato-popup-fechado")
contato.addEventListener("click",function(){

    contatoAcao.classList.toggle("contato-popup-aberto")
})
var contatoSub = document.querySelector("#sub-contato")
var contatoSubAcao = document.querySelector(".contato-popup-fechado")
contatoSub.addEventListener("click",function(){

    contatoSubAcao.classList.toggle("contato-popup-aberto")
})

var fecharContato = document.querySelector(".fechar-contato-popup")
fecharContato.addEventListener("click",function(){

    contatoAcao.classList.toggle("contato-popup-aberto")
})

//Script para abrir Popup Equipe

var equipe = document.querySelector(".btn-popup-equipe")
var equipeAcao = document.querySelector(".equipe-popup-fechado")
equipe.addEventListener("click",function(){

    equipeAcao.classList.toggle("equipe-popup-aberto")
})

var fecharEquipe = document.querySelector(".fechar-equipe-popup")
fecharEquipe.addEventListener("click",function(){

    equipeAcao.classList.toggle("equipe-popup-aberto")
})

