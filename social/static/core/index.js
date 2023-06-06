let btn = document.querySelector('.load-btn');
let currentItems = 1;
let items = [...document.querySelectorAll('.posts')];

btn.onclick = () => {
    for(var i = currentItems; i < currentItems + 1; i++){
        items[i].style.display = "block";
    }
    currentItems +=1
}