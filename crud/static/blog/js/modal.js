
const blogs = document.querySelectorAll(".portfolio-item");
const modals = document.querySelectorAll(".modal"); 
let currentModal = null;

const handleClose = (e) => {
    if (e.target.classList.contains("modal") || e.target.classList.contains("btn-close")) {
        currentModal.style.display = "none";
        currentModal.classList.remove("show");
        currentModal.setAttribute("role", "");
        currentModal.removeEventListener("click", handleClose);
        currentModal = null;
        addEventToBlogs();
    } else {
        console.log("else");
    }
};

const handleClick = (e) => {
    // e.stopPropagation();
    const currentBlogsId = e.target.parentNode.dataset.bsTarget;
    console.log("ssss");
    for (modal of modals){
        if (currentBlogsId === modal.id) {
            currentModal = modal
            console.log(currentModal);
            currentModal.style.display = "block";
            currentModal.classList.add("show");
            currentModal.setAttribute("role", "dialog");
            currentModal.addEventListener("click", handleClose);
        }
    }
}

const addEventToBlogs = () => {
    for (blog of blogs) {
        blog.addEventListener("click", handleClick);
    }
}

const init = () => {
    addEventToBlogs();
};

init();