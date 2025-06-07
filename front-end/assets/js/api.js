import { checkMsgBox, displayMessage } from "./utils.js";

function handleCadastroUser(e){
    e.preventDefault();
    const username = document.querySelector("input[name='username']").value;
    const address = document.querySelector("input[name='address']").value;
    const email = document.querySelector("input[name='email']").value;
    const contact = document.querySelector("input[name='contact']").value;
    const password = document.querySelector("input[name='password']").value;
    const password2 = document.querySelector("input[name='password2']").value;


    fetch('http://127.0.0.1:8000/api/users/add/', {
        method:'post',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': document.cookie.split('=')[1]
        },
        body: JSON.stringify({
            'username': username,
            'address': address,
            'email': email,
            'contact': contact,
            'password': password,
            'password2': password2
        })
        
    })
    .then(response => {
        if(!response.ok){
            return response.json().then(data=>{
                displayMessage(data.message, "error");
                throw new Error(data.errors || "Erro desconhecido do servidor")
            })
        }

        return response.json();
    })
    .then(data=>{
        console.log("Sucesso", data);
        displayMessage(data.message, 'success');
        setTimeout(()=>{
            window.location.href = '/login/';
        }, 3000)
    })
}

document.querySelector('.cadastro-form').addEventListener('submit', handleCadastroUser);