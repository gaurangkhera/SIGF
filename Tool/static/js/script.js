let navbar = document.getElementById('mobile');
let ham = document.getElementById('ham');

ham.addEventListener('click', function(){
    if(navbar.classList.contains('hidden')){
        navbar.classList.remove('hidden')
    }
    else{
        navbar.classList.add('hidden')
    }
})