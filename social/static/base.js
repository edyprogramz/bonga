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
const uploadBtnClick = document.querySelector('.upload-btn');
const postDivClicking = document.querySelector('.upload-click-options');

postDivClicking.onclick = () => {
    if (uploadBtnClick.style.display === "block"){
        uploadBtnClick.style.display = "none";
    } else {
        uploadBtnClick.style.display = "block";
    }
}