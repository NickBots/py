<?php include("top.html") ?>
<link rel="stylesheet" href="../css/modaldef.css">
</head>
<?php include("bar.html") ?>
<?php include("modal_def.html") ?>

<div id="navbar-wrapper">
    <div id="navbar">
        <a href="./index.php">Home</a>
        <a href="./install.php">Install</a>
        <a class="active" href="./documentation.php">Documentation</a>
        <a href="./learn.php">Learn</a>
        <a href="./contribute.php">Contribute</a>
    </div>
</div>

<a href="./documentation_pyplutchik.php">
    <div class="featureBox">
        <div class="featureBoxContent">
            <h3>PyPlutchik</h3>
            <p>To access PyPlutchik documentation, click here</p>
        </div>

    </div>
</a>
<div id="main">
    <div id="page-guide">
        <span>Index</span>
        <ul>
            <li><a href="#load_spacy">load_spacy</a></li>
            <li><a href="#load_baseline">load_baseline</a></li>
            <li><a href="#baseline_distribution">baseline_distribution</a></li>
            <li><a href="#formamentis_network">formamentis_network</a></li>
            <li><a href="#emotions">emotions</a></li>
            <li><a href="#zscores">zscores</a></li>
            <li><a href="#stats">stats</a></li>
            <li><a href="#draw_plutchik">draw_plutchik</a></li>
        </ul>
    </div>

    <div id="functions-wrapper">

        <div class="function" id="load_spacy">
            <h2><code>load_spacy</code></h2>
            <p> Set a spacy model as the default for this object and return it.
                If no spacy_model will be inputed, a spacy model will be loaded according with the language parameter
            </p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>load_spacy(self, spacy_model, language)
                    load_spacy(self, spacy_model)</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>spacy_model</code></dt>
                <dd>Either a string or a spacy_model. If a string, it must be the name of a spacy model to load</dd>

                <dt><code>language</code></dt>
                <dd>Language of the text. Full support is offered for the languages supported by Spacy:
                    Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
                    Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
                    Limited support for other languages is available. By default, English will be loaded.</dd>

            </dl>

            <h3>Return values</h3>
            <dl>
                <dt><code>edges</code></dt>
                <dd>A list of 2-items tuples, defining the edgelist of the <button class="refFM">formamentis network</button></dd>

                <dt><code>vertex</code></dt>
                <dd>A list of string, defining the list of vertices of the network</dd>
            </dl>
        </div>

        <div class="function" id="load_baseline">
            <h2><code>load_baseline</code></h2>
            <p> Set as a baseline emotion distribution the inputed baseline.
                If no baseline is inputed, a new one will be created from the default emotion lexicon loaded.</p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>load_baseline(self, baseline)</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>spacy_model</code></dt>
                <dd>Either a list of lists, a text, or None.
                    If baseline is a list of list, it contains the distribution of emotions of the text used as baseline.
                    If baseline is a text, a new emotion distribution will be computed from it.
                    If baseline is None, it will be computed the emotion distribution of the default emotion lexicon loaded.</dd>
            </dl>
        </div>

        <div class="function" id="baseline_distribution">
            <h2><code>baseline_distribution</code></h2>
            <p> Gets the emotion distribution of the loaded baseline.</p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>baseline_distribution(self, emotionslist = None, emotion_model = 'plutchik', normalization_strategy = 'num_emotions'):</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>emotionslist</code></dt>
                <dd> A list of emotions. Default is None.</dd>

                <dt><code>emotion_model</code></dt>
                <dd>A model of emotions. Default is 'plutchik', that loads as emotions
                    ['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']</dd>

                <dt><code>normalization_strategy</code></dt>
                <dd>A string, whether to normalize emotion scores over the number of words. Accepted values are:
                    'none': no normalization at all
                    'text_lenght': normalize emotion counts over the total text length
                    'emotion_words': normalize emotion counts over the number of words associated to an emotion</dd>
            </dl>

            <h3>Return values</h3>
            <dl>
                <dt><code>TBD</code></dt>
                <dd>A list of lists ?</dd>
            </dl>
        </div>

        <div class="function" id="formamentis_network">
            <h2><code>formamentis_network</code></h2>
            <p> FormaMentis edgelist from input text. </p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>formamentis_network(self, text,
                    language = None,
                    spacy_model = None,
                    keepwords = [],
                    stopwords = [],
                    max_distance = 2)</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>text</code></dt>
                <dd>A string, the text to extract emotions from.</dd>

                <dt><code>language</code></dt>
                <dd>Language of the text. Full support is offered for the languages supported by Spacy:
                    Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
                    Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
                    Limited support for other languages is available. By default, English will be loaded.</dd>

                <dt><code>keepwords</code></dt>
                <dd> A list. Words that shall be included in <button class="refFM">formamentis networks</button> regardless from their part of speech. Default is an empty list.
                    By default implementation, a pre-compiled list of negations and pronouns will be loaded and used as keepwords.</dd>

                <dt><code>stopwords</code></dt>
                <dd>A list. Words that shall be discarded from <button class="refFM">formamentis networks</button> regardless from their part of speech. Default is an empty list.
                    If a word is both in stopwords and in keepwords, the word will be discarded.</dd>

                <dt><code>max_distance</code></dt>
                <dd> An integer, by default 2. Links in the <button class="refFM">formamentis network</button> will be established from each word to each neighbor within a distance
                    defined by max_distance.</dd>
            </dl>

            <h3>Return values</h3>
            <dl>
                <dt><code>edges</code></dt>
                <dd>A list of 2-items tuples, defining the edgelist of the <button class="refFM">formamentis network</button></dd>

                <dt><code>vertex</code></dt>
                <dd>A list of string, defining the list of vertices of the network</dd>
            </dl>
        </div>

        <div class="function" id="emotions">
            <h2><code>emotions</code></h2>
            <p> Count emotions in an inputed text or <button class="refFM">formamentis network</button>.</p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>emotions(self, obj,
                    emotion_lexicon = None,
                    normalization_strategy = 'none',
                    emotionslist = None,
                    language = None,
                    spacy_model = None,
                    duplicates = True,
                    negation_strategy = 'ignore',
                    negations = None,
                    antonyms = None,
                    method = 'default',
                    target_word = None,
                    emotion_model = 'plutchik')</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>obj</code></dt>
                <dd>Either a string or a list of tuples, with the former being the text to extract emotion from,
                    and the latter being the standard representation of a <button class="refFM">formamentis network</button> edgelist.</dd>

                <dt><code>emotion_lexicon</code></dt>
                <dd>A lexicon with every word-emotion association. By default, the <button class="refNRC">NRCLexicon</button> will be loaded.</dd>

                <dt><code>normalization_strategy</code></dt>
                <dd> A string, whether to normalize emotion scores over the number of words. Accepted values are:
                    'none': no normalization at all
                    'text_lenght': normalize emotion counts over the total text length
                    'emotion_words': normalize emotion counts over the number of words associated to an emotion
                </dd>

                <dt><code>emotionslist</code></dt>
                <dd>A list of emotions. Default is None.</dd>

                <dt><code>language</code></dt>
                <dd>Language of the text. Full support is offered for the languages supported by Spacy:
                    Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
                    Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
                    Limited support for other languages is available. By default, English will be loaded.
                </dd>

                <dt><code>spacy_model</code></dt>
                <dd>Either a string or a spacy_model. If a string, it must be the name of a spacy model to load</dd>

                <dt><code>duplicates</code></dt>
                <dd>A boolean: if True, words associated with emotions will be counted as many times as they appear into the wordlist.
                    If False, each word will be counted only once. Default is False.</dd>

                <dt><code>negation_strategy</code></dt>
                <dd> A string, if words introduced by negations will be replaced by their antynomies.
                    Default is 'ignore', for which no action will be done.
                    Other values accepted are 'replace', i.e. words introduced by negations will be replaced,
                    and 'delete', i.e. those words will be deleted.</dd>

                <dt><code>antonyms</code></dt>
                <dd>A dict. For each word in the dict's keys, the correspondent value is its antynomy.
                    Default is None: a pre-compiled dictionary will be loaded.</dd>

                <dt><code>negations</code></dt>
                <dd>A custom-defined list of negations.
                    Default is None: a pre-compiled list will be loaded.</dd>

                <dt><code>method</code></dt>
                <dd>A string, either 'default' or 'formamentis'.
                    If obj is a string and method is 'formamentis', the inputed text will be transformed into a <button class="refFM">formamentis network</button>
                    before extracting emotions.</dd>

                <dt><code>target_word</code></dt>
                <dd>A string or None. If a string and method is 'formamentis', it will be computed the emotion distribution
                    only of the neighborhood of 'target_word' in the <button class="refFM">formamentis network</button>.</dd>

                <dt><code>emotion_model</code></dt>
                <dd>A model of emotions. Default is 'plutchik', that loads as emotions
                    ['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']</dd>
            </dl>

            <h3>Return values</h3>
            <dl>
                <dt><code>emotions</code></dt>
                <dd>A dict. Keys are emotions, and values the scores. </dd>
            </dl>
        </div>

        <div class="function" id="zscores">
            <h2><code>zscores</code></h2>
            <p> Checks the emotion distribution in an inputed text or <button class="refFM">formamentis network</button> against a baseline, and return the z-scores.</p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>zscores(self, obj,
                    language = None,
                    spacy_model = None,
                    baseline = None,
                    emotion_lexicon = None,
                    duplicates = True,
                    negation_strategy = 'ignore',
                    antonyms = None,
                    negations = None,
                    n_samples = 300,
                    method = 'default',
                    target_word = None,
                    emotion_model = 'plutchik')</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>obj</code></dt>
                <dd>Either a string or a list of tuples, with the former being the text to extract emotion from,
                    and the latter being the standard representation of a <button class="refFM">formamentis network</button> edgelist.</dd>

                <dt><code>emotion_lexicon</code></dt>
                <dd>A lexicon with every word-emotion association. By default, the <button class="refNRC">NRCLexicon</button> will be loaded.</dd>

                <dt><code>normalization_strategy</code></dt>
                <dd> A string, whether to normalize emotion scores over the number of words. Accepted values are:
                    'none': no normalization at all
                    'text_lenght': normalize emotion counts over the total text length
                    'emotion_words': normalize emotion counts over the number of words associated to an emotion
                </dd>

                <dt><code>emotionslist</code></dt>
                <dd>A list of emotions. Default is None.</dd>

                <dt><code>language</code></dt>
                <dd>Language of the text. Full support is offered for the languages supported by Spacy:
                    Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
                    Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
                    Limited support for other languages is available. By default, English will be loaded.
                </dd>

                <dt><code>spacy_model</code></dt>
                <dd>Either a string or a spacy_model. If a string, it must be the name of a spacy model to load</dd>

                <dt><code>duplicates</code></dt>
                <dd>A boolean: if True, words associated with emotions will be counted as many times as they appear into the wordlist.
                    If False, each word will be counted only once. Default is False.</dd>

                <dt><code>negation_strategy</code></dt>
                <dd> A string, if words introduced by negations will be replaced by their antynomies.
                    Default is 'ignore', for which no action will be done.
                    Other values accepted are 'replace', i.e. words introduced by negations will be replaced,
                    and 'delete', i.e. those words will be deleted.</dd>

                <dt><code>antonyms</code></dt>
                <dd>A dict. For each word in the dict's keys, the correspondent value is its antynomy.
                    Default is None: a pre-compiled dictionary will be loaded.</dd>

                <dt><code>negations</code></dt>
                <dd>A custom-defined list of negations.
                    Default is None: a pre-compiled list will be loaded.</dd>

                <dt><code>method</code></dt>
                <dd>A string, either 'default' or 'formamentis'.
                    If obj is a string and method is 'formamentis', the inputed text will be transformed into a <button class="refFM">formamentis network</button>
                    before extracting emotions.</dd>

                <dt><code>target_word</code></dt>
                <dd>A string or None. If a string and method is 'formamentis', it will be computed the emotion distribution
                    only of the neighborhood of 'target_word' in the <button class="refFM">formamentis network</button>.</dd>

                <dt><code>emotion_model</code></dt>
                <dd>A model of emotions. Default is 'plutchik', that loads as emotions
                    ['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']</dd>

                <dt><code>n_samples</code></dt>
                <dd> An integer, how many time the baseline emotion distribution will be sampled before checking for z-scores.
                    Default is 300.</dd>
            </dl>

            <h3>Return values</h3>
            <dl>
                <dt><code>z-scores</code></dt>
                <dd>A dict. Keys are emotions, and values the z-scores.</dd>
            </dl>
        </div>

        <div class="function" id="stats">
            <h2><code>stats</code></h2>
            <p> Checks the input text or <button class="refFM">formamentis network</button>, and return a dict of statistics about words, emotions and negations.</p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>lstats(self, obj,
                    emotion_lexicon = None,
                    emotionslist = None,
                    language = None,
                    spacy_model = None,
                    duplicates = True,
                    negation_strategy = 'ignore',
                    negations = None,
                    antonyms = None,
                    method = 'default',
                    target_word = None,
                    emotion_model = 'plutchik'):</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>obj</code></dt>
                <dd>Either a string or a list of tuples, with the former being the text to extract emotion from,
                    and the latter being the standard representation of a formamentis edgelist.</dd>

                <dt><code>emotion_lexicon</code></dt>
                <dd>A lexicon with every word-emotion association. By default, the <button class="refNRC">NRCLexicon</button> will be loaded.</dd>

                <dt><code>emotionslist</code></dt>
                <dd>A list of emotions. Default is None.</dd>

                <dt><code>language</code></dt>
                <dd>Language of the text. Full support is offered for the languages supported by Spacy:
                    Catalan, Chinese, Danish, Dutch, English, French, German, Greek, Japanese, Italian, Lithuanian,
                    Macedonian, Norvegian, Polish, Portuguese, Romanian, Russian, Spanish.
                    Limited support for other languages is available. By default, English will be loaded.
                </dd>

                <dt><code>spacy_model</code></dt>
                <dd>Either a string or a spacy_model. If a string, it must be the name of a spacy model to load</dd>

                <dt><code>duplicates</code></dt>
                <dd>A boolean: if True, words associated with emotions will be counted as many times as they appear into the wordlist.
                    If False, each word will be counted only once. Default is False.</dd>

                <dt><code>negation_strategy</code></dt>
                <dd> A string, if words introduced by negations will be replaced by their antynomies.
                    Default is 'ignore', for which no action will be done.
                    Other values accepted are 'replace', i.e. words introduced by negations will be replaced,
                    and 'delete', i.e. those words will be deleted.</dd>

                <dt><code>antonyms</code></dt>
                <dd>A dict. For each word in the dict's keys, the correspondent value is its antynomy.
                    Default is None: a pre-compiled dictionary will be loaded.</dd>

                <dt><code>negations</code></dt>
                <dd>A custom-defined list of negations.
                    Default is None: a pre-compiled list will be loaded.</dd>

                <dt><code>method</code></dt>
                <dd>A string, either 'default' or 'formamentis'.
                    If obj is a string and method is 'formamentis', the inputed text will be transformed into a <button class="refFM">formamentis network</button>
                    before extracting emotions.</dd>

                <dt><code>target_word</code></dt>
                <dd>A string or None. If a string and method is 'formamentis', it will be computed the emotion distribution
                    only of the neighborhood of 'target_word' in the <button class="refFM">formamentis network</button>.</dd>

                <dt><code>emotion_model</code></dt>
                <dd>A model of emotions. Default is 'plutchik', that loads as emotions
                    ['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']</dd>
            </dl>

            <h3>Return values</h3>
            <dl>
                <dt><code>z-scores</code></dt>
                <dd>A dict of statistics about words, emotions and negations in text.</dd>
            </dl>
        </div>

        <div class="function" id="draw_plutchik">
            <h2><code>draw_plutchik</code></h2>
            <p> Draw the emotions or dyads Plutchik flower.
                Full details <a href="./documentation_pyplutchik.php">here</a></p>
            <h3>Syntax</h3>
            <div class="code-ex">
                <code>def draw_plutchik(self, scores,
                    ax = None,
                    rescale = False,
                    reject_range = None,
                    highlight = 'all',
                    show_intensity_levels = 'none',
                    font = None,
                    fontweight = 'light',
                    fontsize = 15,
                    show_coordinates = True,
                    show_ticklabels = False,
                    ticklabels_angle = 0,
                    ticklabels_size = 11,
                    height_width_ratio = 1,
                    title = None,
                    title_size = None):</code>
            </div>

            <h3>Required arguments</h3>
            <dl>
                <dt><code>scores</code></dt>
                <dd> A dictionary with emotions or dyads.
                    For each entry, values accepted are a 3-values iterable (for emotions only) or a scalar value between 0 and 1.
                    The sum of the 3-values iterable values must not exceed 1, and no value should be negative.
                    See emo_params() and dyad_params() for accepted keys.
                    Emotions and dyads are mutually exclusive. Different kinds of dyads are mutually exclusive.</dd>

                <dt><code>ax</code></dt>
                <dd>Axes to draw the coordinates</dd>

                <dt><code>rescale</code></dt>
                <dd>Either None or a 2-item tuple, with minimum and maximum value of the printable area.</dd>

                <dt><code>reject_range</code></dt>
                <dd>A 2-item tuple. All petal scores that fall within the range must be considered non-interesting, thus drawed in grey.
                    Default is None (no range at all).</dd>

                <dt><code>highlight</code></dt>
                <dd>A string or a list of main emotions to highlight. If a list of emotions is given, other emotions will be shadowed.
                    Default is 'all'.</dd>

                <dt><code>show_intensity_levels</code></dt>
                <dd> A string or a list of main emotions. It shows all three intensity scores for each emotion in the list,
                    and for the others cumulative scores. Default is 'none'.</dd>

                <dt><code>font</code></dt>
                <dd> Font of text. Default is sans-serif.</dd>

                <dt><code>fontweight</code></dt>
                <dd>Font weight of text. Default is light.</dd>

                <dt><code>fontsize</code></dt>
                <dd>Font size of text. Default is 15.</dd>

                <dt><code>show_coordinates</code></dt>
                <dd>A boolean, wether to show polar coordinates or not.</dd>

                <dt><code>show_ticklabels</code></dt>
                <dd>Boolean, wether to show tick labels under Joy petal. Default is False.</dd>

                <dt><code>ticklabels_angle</code></dt>
                <dd>How much to rotate tick labels from y=0. Value should be given in radians. Default is 0.</dd>

                <dt><code>ticklabels_size</code></dt>
                <dd>Size of tick labels. Default is 11.</dd>

                <dt><code>height_width_ratio</code></dt>
                <dd>Ratio between height and width of the petal. Lower the ratio, thicker the petal. Default is 1.</dd>

                <dt><code>title</code></dt>
                <dd>Title for the plot.</dd>

                <dt><code>title_size</code></dt>
                <dd>Size of the title. Default is font_size.</dd>
            </dl>

            <h3>Return values</h3>
            <dl>
                <dt><code>ax</code></dt>
                <dd>The input Axes modified, if provided, otherwise a new generated one.</dd>
            </dl>
        </div>
    </div>


</div>
<?php include("footer.html") ?>