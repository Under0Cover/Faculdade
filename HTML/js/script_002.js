window.onload = function () {
    var heading = document.createElement("h2");
    var heading_text = document.createTextNode("Teste de criação");
    heading.appendChild(heading_text);
    document.body.appendChild(heading);
}