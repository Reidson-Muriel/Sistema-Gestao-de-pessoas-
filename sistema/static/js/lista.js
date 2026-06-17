const api_url = `/contatos`;

async function listarContatos() {
    const resposta = await fetch(api_url);
    const resultado = await resposta.json(); 

   

    const contatos = resultado.message;

    const tbody = document.getElementById("lista_contato");
    tbody.innerHTML = "";

    contatos.forEach(contato => {
        tbody.innerHTML += `
            <tr class="  table-info">
                    <td>${contato.id}</td>
                    <td>${contato.nome}</td>
                    <td>${contato.telefone}</td>    
            </tr>    
        `;
    });
}

listarContatos();