$(document).ready(function () {
    window.addEventListener("storage", function () {
        location.reload();
    });

    localStorage.setItem("needsReload", false);
});
