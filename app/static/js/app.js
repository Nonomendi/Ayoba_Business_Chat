// scripts.js

document.getElementById('toggle-theme').addEventListener('click', function() {
    const bodyClass = document.body.classList;
    if (bodyClass.contains('dark-theme')) {
        bodyClass.remove('dark-theme');
        bodyClass.add('light-theme');
    } else if (bodyClass.contains('light-theme')) {
        bodyClass.remove('light-theme');
        bodyClass.add('custom-theme');
    } else {
        bodyClass.remove('custom-theme');
        bodyClass.add('dark-theme');
    }
});

document.querySelector('.collapse-btn').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('collapsed');
});