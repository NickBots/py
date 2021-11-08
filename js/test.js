var baseData;

$(function () {

    $('#search').on('click', function () {
        addLoading();
        var searchString = $("#query").val();
        var lang = $("#lang").val();
        $.post({
            url: "http://127.0.0.1:5000/getTweets",
            datatype: "json",
            data: { user: searchString, lang: lang },
            success: checkResponse,
            error: function () {
                printErrorMessage("AJAX Request Error")
                $("#loading").remove();
            }
        });
    });

    $('#generate_random').on('click', function () {
        addLoading();
        $.post({
            url: "http://127.0.0.1:5000/generateRandomEmotions",
            datatype: "json",
            success: checkResponse,
            error: function () {
                printErrorMessage("AJAX Request Error");
                $("#loading").remove();
            }
        });
    });

    $('#upload').on('click', function () {
        addLoading();
        var textFile = $('#uploadText').prop('files')[0];
        var lang = $("#lang").val();
        var form_data = new FormData();
        form_data.append('file', textFile)
        form_data.append(lang, lang)
        $.post({
            url: 'http://127.0.0.1:5000/textUpload',
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            data: form_data,
            success: checkResponse,
            error: function () {
                printErrorMessage("AJAX Request Error");
                $("#loading").remove();
            }
        });
    });

    $("#submitUserInput").on("click", function () {
        addLoading();
        input = $('#userInput').val();
        var lang = $("#lang").val();
        $.post({
            url: "http://127.0.0.1:5000/userInput",
            datatype: "json",
            data: { userInput: input, lang: lang },
            success: checkResponse,
            error: function () {
                printErrorMessage("AJAX Request Error");
                $("#loading").remove();
            }
        });
    });
});

function addLoading(){
    $("#chart").before('<div id="loading"><img src="../resources/img/loading.gif"></div>');
    $('html, body').animate({
        scrollTop: $("#loading").offset().top
      },200);
}

function checkResponse(json) {
    $("#loading").remove();
    if (json.errMsg) {
        printErrorMessage(json.errMsg);
    }
    else {
        if (json.succMsg) printSuccessMessage(json.succMsg);
        if (json.file) {
            $("#chart").html("");
            $("#chart").show(0.5);
            baseData = json.file;
            $("#chart").append('<img src="data:image/svg+xml;base64,' + baseData + '">');
            $('html, body').animate({
                scrollTop: $("#chart").offset().top
              },200);
        }
    }
}

function openTestPanel(evt, tabName) {
    var i, tabElements, tabButtons;
    tabElements = document.getElementsByClassName("tabElement");
    for (i = 0; i < tabElements.length; i++) {
        tabElements[i].style.display = "none";
    }

    tabButtons = document.getElementsByClassName("tabButton");
    for (i = 0; i < tabButtons.length; i++) {
        tabButtons[i].className = tabButtons[i].className.replace("active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

