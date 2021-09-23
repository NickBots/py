$(function() {

    $('#search').on('click', function () {
        const searchString = $("#query").val();
        $.post({
            url: "http://127.0.0.1:5000/getTweets",
            datatype: "json",
            data: { user: searchString },
            success: checkLoadedTweets,
        });
    });

    $('#generate_random').on('click', function () {
        $.post({
            url: "http://127.0.0.1:5000/generateRandomEmotions",
            datatype: "json",
            success: checkRandomEmotions,
        });
    });

    $('#upload').on('click', function () {
        var textFile= $('#uploadText').prop('files')[0];
        var form_data = new FormData();
        form_data.append('file', textFile)
        $.post({
            url: 'http://127.0.0.1:5000/textUpload',
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            data: form_data,
        });
    });

    $("#submitUserInput").on("click",function(){
        input = $('#userInput').val();
        $.post({
            url: "http://127.0.0.1:5000/userInput",
            datatype: "json",
            data: {userInput: input},
            success: checkInputResponse,
        });
    });
});


function checkLoadedTweets(json) {
    console.log(json);
};

function checkRandomEmotions(json){
    $("#chart").html("");
    $("#chart").show(0.5);
    plutchik("#chart", "../py/temp/"+json.fileID+".json");
    $.post({
        url: "http://127.0.0.1:5000/deleteFile",
        data: {fileID: json.fileID},
    });
}

function checkInputResponse(json){
    console.log(json);
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

