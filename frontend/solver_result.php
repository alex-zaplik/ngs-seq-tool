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
$fn = fopen("generated/tmp.txt", "r");
$title = "";
$array = [];

while (!feof($fn)) {
  $result = fgets($fn);
  if ($result == "FILE:\n")
  {
      show_2D_table($title, $array);
      $array = [];
      $title = fgets($fn);
  }
  else if ($result != "\n")
  {
    array_push($array, explode(" ", $result));
  }
  else
  {
      array_push($array, [" ", " ", " ", " "]);
  }
}
show_2D_table($title, $array);

fclose($fn);


?>

</body>