const features = document.querySelectorAll('.features');

const totop = document.getElementById('totop')

const booksbutton = document.getElementById('managebooks');
const usersbutton = document.getElementById('manageusers');
const shelvesbutton = document.getElementById('manageshelves');

const userContent = document.getElementsByClassName('user-section');
const bookContent = document.getElementsByClassName('book-section');
const shelfContent = document.getElementsByClassName('shelf-section');

const showshelves = document.getElementById('showshelves');
const books = document.getElementsByClassName('book-grid');
const shelves = document.getElementsByClassName('shelves');




for (let i = 0; i < features.length; i++){
    const currentFeature = features[i];
    window.addEventListener("scroll", function(){
        setTimeout(() => {
            currentFeature.style.display = "flex";
            currentFeature.style.animation = "fadeIn 2s";
        }, 450);
    })
}


window.onscroll = function() {scrollFunction()};

function scrollFunction() {
if (document.body.scrollTop > 360 || document.documentElement.scrollTop > 360) {
    totop.style.display = "block";
    totop.style.animation = "fadeIn 2s"
} else {
    totop.style.display = "none";
}
}
function topFunction() {
document.body.scrollTop = 0; 
document.documentElement.scrollTop = 0;
}

document.addEventListener("DOMContentLoaded", () => {
    if (showshelves && books && shelves){
        displayShelves()
    }
    if (usersbutton) {
        displayUserContent()
    }
    if (shelvesbutton){
        displayShelfContent()
    }
    if(booksbutton){
        displayBookContent()
    }
})




// HOME.HTML
function displayShelves(){
    showshelves.addEventListener("click", function(){
    if (shelves[0].style.display = "none"){
        books[0].style.display = "none";
        shelves[0].style.display = "block";
        }
    })
}


// OWNER_DASHBOARD.HTML

function displayUserContent() {
    usersbutton.addEventListener("click", function(){
    if (userContent[0].style.display = "none"){
        userContent[0].style.display = "flex";
        bookContent[0].style.display = "none";
        shelfContent[0].style.display = "none";
        }
    })
}


function displayShelfContent(){
    shelvesbutton.addEventListener("click", function(){
    if (shelfContent[0].style.display = "none"){
        shelfContent[0].style.display = "flex";
        bookContent[0].style.display = "none";
        userContent[0].style.display = "none";
        }
    })
}

function displayBookContent() {
    booksbutton.addEventListener("click", function(){
    if (bookContent[0].style.display = "none"){
        bookContent[0].style.display = "flex";
        userContent[0].style.display = "none";
        shelfContent[0].style.display = "none";
        }
    })
}