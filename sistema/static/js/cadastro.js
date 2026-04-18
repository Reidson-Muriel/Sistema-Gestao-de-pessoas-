const api_url = `/contatos`;   

document.getElementById("form_contato").addEventListener("submit", async (e) =>{
    e.preventDefault();

    const nome = document.getElementById("nome").value;
    const nascimento = document.getElementById("nascimento").value;
    const telefone = document.getElementById("telefone").value;
    const email = document.getElementById("email").value;
    const endereco = document.getElementById("endereco").value;
    const observacao = document.getElementById("observacao").value;

    const resposta = await fetch(api_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({nome, data_nascimento:nascimento, telefone, email, endereco, observacao})
        });

        const resultado = await resposta.json();
        if (!resposta.ok){
            alert(resultado.error);
            return;  
        }

        alert(resultado.message);
        e.target.reset(); 


});