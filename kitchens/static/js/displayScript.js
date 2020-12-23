$(document).ready(function () {
    window.addEventListener("storage", function () {
        console.log("hi");
        location.reload();
    });

    localStorage.setItem("needsReload", false);
});
