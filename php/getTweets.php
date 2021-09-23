<?php
if (!isset($_SERVER["REQUEST_METHOD"]) || $_SERVER["REQUEST_METHOD"] != "POST") {
    header("HTTP/1.1 400 Invalid Request");
    die("ERROR 400: Invalid request - This service accepts only POST requests.");
}

header("Content-type: application/json");
print "{\n";
    $filtQueryString = filter_input(INPUT_POST, "string", FILTER_SANITIZE_STRING);

    $output = passthru('python ../py/get_tweets.py '.$filtQueryString.'');
        print "  \"tweets\": ";
        print json_encode($output);


print "\n}\n";

?>