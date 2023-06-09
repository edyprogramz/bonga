const clickHere = document.querySelector('.upload-btn-click');
const displayAfterClick = document.querySelector('.upload-click-options');

clickHere.onclick = () => {
    if (displayAfterClick.style.display === 'block') {
        displayAfterClick.style.display = 'none';
    } else {
        displayAfterClick.style.display = 'block';
    }
}