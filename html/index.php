<?php include("top.html") ?>
<link rel="stylesheet" href="../css/index.css">
<link rel="stylesheet" href="../css/form.css">
</head>

<?php include("bar.html") ?>

<div id="message"></div>

<div id="navbar-wrapper">
    <div id="navbar">
        <a class="active" href="#home">Home</a>
        <a href="./install.php">Install</a>
        <a href="./documentation.php">Documentation</a>
        <a href="./learn.php">Learn</a>
        <a href="./contribute.php">Contribute</a>
    </div>
</div>

<div class="feature">

    <div class="column">
        <a href="./learn.php#getemcount">
            <div class="featureBox">
                <div class="featureBoxContent">
                    <h4>EMOTIONS ANALYSIS</h4>
                    <p>With EmotionsLib is possible to get a count of emotions in a corpora of text</p>
                </div>
            </div>
        </a>
        <a href="./learn.php#zscorescustom">
            <div class="featureBox">
                <div class="featureBoxContent">
                    <h4>EMOTIONS COMPARISON</h4>
                    <p>EmotionsLib offers tools to allow to compare emotions distribution between two texts</p>
                </div>
            </div>
        </a>
    </div>

    <div class="column">
        <a href="./learn_pyplutchik.php">
            <div class="featureBox">
                <div class="featureBoxContent">
                    <h4>VISUAL REPRESENTATION</h4>
                    <p>With PyPlutchik is possible to directly draw a visual representation of the emotions in a text</p>
                </div>
            </div>
        </a>
        <a href="./learn.php#fmnetworkkeywordz">
            <div class="featureBox">
                <div class="featureBoxContent">
                    <h4>SEMANTIC ANALYSIS</h4>
                    <p>Using Forma Mentis emotionslib is able reconstruct and analyze the semantic context around the key concepts</p>
                </div>
            </div>
        </a>
    </div>

    <div class="column_1">
        <a href="./lexicon.php">
            <div class="featureBox">
                <div class="featureBoxContent">
                    <h4>WIDE LANGUAGE SUPPORT</h4>
                    <p>Using NRCLexicon as standard lexicon, 18 languages are currently supported</p>
                </div>
            </div>
        </a>
        <a href="./learn.php">
            <div class="featureBox">
                <div class="featureBoxContent">
                    <h4>GET STARTED</h4>
                    <p>Start using EmotionsLib and PyPlutchik with guided examples provided here</p>
                </div>
            </div>
        </a>
    </div>
</div>

<h1>Try PyPlutchik now!</h1>
<div id="liveTest">


    <div class="tab">
        <button class="tabButton" onclick="openTestPanel(event, 'TextUpload')">Text</button>
        <button class="tabButton" onclick="openTestPanel(event, 'FileUpload')">Upload file</button>
        <button class="tabButton" onclick="openTestPanel(event, 'AccSubmit')">Tweet</button>
        <button class="tabButton" onclick="openTestPanel(event, 'RandomGeneration')">Random flower</button>
    </div>


    <div id="languageSelect">
        <label for="lang">Choose the language:</label>
        <select name="lang" id="lang">
            <option value="catalan">Catalan</option>
            <option value="chinese">Saab</option>
            <option value="danish">Mercedes</option>
            <option value="dutch">Dutch</option>
            <option selected value="english">English</option>
            <option value="german">German</option>
            <option value="greek">Greek</option>
            <option value="italian">Italian</option>
            <option value="japanese">Japanese</option>
            <option value="lithuanian">Lithuanian</option>
            <option value="macedonian">Macedonian</option>
            <option value="norwegian">Norwegian</option>
            <option value="polish">Polish</option>
            <option value="portuguese">Polish</option>
            <option value="russian">Russian</option>
            <option value="spanish">Spanish</option>
        </select>
    </div>

    <div id="FileUpload" class="tabElement">
        <p>Upload text(Only .txt allowed): </p>
        <input id="uploadText" type="file" name="uploadPreview">
        <button id="upload">UPLOAD</button><br>
    </div>

    <div id="AccSubmit" class="tabElement">
        <input type="text" id="query" name="query" placeholder="@repubblica">
        <button id="search">Search</button><br>
    </div>

    <div id="TextUpload" class="tabElement">
        <textarea id="userInput" placeholder="Insert text here" maxlength="20000"></textarea><br>
        <button id="submitUserInput">Submit</button>
    </div>

    <div id="RandomGeneration" class="tabElement">
        <button id="generate_random">Generate random emotion value</button>
    </div>



</div>




<div id="chart"></div>

<?php include("footer.html") ?>