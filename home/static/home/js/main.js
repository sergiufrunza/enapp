
myInterval = setInterval(function (){up_down()},1000);

function up_down(){
    const element = document.getElementById("logo_img");
    if (element.style.marginTop === "-7px"){
        element.style.marginTop = "0px";

    }
    else{
        element.style.marginTop = "-7px";

    }
   }
const containerBurger = document.getElementById("container_burger");
const Burger = document.getElementById("burger");
const LeftMenu = document.getElementById("nav");
const profile = document.getElementById("user_info");
const navItem = document.getElementsByClassName("nav_item_name");
const LeftMenuIt = document.getElementsByClassName("icon_nav_item");
const LeftMenuContainer = document.getElementById("nav_items");
const ProfileFoto = document.getElementById("profile_foto");
const textareaContainer = document.getElementById("answer");
const check_btn = document.getElementById("btn_check");
const md_txt = document.getElementById("md_text");
const btn_log = document.getElementById("btn_log");
const reset_btn = document.getElementById("btn_reset");
const password2 = document.getElementById("pass2");
const password1 = document.getElementById("pass1");
const eye1 = document.getElementById("password1");
const eye2 = document.getElementById("password2");
const exit_form = document.getElementById("exit_form");
const cor = document.getElementById("cor");
const incor = document.getElementById("incor");
if(cor){
    cor.style.width = cor.dataset.correct+"%"
    incor.style.width = incor.dataset.incorrect+"%"
}
function Checkinputtype(a, b) {
    if (b.type === "password") {
        a.style.color = "var(--blue)"
        b.type = "text"
    } else {
        a.style.color = "var(--text-color)"
        b.type = "password"
    }
}
if(eye1) {
    eye1.onclick = function () {
        Checkinputtype(eye1, password1)
    }

    if (eye2) {
        eye2.onclick = function () {
            Checkinputtype(eye2, password2)
        }
    }
    exit_form.onclick = function () {
        window.location.href = "/"
    }
}




function delay(){
   profile.style.display = "flex";
   for ( let element of navItem ){
       element.style.display = "block";
   }
}
function PageRestart(){
        textareaContainer.value = "";
        document.location.reload(true)
}

if (check_btn){
check_btn.onclick = function(){
    let en = textareaContainer.value;
    let md = md_txt.innerHTML;
    $.ajax({
        url:'answer-mgFWETBrxIzdJwwA/',
        method:'get',
        data:
        {
            'en': en,
            'md': md
        },
    dataType:"json"
    });
    setTimeout(PageRestart, 250);
}

reset_btn.onclick = function() {
        setTimeout(PageRestart, 200);
}
}
if(containerBurger){
containerBurger.onclick = function click() {
        if (LeftMenu.style.width === "250px") {
            LeftMenuContainer.style.width = null;
            LeftMenu.style.width = "50px";
            ProfileFoto.style.width = "46px"
            ProfileFoto.style.height = "46px"
            ProfileFoto.style.borderColor = "#0339fa"
            LeftMenu.style.alignItems = "end";
            Burger.classList.toggle("burger");
            Burger.classList.toggle("burger_active");
            profile.style.display = "none";
            for ( let i=0; i<navItem.length; i++) {
                LeftMenuIt[i].style.justifyContent = "end";
                navItem[i].style.display = "none";
            }
        } else {
            LeftMenuContainer.style.width = "100%";
            LeftMenu.style.width = "250px";
            ProfileFoto.style.width = "75px"
            ProfileFoto.style.height = "75px"
            ProfileFoto.style.borderColor = "#4d5665"
            LeftMenu.style.alignItems = "flex-start";
            Burger.classList.toggle("burger_active");
            Burger.classList.toggle("burger");
            setTimeout(delay, 200);
            for ( let element of LeftMenuIt ) {
                element.style.justifyContent = "start";
            }
        }
    }
}



