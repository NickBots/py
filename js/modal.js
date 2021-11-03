$(function () {

    var modalNRC = $("#modalNRCLexicon");
    console.log(modalNRC);
    var modalFM = $("#modalFormaMentis");

    var linkNRC = $(".refNRC");
    var linkFM = $(".refFM");


    var spanNRC = $(".closeNRC");
    var spanFM = $(".closeFM");

    linkNRC.on("click", function () {
        modalNRC.css("display", "block");
    });

    linkFM.on("click", function () {
        modalFM.css("display", "block");
    });

    spanNRC.on("click", function () {
        modalNRC.css("display", "none");
    });

    spanFM.on("click", function () {
        modalFM.css("display", "none");
    });

});