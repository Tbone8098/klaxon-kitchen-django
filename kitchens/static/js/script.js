$(document).ready(function () {
    localStorage.setItem("needsReload", true);
    // changes the background of the status btns by adding or removing a class
    var statBtnArr = $(".statBtn");
    for (let i = 0; i < statBtnArr.length; i++) {
        var statBtn = statBtnArr[i];
        console.log($(statBtn).text());
        if ($(statBtn).text() === "in progress") {
            $(statBtn).addClass("stat-in-progress");
            $(statBtn).removeClass("stat-ready");
            $(statBtn).removeClass("stat-done");
        } else if ($(statBtn).text() === "ready") {
            $(statBtn).addClass("stat-ready");
            $(statBtn).removeClass("stat-in-progress");
            $(statBtn).removeClass("stat-done");
        } else if ($(statBtn).text() === "done") {
            $(statBtn).addClass("stat-done");
            $(statBtn).removeClass("stat-ready");
            $(statBtn).removeClass("stat-in-progress");
        }
    }

    // console.log($("#kitchenOption").val());
    $("#kitchenOption").change(function () {
        $(".orderFormBtn").removeClass("disabled");
        $(".orderFormBtn").removeAttr("disabled");
    });

    // $(".statBtn").on("click", function (e) {
    //     // e.preventDefault();
    //     console.log("change storage to true");
    // });
});
