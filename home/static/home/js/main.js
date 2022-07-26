
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
const Entranslate = document.getElementById("en_text");
const href_btn = document.getElementById("a_check")
const check_btn = document.getElementById("btn_check")
const md_txt = document.getElementById("md_text")
function delay2(){
    let i = 0;
   profile.style.display = "flex";
   for ( i in navItem){
       navItem[i].style.display = "block";
   }
}
function get_info(){
    let en = textareaContainer.value;
    let md = md_txt.innerHTML;
    textareaContainer.value = "";
        $.ajax({
            type: "POST",
            url: '/',
            async: false,
            // cache: false,
            data: {
                md: md,
                en: en
             },
             dataType: 'json'
             });
            href_btn.href = '/?md=' + md + '&en=' + en

}
check_btn.onclick = function() {
    get_info()
            }
document.getElementById("btn_reset").onclick = function() {
        textareaContainer.value = "";
        window.location.href="/";
}
containerBurger.onclick = function click(){
let i = 0;
        if (LeftMenu.style.width === "250px"){
            LeftMenuContainer.style.width = null;
            LeftMenu.style.width = "50px";
            ProfileFoto.style.width = "46px"
            ProfileFoto.style.height = "46px"
            ProfileFoto.style.borderColor = "#0339fa"
            LeftMenu.style.alignItems = "end";
            Burger.classList.toggle("burger");
            Burger.classList.toggle("burger_active");
            profile.style.display = "none";
            for (i  in navItem){
                 LeftMenuIt[i].style.justifyContent = "end";
                navItem[i].style.display = "none";
            }
        }
        else{
            LeftMenuContainer.style.width = "100%";
            LeftMenu.style.width = "250px";
            ProfileFoto.style.width = "75px"
            ProfileFoto.style.height = "75px"
            ProfileFoto.style.borderColor = "#4d5665"
            LeftMenu.style.alignItems = "flex-start";
            Burger.classList.toggle("burger_active");
            Burger.classList.toggle("burger");
            setTimeout(delay2 ,200);
            for (i  in LeftMenuIt){
                LeftMenuIt[i].style.justifyContent = "start";
            }
        }
        return 0;
};


