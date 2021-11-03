<?php include("top.html") ?>
</head>
<?php include("bar.html") ?>

<div id="navbar-wrapper">
<div id="navbar">
    <a href="./index.php">Home</a>
    <a class="active" href="./install.php">Install</a>
    <a href="./documentation.php">Documentation</a>
    <a href="./learn.php">Learn</a>
    <a href="./contribute.php">Contribute</a>
</div>
</div>

<div id="functions-wrapper">

    <div class="function">
        <h2><code>Install PyPlutchik</code></h2>
        <p>PyPlutchik could be installed with both pip and conda.<br> With pip:</p>
        <div class="code-ex">
            <code>pip3 install pyplutchik </code>
        </div>
        <p>With conda:</p>
        <div class="code-ex">
            <code>conda install pyplutchik</code>
        </div>
    </div>
    <div class="function">
        <h2><code>Requirements</code></h2>
        <p>In order to work properly, PyPlutchik needs the following libraries</p>
        <div class="code-ex">
            <code>Shapely==1.7.1
                numpy==1.17.4
                matplotlib==3.3.2
                descartes==1.1.0 </code>
        </div>
    </div>
</div>
<?php include("footer.html") ?>