$(document).ready(function () {
    localStorage.setItem("needsReload", true);

    // set the DOM before teh interval timer
    var statBtnArr = $(".statBtn");
    for (let i = 0; i < statBtnArr.length; i++) {
        setDOM(i);
    }
    // start the interval timer at a second
    setInterval(function () {
        for (let i = 0; i < statBtnArr.length; i++) {
            setDOM(i);
        }
    }, 1000);

    $("#kitchenOption").change(function () {
        $(".orderFormBtn").removeClass("disabled");
        $(".orderFormBtn").removeAttr("disabled");
    });

    function setDOM(i) {
        // modify time elapsed column
        var timeElapsedSpan = $(".time_elapsed")[i];

        var timeCreatedSpan = $(".time_created")[i];
        var timeInSeconds = parseInt(
            $(timeCreatedSpan).attr("data-timeInSeconds")
        );
        var timeCreatedInMilli = timeInSeconds * 1000;
        var timeCreated = new Date(timeCreatedInMilli);

        var now = new Date();
        var duration = now - timeCreated;

        var seconds = Math.floor((duration / 1000) % 60);
        var minutes = Math.floor((duration / (1000 * 60)) % 60);
        var hours = Math.floor((duration / (1000 * 60 * 60)) % 24);

        $(timeElapsedSpan).text(`${hours}:${minutes}:${seconds}`);

        // change classes on status btns.
        var statBtn = statBtnArr[i];
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
});
