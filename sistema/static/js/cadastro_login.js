document.getElementById("form-login-cadastro").addEventListener("submit", async (e) =>{
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const resposta = await fetch('/cadastro-usuarios', {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({username, password})
    });

    const dados = await resposta.json();
    if (resposta.ok){
        window.location.href = "/";
    }else{
        document.getElementById("msg").innerText = dados.message;
    }

});