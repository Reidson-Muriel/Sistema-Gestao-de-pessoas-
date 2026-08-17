
document.addEventListener("DOMContentLoaded", async function (e) {
    const usuario_id = document.getElementById("usuario_id");
    const resposta_usuario = await fetch(`/lista-usuarios`);
    const dados_usuarios = await resposta_usuario.json();

    if (!resposta_usuario.ok) {
        alert(dados_usuarios.message);
        return;
    }
    usuario_id.innerHTML = "";

    dados_usuarios.message.forEach(usuario =>{
        const option = document.createElement("option");
        option.value = usuario[0];
        option.innerHTML = usuario[1];
        usuario_id.appendChild(option);
    });
    
    document.getElementById("form_contato").addEventListener("submit", async function (e) {
        e.preventDefault();
        
        const usuario_id = document.getElementById("usuario_id").value;
        const nome = document.getElementById("nome").value;
        const nascimento = document.getElementById("nascimento").value;
        const telefone = document.getElementById("telefone").value;
        const email = document.getElementById("email").value;
        const endereco = document.getElementById("endereco").value;
        const observacao = document.getElementById("observacao").value;
        
        const resposta = await fetch(`/contatos`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({usuario_id, nome, data_nascimento: nascimento, telefone, email, endereco, observacao })
        });
        const resultado = await resposta.json();
        if (!resposta.ok) {
            alert(resultado.message);
            return;
        }
        
        alert(resultado.message);
        e.target.reset();
        
    });
});