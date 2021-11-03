<?php include("top.html") ?>
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

<div id="main">

    <div id="page-guide">
        Index
        <ul>
            <li><a href="#basic">Basic usage</a></li>
            <li><a href="#matplotlib">Simple integration with matplotlib: ax</a></li>
            <li><a href="#fonts">Managing fonts: font, fontweight, fontsize</a></li>
            <li><a href="#coordinates">Small-multi: show_coordinates</a></li>
            <li><a href="#ticks">Ticks in polar coordinates: show_ticklabels, ticklabels_angle</a></li>
            <li><a href="#zoom">Zoom and focus: highlight_emotions, show_intensity_labels</a></li>
            <li><a href="#proportion">Petal proportion: height_width_ratio</a></li>
            <li><a href="#title">Managing the title: title, title_size</a></li>
            <li><a href="#normalize">Rescaling petal length: normalize</a></li>
        </ul>
    </div>

    <div id="functions-wrapper">

        <div class="function" id="basic">
            <h2><code>Basic usage</code></h2>
            <p> Set a spacy model as the default for this object and return it.
                If no spacy_model will be inputed, a spacy model will be loaded according with the language parameter:
            </p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik

                    emotions_simple = {
                    'joy': 1,
                    'trust': 0.6,
                    'fear': 0.7,
                    'surprise': 1,
                    'sadness': 1,
                    'disgust': 0.95,
                    'anger': 0.64,
                    'anticipation': 1
                    }

                    plutchik(emotions_simple) </code>
            </div>

            <img src="../resources/img/learnPyPlutchik/01.png" alt="Learn PyPlutchik 01">

            <p> Emotions can also be detailed in 3 degrees of intensity each:</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik

                    emotions_degrees = {
                    'joy': [0.3, 0.2, 0.5],
                    'trust': [0.5, 0.1, 0.0],
                    'fear': [0.1, 0.4, 0.2],
                    'surprise': [0.15, 0.5, 0.35],
                    'sadness': [0, 0.5, 0.5],
                    'disgust': [0.4, 0.33, 0.22],
                    'anger': [0.43, 0.12, 0.09],
                    'anticipation': [0.3, 0.5, 0.2]
                    }

                    plutchik(emotions_degrees) # scores = emotions_degrees</code>
            </div>

            <img src="../resources/img/learnPyPlutchik/02.png" alt="Learn PyPlutchik 02">

        </div>

        <div class="function" id="matplotlib">
            <h2><code>Simple integration with matplotlib: ax</code></h2>
            <p> Subplot composition is responsibility of matplotlib. PyPlutchik can be used for plotting on a matplotlib.axes:</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik
                    import matplotlib.pyplot as plt

                    fig, ax = plt.subplots( nrows = 1, ncols = 2, figsize = (16, 8) )

                    plutchik(emotions_simple, ax[0])
                    plutchik(emotions_degrees, ax[1])</code>
            </div>

            <img src="../resources/img/learnPyPlutchik/03.png" alt="Learn PyPlutchik 03">

        </div>

        <div class="function" id="fonts">
            <h2><code>Managing fonts: font, fontweight, fontsize</code></h2>
            <p> It is possible to use any font available in your system. </p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik

                    plutchik(emotions_simple, font = 'Roboto', fontweight = 'bold', fontsize = 8)</code>
            </div>
            <img src="../resources/img/learnPyPlutchik/04.png" alt="Learn PyPlutchik 04">
        </div>

        <div class="function" id="coordinates">
            <h2><code>Small-multi: show_coordinates</code></h2>
            <p>Ticks can be added in order to mark a visual reference, for an easier understanding of the petal length.</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik

                    plutchik(emotions_simple, show_coordinates = False)</code>
            </div>

            <img src="../resources/img/learnPyPlutchik/05.png" alt="Learn PyPlutchik 05">

            <p>This features comes handy when plotting small-multiples (here we just repeated the same flower over and over... you should change scores every time!)</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik
                    import matplotlib.pyplot as plt

                    fig, ax = plt.subplots( nrows = 4, ncols = 4, figsize = (20, 20) )

                    for i in range(16):
                    plt.subplot(4, 4, i+1)

                    # change score every time...
                    plutchik(emotions_simple, ax = plt.gca(), show_coordinates = False)</code>
            </div>

            <img src="../resources/img/learnPyPlutchik/06.png" alt="Learn PyPlutchik 06">

        </div>

        <div class="function" id="ticks">
            <h2><code>Ticks in polar coordinates: show_ticklabels, ticklabels_angle</code></h2>
            <p> Ticks can be added in order to mark a visual reference, for an easier understanding of the petal length. Ticks can be also rotated, if you don't want them to overlap on the Joy petal.</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik

                    plutchik(emotions_simple, show_ticklabels = True, ticklabels_angle = 15)</code>
            </div>

            <img src="../resources/img/learnPyPlutchik/07.png" alt="Learn PyPlutchik 07">

        </div>

        <div class="function" id="zoom">
            <h2><code>Zoom and focus: highlight_emotions, show_intensity_labels</code></h2>
            <p> Controlling what information to display about which emotion can be crucial to tell the right story. Here, with <code>highlight_emotion</code> you can decide to color only a subset of petals; with <code>show_intensity_labels</code> you can decide to show all the three degrees of intensity labels.</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik
                    import matplotlib.pyplot as plt

                    fig, ax = plt.subplots( nrows = 1, ncols = 3, figsize = (26, 8) )

                    plutchik(emotions_degrees, ax = ax[0], highlight_emotions = ['anticipation', 'trust'])
                    plutchik(emotions_degrees, ax = ax[1], show_intensity_labels = ['anticipation', 'trust'])
                    plutchik(emotions_degrees, ax = ax[2], highlight_emotions = ['anticipation', 'trust'], show_intensity_labels = ['anticipation', 'trust'])</code>
            </div>
            <img src="../resources/img/learnPyPlutchik/08.png" alt="Learn PyPlutchik 08">
        </div>

        <div class="function" id="proportion">
            <h2><code>Petal proportion: height_width_ratio</code></h2>
            <p> Do you like thinner petals? Or do you prefer thicker shapes?</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik
                    import matplotlib.pyplot as plt

                    fig, ax = plt.subplots( nrows = 1, ncols = 2, figsize = (17, 8) )

                    plutchik(emotions_simple, ax = ax[0], height_width_ratio = 1.3)
                    plutchik(emotions_simple, ax = ax[1], height_width_ratio = 0.7)</code>
            </div>
            <img src="../resources/img/learnPyPlutchik/09.png" alt="Learn PyPlutchik 09">
        </div>

        <div class="function" id="title">
            <h2><code>Managing the title: title, title_size</code></h2>
            <p> How do we set a title to this plot?</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik

                    plutchik(emotions_simple, title = "Random\ntitle", title_size = 24)</code>
            </div>
            <img src="../resources/img/learnPyPlutchik/10.png" alt="Learn PyPlutchik 11">
        </div>

        <div class="function" id="normalize">
            <h2><code>Rescaling petal length: normalize</code></h2>
            <p> Do you like thinner petals? Or do you prefer thicker shapes?</p>
            <div class="code-ex">
                <code>from pyplutchik import plutchik
                    import matplotlib.pyplot as plt

                    short_emotions = {
                    'joy': 0.23,
                    'trust': 0.07,
                    'fear': 0.09,
                    'surprise': 0.16,
                    'sadness': 0.13,
                    'disgust': 0.07,
                    'anger': 0.15,
                    'anticipation': 0.17
                    }

                    fig, ax = plt.subplots( nrows = 1, ncols = 2, figsize = (17, 8) )

                    plutchik(short_emotions, ax = ax[0])
                    plutchik(short_emotions, ax = ax[1], normalize = 0.25)</code>
            </div>

            <img src="../resources/img/learnPyPlutchik/11.png" alt="Learn PyPlutchik 11">

        </div>
    </div>
</div>




</div>


<?php include("footer.html") ?>