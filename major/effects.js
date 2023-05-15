let sun = document.getElementById("sunandclouds");
let summer = document.getElementById("summer");
let pyramids = document.getElementById("pyramids");
let sand = document.getElementById("sand");
let birds = document.getElementById("birds");
let birds2 = document.getElementById("birds2");

window.addEventListener("scroll", function(){
    let value = window.scrollY;

    summer.style.top = 30 + value * -0.1 + "%";
    birds.style.top = value * -1 + "px";
    birds.style.left = value * 1 + "px";
    birds2.style.top = value * -1 + "px";
    birds2.style.left = value * -1.3 + "px";
    pyramids.style.marginTop = value * 0.3 + "px";
    sun.style.top = value * -0.1 + "px";
})


let button = document.getElementById("scroll");
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}

var media=document.querySelector('video');
replay.addEventListener("click",function(){
    media.currentTime = 0;
})