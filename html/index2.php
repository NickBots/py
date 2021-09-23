<!DOCTYPE html>
<html lang="en">

<head>
<title>Homepage - PyPlutchik</title>
<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<script src="../js/test.js"></script>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="../js/plutchik.js"></script>
  <link rel="stylesheet" href="../css/common.css">
  <link rel="stylesheet" href="../css/main.css">
  <link type="text/css" rel="stylesheet" href="../css/plutchik.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
</head>

<body>

  <div class="header">
    <img class="logoHeader" alt="PyPlutchik" src="../resources/logo.png">
    <p class="logoHeader"> The package for text sentiment analysis with python </p>
  </div>

  <ul>
    <li><a class="active" href="#home">Home</a></li>
    <li><a href="./install.html">Install</a></li>
    <li><a href="./documentation.html">Documentation</a></li>
    <li><a href="./learn.html">Learn</a></li>
    <li><a href="./contribute.html">Contribute</a></li>
  </ul>

  <div class="feature">

    <div class="column">
      <div class="featureBox">
        <h3>LOREM IPSUM</h3>
        <p>Lorem ipsum dolor sit amet</p>
      </div>
      <div class="featureBox">
        <h3>LOREM IPSUM</h3>
        <p>Lorem ipsum dolor sit amet</p>
      </div>
    </div>

    <div class="column">
      <div class="featureBox">
        <h3>LOREM IPSUM</h3>
        <p>Lorem ipsum dolor sit amet</p>
      </div>
      <div class="featureBox">
        <h3>LOREM IPSUM</h3>
        <p>Lorem ipsum dolor sit amet</p>
      </div>
    </div>

    <div id="column_1">
      <div class="featureBox">
        <h3>LOREM IPSUM</h3>
        <p>Lorem ipsum dolor sit amet</p>
      </div>
      <div class="featureBox">
        <h3>LOREM IPSUM</h3>
        <p>Lorem ipsum dolor sit amet</p>
      </div>
    </div>
  </div>

  <hr>


  <div>
    <div class="tab">
      <button class="tabButton" onclick="openTestPanel(event, 'TextUpload')">Text</button>
      <button class="tabButton" onclick="openTestPanel(event, 'FileUpload')">Upload file</button>
      <button class="tabButton" onclick="openTestPanel(event, 'AccSubmit')">Tweet</button>
      <button class="tabButton" onclick="openTestPanel(event, 'RandomGeneration')">Random flower</button>
    </div>


    <div id="FileUpload" class="tabElement">
      <p>Upload text(Only .txt allowed): </p>
      <input id="uploadText" type="file" name="uploadPreview">
      <button id="upload">UPLOAD</button><br>
    </div>

    <div id="AccSubmit" class="tabElement">
      <input type="text" id="query" name="query" placeholder="Search">
      <button id="search">Search</button><br>
    </div>

    <div id="TextUpload" class="tabElement">
      <textarea id="userInput" placeholder="Insert text here" maxlength="2000"></textarea><br>
      <button id="submitUserInput">Submit</button>
    </div>

    <div id="RandomGeneration" class="tabElement">
      <button id="generate_random">Generate random emotion value</button>
    </div>
    <div id="chart"></div>
    
  </div>

</body>

</html>