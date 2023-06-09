const navImgClickDiv = document.querySelector('.navbar-img-click-options');
const divClicking = document.querySelector('.nav-img-click');

divClicking.onclick = () => {
    if (navImgClickDiv.style.display === "block"){
        navImgClickDiv.style.display = "none";
    } else {
        navImgClickDiv.style.display = "block"; 
    }
}


// post -_---------
