let navbar = document.getElementById('mobile');
let ham = document.getElementById('ham');
let cross = document.getElementById('cross');

ham.addEventListener('click', function () {
    if (navbar.classList.contains('hidden')) {
        navbar.classList.remove('hidden');
        cross.classList.remove('hidden');
        ham.classList.add('hidden');
    }
});

cross.addEventListener('click', function () {
    if (!navbar.classList.contains('hidden')) {
        navbar.classList.add('hidden');
        cross.classList.add('hidden');
        ham.classList.remove('hidden');
    }
});