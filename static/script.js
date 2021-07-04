
document.getElementById("formulario").onsubmit = error;

window.onload = () => {
    const advertencia = document.querySelector(".advertencia");
    if (advertencia.textContent !== "") {
        advertencia.classList.replace("advertencia", "show");
    }
}

function error(e) {
    const user = e.target.elements.usuario;
    const password = e.target.elements.contraseña;
    const email = e.target.elements.email;
    if (!user.value || !password.value || !email.value) {
        let advertencia = document.querySelector(".advertencia");
        if (advertencia.textContent != "") {
            advertencia.classList.replace("advertencia", "show");

            return false;
        }

        if (advertencia != null) {
            advertencia.innerText = "Completa los campos requeridos";
            advertencia.classList.replace("advertencia", "show");

            return false;
        }
        else {
            return false;
        }
    }
}
