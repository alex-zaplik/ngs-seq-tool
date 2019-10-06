<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);

// call python backend script
$command = escapeshellcmd('python3 ../backend/excerciseGenerator.py '
. $_POST['grp'] . " " . $_POST['row'] . " " . $_POST['col']);

$output = shell_exec($command);
$result = explode("\n", $output);
?>



<!DOCTYPE html>
<html class="h-100">
    <head>
        <title>Upload Files</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>

    <body class="h-100" style="background-color: #f8b88b;">

        <div style="position: absolute; top:5vw; right: 0vw" class="h3">
            <p style="transform: rotate(30deg); color: #8aa0ce;">thinking out of the box!</p>
        </div>

        <div class="container h-100">
            <div class="row h-100 justify-content-center align-items-center">
                <div class="col-4 card">
                  <h1 class="my-3">Results</h1>
                  <div class="form-group">
                    <a href="./" class="btn btn-secondary btn-block">Back to the homepage</a>
                  </div>
                  <ul class="list-group">

<?php
//display result.
//TODO: convert to 2D array
echo "<li class='list-group-item py-2 active'>".$result[0]."</li>";
for ($i = 1; $i < count($result); $i++)
{
  echo "<li class='list-group-item py-2'>".$result[$i]."</li>";
}
?>

                  </ul>
                  <div class="my-4">
                    <a href="./" class="btn btn-secondary btn-block">Back to the homepage</a>
                  </div>
                </div>
              </div>
            </div> 
        </div>
    </body>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>