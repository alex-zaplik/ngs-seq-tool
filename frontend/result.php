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
    <title>Admin Page</title>
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
</head>
<body>




<?php
$fn = fopen("tmp.txt", "r");
$title = "";
$array = [];
while (!feof($fn)) {
  $result = fgets($fn);
//  echo "v=" . $result;
  //echo "<br>";
  if ($result == "FILE:\n")
  {
      if ($title != "")
      {
        show_2D_table($title, $array);
      }
      $title = fgets($fn);
  }
  else if ($result != "\n")
  {
    //$row = [$result];
    explode(" ", $result);
//    array_push($array, [1,2,3]);
  }
}
show_2D_table($title, $array);

fclose($fn);


?>

</body>