$(document).ready(() => {
    let alert = $('.alert');

    setInterval(() => {
        alert.ready(() => {
            alert.fadeOut(1000);
        });
    }, 4000);
});