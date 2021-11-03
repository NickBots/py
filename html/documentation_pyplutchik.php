<?php include("top.html") ?>
</head>
<?php include("bar.html") ?>

<div id="navbar-wrapper">
    <div id="navbar">
        <a href="./index.php">Home</a>
        <a href="./install.php">Install</a>
        <a class="active" href="./documentation.php">Documentation</a>
        <a href="./learn.php">Learn</a>
        <a href="./contribute.php">Contribute</a>
    </div>
</div>

<div id="functions-wrapper">

    <div class="function" id="load_spacy">
        <h2><code>plutchik</code></h2>
        <p> PyPlutchik is a Python module specifically designed for the visualisation of Plutchik’s wheel of emotions in texts or
            in corpora. PyPlutchik draws the Plutchik’s flower with each emotion petal sized after how much that emotion is detected
            or annotated in the corpus, also representing three degrees of intensity for each of them. PyPlutchik allows users to
            display also primary, secondary, tertiary and opposite dyads.
            It contains, only this function, which draws the Plutchik's wheel of emotion, with petals sized after the input
            parameter <code>scores</code>.
        </p>
        <h3>Syntax</h3>
        <div class="code-ex">
            <code>pyplutchik.plutchik(
                scores,
                ax = None,
                font = None,
                fontweight = 'light',
                fontsize = 15,
                show_coordinates = True,
                show_ticklabels = False,
                highlight_emotions = 'all',
                show_intensity_labels = 'none',
                ticklabels_angle = 0,
                ticklabels_size = 11,
                height_width_ratio = 1,
                title = None,
                title_size = None,
                normalize = False )</code>
        </div>

        <h3>Required arguments</h3>
        <dl>
            <dt><code>scores</code></dt>
            <dd>A dictionary with emotions or dyads. For each entry, values accepted are a 3-values iterable (for emotions only) or a scalar value between 0 and 1. The sum of the 3-values iterable values must not exceed 1, and no value should be negative.</dd>

            <dt><code>ax</code></dt>
            <dd>matplotlib.axes to draw the flower on. Default is None: a new ax will be created.</dd>

            <dt><code>font</code></dt>
            <dd>Font of text. Default is sans-serif.</dd>

            <dt><code>fontweight</code></dt>
            <dd>Font weight of text. Default is light.</dd>

            <dt><code>fontsize</code></dt>
            <dd>A boolean, wether to show polar coordinates or not.</dd>

            <dt><code>show_coordinates</code></dt>
            <dd>A dictionary with emotions or dyads. For each entry, values accepted are a 3-values iterable (for emotions only) or a scalar value between 0 and 1. The sum of the 3-values iterable values must not exceed 1, and no value should be negative.</dd>

            <dt><code>show_ticklabels</code></dt>
            <dd>How much to rotate tick labels from y=0. Value should be given in radians. Default is 0</dd>

            <dt><code>ticklabels_angle</code></dt>
            <dd>A dictionary with emotions or dyads. For each entry, values accepted are a 3-values iterable (for emotions only) or a scalar value between 0 and 1. The sum of the 3-values iterable values must not exceed 1, and no value should be negative.</dd>

            <dt><code>highlight_emotions</code></dt>
            <dd>A string or a list of main emotions to highlight. If a list of emotions is given, other emotions will be shadowed. Default is 'all'.</dd>

            <dt><code>show_intensity_labels</code></dt>
            <dd>A string or a list of main emotions. It shows all three intensity scores for each emotion in the list, and for the others cumulative scores. Default is 'none'.</dd>

            <dt><code>ticklabels_size</code></dt>
            <dd>Size of tick labels. Default is 11.</dd>

            <dt><code>height_width_ratio</code></dt>
            <dd>Ratio between height and width of the petal. Lower the ratio, thicker the petal. Default is 1.</dd>

            <dt><code>title</code></dt>
            <dd>Title for the plot.</dd>

            <dt><code>title_size</code></dt>
            <dd>Size of the title. Default is font_size.</dd>

            <dt><code>normalize</code></dt>
            <dd>A numeric. It scales the the drawing area to a new value. If normalize = 0.5, for instance, petals with height 0.5 will touch the drawing area border. Default is False, no rescaling (drawing area spans from 0 to 1).</dd>
        </dl>

        <h3>Return values</h3>
        <dl>
            <dt><code>ax</code></dt>
            <dd>The matplotlib.axes where the flower has been drawed on, for possible further customization.</dd>
        </dl>
    </div>
</div>

<?php include("footer.html") ?>