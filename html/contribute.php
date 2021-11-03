<?php include("top.html") ?>
<link rel="stylesheet" href="../css/form.css">
</head>
<?php include("bar.html") ?>

<div id="message"></div>
<script src="../js/sendMail.js"></script>

<div id="navbar-wrapper">
    <div id="navbar">
        <a href="./index.php">Home</a>
        <a href="./install.php">Install</a>
        <a href="./documentation.php">Documentation</a>
        <a href="./learn.php">Learn</a>
        <a class="active" href="./contribute.php">Contribute</a>
    </div>
</div>

<div id="functions-wrapper">

    <div class="function">
        <h2><code>Contribute</code></h2>
        <p> PyPlutchik and EmotionsLib use NRC Lexicon as base lexicon to calculate emotions of texts.
            If you want to contribute to the lexicon, especially with antonyms and negations,
            feel free to get in touch with us through the form below. We'll reply you as soon as possible.</p>
        <p> If you want to download the lexicon, click <a href="./lexicon.php">here</a></p>
    </div>
</div>
<div id="contact">
    <form id="signinform">
        <input type="text" id="username" placeholder="Name"><br>
        <input type="email" id="useremail" placeholder="Email address"><br>
        <textarea type="text" id="mail" name="message" placeholder="Type here your message" rows="10" maxlength="2000"></textarea><br>
        <input type="button" class="btn-grad" value="Send message" id="send">
    </form>
</div>

<?php include("footer.html") ?>