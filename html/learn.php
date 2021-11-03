<?php include("top.html") ?>
<link rel="stylesheet" href="../css/modaldef.css">
</head>
<?php include("bar.html") ?>

<div id="navbar-wrapper">
    <div id="navbar">
        <a href="./index.php">Home</a>
        <a href="./install.php">Install</a>
        <a href="./documentation.php">Documentation</a>
        <a class="active" href="./learn.php">Learn</a>
        <a href="./contribute.php">Contribute</a>
    </div>
</div>

<a href="./learn_pyplutchik.php">
    <div class="featureBox">
        <div class="featureBoxContent">
            <h3>PyPlutchik</h3>
            <p>To access PyPlutchik tutorial, click here</p>
        </div>
    </div>
</a>


<?php include("modal_def.html") ?>


<div id="main">
    <div id="page-guide">
        <span>Index</span>
        <ul>
            <li><a href="#howto">How to use emotionslib</a></li>
            <li><a href="#getemcount">Get emotions count</a></li>
            <li><a href="#zscoresdefault">Z-Scores against default baseline</a></li>
            <li><a href="#zscorescustom">Z-Scores against custom baseline</a></li>
            <li><a href="#permanentbaseline">Load a permanent baseline</a></li>
            <li><a href="#fmnetworkemcount">Get a formamentis network and print emotion counts</a></li>
            <li><a href="#fmnetworkkeywordem">Get a Formamentis network related with a keyword and get emotion counts</a></li>
            <li><a href="#fmnetworkkeywordz">Get a formamentis network related with a keywork and get Z-Scores</a></li>
            <li><a href="#zscoresfmedge">Get Z-scores from text through Formamentis, and filter the edges of a keyboard</a></li>
            <li><a href="#plot">Plot the results</a></li>
        </ul>
    </div>

    <div id="functions-wrapper">

        <div class="function" id="howto">
            <h2><code>How to use emotionslib</code></h2>
            <p> The following tutorial will show the main features of emotionslib.
                For testing purposes, an Italian news article about vaccines has been used.
                You can download it <a href="../resources/doc/sample_article.txt" download="">here</a>
            </p>
            <p>The text used as baseline is be a similar one. You can download it <a href="../resources/doc/another_text_[baseline].txt" download>here</a></p>
            <div class="code-ex">
                <code>
                    file = 'sample_article.txt'
                    with open(file, 'r') as fr:
                    text = fr.read()

                    file = 'another_text_[baseline].txt'
                    with open(file, 'r') as fr:
                    baseline_text = fr.read()

                    from emotionslib import EmoScores
                    emos = EmoScores(language = 'italian')
                </code>
            </div>
        </div>

        <div class="function" id="getemcount">
            <h2><code>Get emotions count</code></h2>
            <p> The function <code>emotions</code> count the emotions found in the given text
            </p>
            <div class="code-ex">
                <code>emo_counts = emos.emotions(text) </code>
            </div>

            <p>For the sample text file, the output is:</p>
            <div class="code-ex">
                <code>{
                    'anger': 13,
                    'trust': 30,
                    'surprise': 9,
                    'disgust': 6,
                    'joy': 11,
                    'sadness': 10,
                    'fear': 10,
                    'anticipation': 13
                    }</code>
            </div>
        </div>

        <div class="function" id="zscoresdefault">
            <h2><code>Z-Scores against default baseline</code></h2>
            <p>The function <code>zscores</code> calculate the z-scores against the default baseline </p>
            <div class="code-ex">
                <code>zscores = emos.zscores(text)</code>
            </div>
            <p>For the sample text file, the output is:</p>
            <div class="code-ex">
                <code>{
                    'anger': -0.9522851268751225,
                    'trust': 4.154804864386931,
                    'surprise': 0.5117631779280652,
                    'disgust': -2.468675084157538,
                    'joy': 0.5127558828909093,
                    'sadness': -1.6538982659464827,
                    'fear': -2.8998865994251437,
                    'anticipation': 0.3467856686382607
                    }</code>
            </div>
        </div>

        <div class="function" id="zscorescustom">
            <h2><code>Z-Scores against custom baseline</code></h2>
            <p>The function <code>zscores</code>, when a custom baseline has been given in input, calculate the z-scores against the custom baseline </p>
            <div class="code-ex">
                <code>zscores = emos.zscores(text, baseline = baseline_text)</code>
            </div>

            <p>For the sample text files, the output is:</p>
            <div class="code-ex">
                <code>{
                    'anger': 2.3741623426314957,
                    'trust': -0.10497304822332047,
                    'surprise': 2.5834040205867477,
                    'disgust': 4.849247787516226,
                    'joy': 1.6799908875023282,
                    'sadness': -0.7338748373578562,
                    'fear': -1.8969228868514503,
                    'anticipation': -1.26535346750406
                    }</code>
            </div>
        </div>

        <div class="function" id="permanentbaseline">
            <h2><code>Load a permanent baseline</code></h2>
            <p>Load a permanent baseline. Works best for multiple file. After loading the baseline, it is permanent.<br>
                The following section of code loads a baseline and calculate the Z-Scores against it.</p>
            <div class="code-ex">
                <code>emos.load_baseline(baseline_text)
                    zscores = emos.zscores(text)</code>
            </div>

            <p>For the sample text files, the output is:</p>
            <div class="code-ex">
                <code>{
                    'anger': 2.3741623426314957,
                    'trust': -0.10497304822332047,
                    'surprise': 2.5834040205867477,
                    'disgust': 4.849247787516226,
                    'joy': 1.6799908875023282,
                    'sadness': -0.7338748373578562,
                    'fear': -1.8969228868514503,
                    'anticipation': -1.26535346750406
                    }</code>
            </div>
        </div>

        <div class="function" id="fmnetworkemcount">
            <h2><code>Get a formamentis network and print emotion counts</code></h2>
            <p>The code below a <button class="refFM">formamentis network</button> from text and then z-scores against the loaded baseline </p>
            <div class="code-ex">
                <code>edges, vertex = emos.formamentis_network(text)
                    emo_counts = emos.emotions(edges)</code>
            </div>

            <p>For the sample text file, the output is:</p>
            <div class="code-ex">
                <code>{'anger': 32,
                    'trust': 80,
                    'surprise': 17,
                    'disgust': 19,
                    'joy': 26,
                    'sadness': 26,
                    'fear': 28,
                    'anticipation': 31
                    }</code>
            </div>
        </div>

        <div class="function" id="fmnetworkkeywordem">
            <h2><code>Get a Formamentis network related with a keyword and get emotion counts</code></h2>
            <p>The code below get a <button class="refFM">formamentis network</button> about "vaccino" and print emotion counts </p>
            <div class="code-ex">
                <code>edges, vertex = emos.formamentis_network(text, target_word = "vaccino")
                    emo_counts = emos.emotions(edges)</code>
            </div>

            <p>For the sample text files, the output is:</p>
            <div class="code-ex">
                <code>{
                    'anger': 0,
                    'trust': 7,
                    'surprise': 0,
                    'disgust': 0,
                    'joy': 0,
                    'sadness': 0,
                    'fear': 0,
                    'anticipation': 0
                    }</code>
            </div>
        </div>

        <div class="function" id="fmnetworkkeywordz">
            <h2><code>Get a formamentis network related with a keywork and get Z-Scores</code></h2>
            <p>The code below get a <button class="refFM">formamentis network</button> and get z-scores against loaded baseline, with filter on edges linked to 'vaccino' </p>
            <div class="code-ex">
                <code>edges, vertex = emos.formamentis_network(text)
                    zscores = emos.zscores(edges, target_word = "vaccino")</code>
            </div>

            <p>For the sample text files, the output is:</p>
            <div class="code-ex">
                <code>{
                    'anger': -0.6164874904402363,
                    'trust': 1.7569323698576893,
                    'surprise': -0.45240763670536194,
                    'disgust': -0.20412414523193148,
                    'joy': -0.657566025931939,
                    'sadness': -0.9451740269746034,
                    'fear': -1.2138019929127832,
                    'anticipation': -1.0860294283307934
                    }</code>
            </div>
        </div>

        <div class="function" id="zscoresfmedge">
            <h2><code>Get Z-scores from text through Formamentis, and filter the edges of a keyboard</code></h2>
            <p>The code below get Z-scores from text through Formamentis, and filter the edges on 'vaccino'</p>
            <p>Note: Loading a formamentis and asking z-scores is best when working with multiple files.
                It's possibile just to get emotion counts and ask to use <button class="refFM">formamentis network</button> as well.</p>
            <div class="code-ex">
                <code>zscores = emos.zscores(text, baseline = baseline_text)</code>
            </div>

            <p>For the sample text files, the output is:</p>
            <div class="code-ex">
                <code>{
                    'anger': -0.6145449084065377,
                    'trust': 1.5896705195776903,
                    'surprise': -0.4121213665866246,
                    'disgust': -0.1856953381770519,
                    'joy': -0.6706818369346617,
                    'sadness': -0.801545489593034,
                    'fear': -1.1360826531071895,
                    'anticipation': -1.1442156775233001
                    }</code>
            </div>
        </div>

        <div class="function" id="plot">
            <h2><code>Plot the results</code></h2>
            <p>The results of the previous operation could be graphically visualised using a Plutchik Wheel (also known as Plutchik Flower).
                Emotions lib embed a module, known as PyPlutchik, which allow to easily plot the emotions. The full documentation is available
                <a href="./documentation_pyplutchik.php">here</a> or clicking "Documentation" in the navigation bar.
            </p>
            <div class="code-ex">
                <code>import matplotlib.pyplot as plt

                    fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (26, 8))

                    emo_counts = emos.emotions(text, normalization_strategy = 'num_emotions')
                    emo_baseline = emos.baseline_distribution().emotions
                    zscores = emos.zscores(text)


                    emos.draw_plutchik(emo_counts, ax = ax[0], title = 'counts')
                    emos.draw_plutchik(emo_baseline, ax = ax[1], title = 'baseline')
                    emos.draw_plutchik(zscores, reject_range = (-1.96, 1.96), rescale = (-10, 10), ax = ax[2], title = 'against baseline');</code>
            </div>

            <p>The code above uses the <code>draw_plutchik</code> function to three Plutchik wheel, representing respectively
                <li>Left plot: Emotions distribution in the text</li>
                <li>Center plot: Emotions distribution in the baseline</li>
                <li>Right plot: Difference between the two distributions in Z-Scores</li>
            </p>
            <img src="../resources/img/learn1.png" alt="Learn PyPlutchik 01">
        </div>

    </div>
</div>

<?php include("footer.html") ?>