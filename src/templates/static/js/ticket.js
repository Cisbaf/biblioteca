var formOpenTicket;
var modalTicket;

function OpenTicket(url) {
    console.log(url)
    formOpenTicket.setAttribute('action', url);
    modalTicket.show();
}

window.addEventListener("load", ()=>{
    formOpenTicket = document.getElementById("formTicket");
    modalTicket = new bootstrap.Modal(document.getElementById("ticketModal"));
})