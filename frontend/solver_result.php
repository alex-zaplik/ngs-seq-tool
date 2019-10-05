<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);
?>

<html>
<head>
    <title>NGS indexing tool</title>
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
</head>
<body>

<?php
//display last results present in generated/tmp.txt
//as table in html
$fn = fopen("generated/tmp.txt", "r");
$title = "";
$array = [];

//iterate over all the data line by line
while (!feof($fn)) {
  $result = fgets($fn);

  //file header
  if ($result == "FILE:\n")
  {
      //show the table
      show_2D_table($title, $array);
      //prepare for next table
      $array = [];
      $title = fgets($fn);
  }
  else if ($result != "\n")
  {
      //push data line
      array_push($array, explode(" ", $result));
  }
  else
  {
//      push empty line
      array_push($array, [" ", " ", " ", " "]);
  }
}
//show last table and close file
show_2D_table($title, $array);
fclose($fn);
?>
</body>