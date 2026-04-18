
const api_url = `/contatos`;

async function listarContatos() {
    const resposta = await fetch(api_url);
    const resultado = await resposta.json(); 

    const contatos = resultado.data;

    if(!Array.isArray(contatos)){
        return;
    }
    const tbody = document.getElementById("lista_contato");
    tbody.innerHTML = "";

    contatos.forEach(contato => {
        tbody.innerHTML += `
            <tr class=" table-info">
                    <td>${contato.nome}</td>
                    <td>${contato.telefone}</td>
            </tr>    
        `;
    });
}

listarContatos();


document.getElementById("form_contato").addEventListener("submit", async (e) =>{
    e.preventDefault();

    const nome = document.getElementById("nome").value;
    const idade = document.getElementById("idade").value;
    const telefone = document.getElementById("telefone").value;
    const email = document.getElementById("email").value;
    const endereco = document.getElementById("endereco").value;
    const observacao = document.getElementById("observacao").value;

    const resposta = await fetch(api_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({nome, idade, telefone, email, endereco, observacao})
        });

        if (resposta.ok){
            alert("Contato adicionado com sucesso!");
            listarContatos();
            e.target.reset();   
        }else{
            const erro = await resposta.json();
            alert(erro.ERROR || erro.erro);
        }

});

        
