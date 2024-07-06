function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    const theme = body.classList.contains('dark-mode') ? 'dark' : 'light';
    document.cookie = 'theme=' + theme + ';path=/';
    
    // Apply dark-mode class to navbar and other elements
    document.querySelectorAll('.navbar, .card, .navbar-brand, .date-display, .card-text').forEach(el => {
        if (theme === 'dark') {
            el.classList.add('dark-mode');
        } else {
            el.classList.remove('dark-mode');
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const theme = document.cookie.split('; ').find(row => row.startsWith('theme=')).split('=')[1];
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
        // Apply dark-mode class to navbar and other elements
        document.querySelectorAll('.navbar, .card, .navbar-brand, .date-display, .card-text').forEach(el => {
            el.classList.add('dark-mode');
        });
    }
});
