<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);
?>

<!DOCTYPE html>
<html class="h-100">
<head>
    <meta http-equiv='content-type' content='text/html;charset=utf-8' />
    <title>Results</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
<body class="h-100">
<div class="container">
  <div class="row h-100 justify-content-center align-items-center">
    <div class="col-4 card">
           
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
</div>
</div>
</div>
</body>
</html>