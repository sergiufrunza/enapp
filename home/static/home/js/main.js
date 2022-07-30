
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

function delay2(){
    let i = 0;
   profile.style.display = "flex";
   for ( i in navItem){
       navItem[i].style.display = "block";
   }
}
function PageRestart(){
        textareaContainer.value = "";
        window.location.href="/"
}


check_btn.onclick = function(){
    let en = textareaContainer.value;
    let md = md_txt.innerHTML;
    $.ajax({
        url:'answer',
        method:'get',
        data:
        {
            'en': en,
            'md': md
        },
    dataType:"json"
    });
    setTimeout(PageRestart, 150);
}
reset_btn.onclick = function() {
        setTimeout(PageRestart, 100);

}
    containerBurger.onclick = function click() {
        let i = 0;
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
            for (i in navItem) {
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
            setTimeout(delay2, 200);
            for (i in LeftMenuIt) {
                LeftMenuIt[i].style.justifyContent = "start";
            }
        }
        return 0;
    };


