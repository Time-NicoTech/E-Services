export function checkMsgBox(msgBox){
    if(msgBox){
        msgBox.style.animation = 'fadeOut 2.5s ease-in forwards'
        setTimeout(()=>{
            msgBox.style.animation = '';
            msgBox.remove();
        }, 2500);
    }
}

document.addEventListener('DOMContentLoaded', ()=>{
    const msgBoxes = document.querySelectorAll('.msg-box');
    msgBoxes.forEach(msg=>{
        checkMsgBox(msg);
    })
})

export function displayMessage(msg, type){
    const main = document.getElementsByTagName('main')[0];
    const span = document.createElement('span');
    span.classList.add("msg-box", type);
    const i = document.createElement('i');
    const message = document.createElement('p');
    message.textContent = msg;

    if (type === 'success') {
        i.classList.add('bi', 'bi-check-square')
    } else {
        i.classList.add('bi', 'bi-exclamation-octagon');
    }

    span.appendChild(i);
    span.appendChild(message);
    main.appendChild(span);

    checkMsgBox(span);
}
