window.onload = () => {
    const button = document.querySelector("button.btn-img");
    const main = document.querySelector("main");

    const main_content = localStorage.getItem("main-content");
    main.innerHTML += main_content;
    
    button.addEventListener("click", async (e) => {
        const img_src = await prompt("Introduce el link de tu imagen");
        const img_img = document.createElement("IMG");
        img_img.src = img_src;
        
        const container = document.createElement("DIV");
        const img = document.createElement("DIV");
        const img_title = document.createElement("DIV");
        const img_description = document.createElement("DIV");
        
        const img_title_p = document.createElement("P");
        img_title_p.innerText = "Título";
        img_title_p.setAttribute("contenteditable", "");
        
        const img_description_p = document.createElement("P")
        img_description_p.setAttribute("contenteditable", "");
        img_description_p.innerText = `Lorem ipsum dolor sit, amet consectetur adipisicing elit. Unde animi voluptates tenetur error ducimus,
        repellat nostrum quaerat nulla mollitia sapiente quo, modi dignissimos iure suscipit. Placeat, quos iusto. In, incidunt?`
        
        container.classList.add("img-container");
        img.classList.add("img");
        img_title.classList.add("img-title");
        img_description.classList.add("img-description");
        
        img.appendChild(img_img);
        container.append(img, img_title, img_description);
        
        img_title.appendChild(img_title_p);
        img_description.appendChild(img_description_p);
        
        main.appendChild(container);
        main.style.setProperty("width", "100%");
    });
}

function save_all() {
    const main = document.querySelector("main#main");
    localStorage.setItem("main-content", main.innerHTML);
}
