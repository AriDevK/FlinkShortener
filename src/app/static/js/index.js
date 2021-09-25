function changeCopyButtonState() {
    let inputUrl = $('#url').val();
    let actualUrl = window.location.href;

    if (inputUrl.startsWith(actualUrl)) {
        $('#copy').prop('disabled', false);
        $('#copy').click(() => {
            navigator.clipboard.writeText(inputUrl);
        });
    } else {
        $('#copy').prop('disabled', true);
    }
}


$(document).ready(() => {
    $('#url').ready(changeCopyButtonState);
    $('#url').on('input change', changeCopyButtonState);
});