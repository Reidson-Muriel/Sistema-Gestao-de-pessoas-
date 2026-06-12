let contatoAtual = null;
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("entrada").addEventListener("submit",
        async function (e) {
            e.preventDefault();
            console.log("recarregando busca....")
            const id = document.getElementById("buscar").value;

            if (!id) {
                alert("Digite o ID");
                return;
            }
            const api_url = `/contatos/${id}`;
            const resposta = await fetch(api_url);

            if (!resposta.ok) {
                alert("Contato nao encontrado!");
                return;
            }
            const contatoresposta = await resposta.json();
            const contato = contatoresposta.message;
            contatoAtual = contato;


            const tbody = document.getElementById("busca_contato");
            tbody.innerHTML = "";

            const tr = document.createElement("tr");
            tr.innerHTML = `
                        <td>${contato.id}</td>
                        <td>${contato.nome}</td>
                        <td>${contato.idade}</td>
                        <td>${contato.telefone}</td>    
                        <td>${contato.email}</td>    
                        <td>${contato.endereco}</td>    
                        <td>${contato.observacao}</td>    
                        <td>
                            <div class="acoes">
                                <button class="btn btn-primary me-1" onclick="editar()">Editar</button>
                                <button class="btn btn-danger " onclick="excluir(${contato.id})">Excluir</button>
                            </div>
                        </td>
            `;
            tbody.appendChild(tr);
        });

    window.editar = function () {

        if (!contatoAtual) {
            alert("Busca primeiro");
            return;
        }

        document.getElementById("form-editar").style.display = "block";

        const nascimentoInput = document.getElementById("edit-nascimento");

        if (!nascimentoInput) {
            console.log("O elemento nao encontrado!");
            return;
        }

        document.getElementById("edit-id").value = contatoAtual.id;
        document.getElementById("edit-nome").value = contatoAtual.nome;
        if (contatoAtual.data_nascimento) {
            nascimentoInput.value = contatoAtual.data_nascimento.split("T")[0];
        } else {
            nascimentoInput.value = "";
        }
        document.getElementById("edit-telefone").value = contatoAtual.telefone;
        document.getElementById("edit-email").value = contatoAtual.email;
        document.getElementById("edit-endereco").value = contatoAtual.endereco;
        document.getElementById("edit-observacao").value = contatoAtual.observacao;

    }

    window.salvarEdicao = async function () {
        const id = contatoAtual.id;
        const api_url = `/contatos/${id}`;

        const nascimentoInput = document.getElementById("edit-nascimento");
        if (!nascimentoInput) {
            console.log("O campo nascimento nao encontrado!");
            return;
        }

        const nome = document.getElementById("edit-nome").value;
        const telefone = document.getElementById("edit-telefone").value;
        const nascimento = nascimentoInput.value;
        const email = document.getElementById("edit-email").value;
        const endereco = document.getElementById("edit-endereco").value;
        const observacao = document.getElementById("edit-observacao").value;


        const resposta = await fetch(api_url, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ nome, data_nascimento:nascimento, telefone, email, endereco, observacao })
        });

        if (!resposta.ok) {
            alert("Erro ao atualizar");
            return;
        }

        alert("Atualizado com sucesso!");

        document.getElementById("form-editar").style.display = "none";
        document.getElementById("entrada").dispatchEvent(new Event("submit"));
    }


    window.excluir = async function (id) {
        const api_url = `/contatos/${id}`;
        fetch(api_url, {
            method: "DELETE"
        })
            .then(res => {
                if (!res.ok) {
                    alert("Erro ao deletar");
                    return;
                }
                alert("Excluido com sucesso!");

                document.getElementById("busca_contato").innerHTML = "";
            });
    }
});