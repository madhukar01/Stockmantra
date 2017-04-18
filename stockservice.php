<?php
ob_start();
extract($_GET);
header("Content-type: text/json");
$url = "https://www.google.com/finance/info?q=".$company;
    clearstatcache();
    $stockarr = array();
    $feed = file_get_contents($url);
    $arr = array("//","[","]","}","\n");
    $feed = str_replace($arr,"",$feed);
    $feed = explode("{", $feed);
    $stockval = (float)str_replace('"',"",explode(":",explode(",", $feed[   1])[5])[1]);
    $stockarr = [$company];
    $stockarr[1] = $stockval;
    $stockarr = json_encode($stockarr);
    echo $stockarr;
    ob_flush();
    flush();
?>