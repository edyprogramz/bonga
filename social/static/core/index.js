// the load more button 
let btn = document.querySelector('.load-btn');
let currentItems = 1;
let items = [...document.querySelectorAll('.posts')];

btn.onclick = () => {
    for(var i = currentItems; i < currentItems + 1; i++){
        items[i].style.display = "block";
    }
    currentItems +=1
}

// displaying comments 
let openComments = document.querySelectorAll('.open-comments');
let displayComments = document.querySelectorAll('.comments-display');

openComments.forEach((openComment, index) => {
    openComment.onclick = () => {
        if(displayComments[index].style.display === "block"){
            displayComments[index].style.display = "none";
        } else {
            displayComments[index].style.display = "block";
        }
    };
});




