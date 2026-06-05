document.getElementById("form-login").addEventListener("submit", async function(e){
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const resposta = await fetch("/login",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    });
    const dados = await resposta.json();
    if (dados.success){ 
        window.location.href = "/index";
        
    }else{
        document.getElementById("msg").innerText = dados.message;
    }
    
});

document.getElementById("show-password").addEventListener("click", async (e) =>{
    e.preventDefault();
    const password = document.getElementById("password");
    const showPassword = document.getElementById("show-password");

    if (password.type == "password") {
        password.type = "text";
    }else{
        password.type = "password";
    }

});