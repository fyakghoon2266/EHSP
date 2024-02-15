// common.js

function showLoading() {
    $('#loadingModal').modal('show');
}

$(document).ready(function () {
    $('#loadingModal').on('hidden.bs.modal', function () {
        // Code to display result here
    });

    $('form').submit(function () {
        showLoading();
    });

    var interval = setInterval(function () {
        var cookies = document.cookie.split(';');
        var found = false;
        for (var i = 0; i < cookies.length; i++) {
            if (cookies[i].indexOf('fileDownload=true') !== -1) {
                found = true;
                break;
            }
        }
        if (found) {
            clearInterval(interval);
            $('#loadingModal').modal('hide');
        }
    }, 1000);
});