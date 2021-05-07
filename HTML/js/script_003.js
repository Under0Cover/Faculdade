function Enviar() {
    var nome = document.getElementById("IDnome");
    
    if (nome.value != '') {
        window.alert('Obrigado Sr(a) ' +nome.value+ ' os seus dados foram enviados com sucesso!')
    }
}