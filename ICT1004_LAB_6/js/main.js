$( document ).ready(function() {
    var imgs = document.getElementsByClassName("img-small")
    for (var i=0;i<imgs.length;i++) {
        imgs[i].addEventListener("click", function(img) {
            var animal = img.target.alt;
            console.log(animal);
            console.log(img);
            var span = document.createElement("span");
            span.setAttribute("class", "img-popup")
            span.setAttribute("id", "img-popup")
            var img = document.createElement("img")
            img.setAttribute("src", "images/"+animal+"_small.jpg");
            img.setAttribute("id", "popup")
            img.setAttribute("class", "popup")
            span.appendChild(img);
            const element = document.getElementById(animal);
            span.addEventListener("click", remove_img);
            element.appendChild(span);
        });
        
    }
    activateMenu();
});

function remove_img() {
    var span = document.getElementById("img-popup");
    span.remove();
};

function activateMenu() 
{ 
var current_page_URL = location.href;
$(".navbar-nav a").each(function() 
{ 
var target_URL = $(this).prop("href");
if (target_URL === current_page_URL)
{ 
$('nav a').parents('li, ul').removeClass('active'); 
$(this).parent('li').addClass('active'); 
return false;
} 
});   
}