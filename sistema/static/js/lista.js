async function listarContatos() {
    try {
        const resposta = await fetch(`/contatos`);
        const resultado = await resposta.json(); 
        console.log("resultado:", resultado.message);

        
        const tbody = document.getElementById("lista_contato");
        tbody.innerHTML = "";
        resultado.message.forEach(contato => {
            const tr = document.createElement("tr");
            tr.className ="table-info";
            tr.innerHTML = ` 
                        <td>${contato.id}</td>
                        <td>${contato.nome}</td>
                        <td>${contato.telefone}</td>
                        `;
            tbody.appendChild(tr);
        });

        const respostaUsuario = await fetch("/me");
        const resultadoUsuario = await respostaUsuario.json();
        const res = resultadoUsuario.message.cargo;
        const botao = document.getElementById("bnt-adicionar");
        if (res?.trim() === "admin"){
            botao.style.display = "block";
        }else{
            botao.style.display = "none";
        }
        if (!resposta.ok) {
            alert(resultado.message);
            return;
        }
        
        alert("Contatos listado com sucesso!");
        e.target.reset();
    } catch (error){
        console.error("erro ao listar o contato: ", error);
    }
}

listarContatos();