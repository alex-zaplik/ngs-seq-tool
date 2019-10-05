<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);

$index = 2;
$seq = 2;
$mat = 2;
$chan = 2;

$c1 = "active";
$c2 = "checked";
$c3 = "";
$c4 = "";

if($_SERVER['REQUEST_METHOD'] == 'POST'){
  $index = $_POST["index"];
  $seq = $_POST["seq"];
  $mat = $_POST["mat"];
  $chan = $_POST["buttons"];

  if ($chan == "4")
  {
    swap($c3, $c1);
    swap($c4, $c2);
  }
}
?>

<!DOCTYPE html>
<html class="h-100">
    <head>
        <title>Upload Files</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>

    <body class="h-100" style="background-color: #baed91;">

        <div style="position: absolute; top:5vw; right: 0vw" class="h3">
            <p style="transform: rotate(30deg); color: #8cb36d;">thinking out of the box!</p>
        </div>

        <div class="container h-100">
            <div class="row h-100 justify-content-center align-items-center">
                <form class="col-4 card" method="post" enctype="multipart/form-data">
                    <h1 class="my-3">Input</h1>

                    <div class="form-group">
                        <label for="formGroupExampleInput">Index count (rows):</label>
                        <input type="text" name="seq" class="form-control" id="sequence" value="<?php echo $seq ?>">
                    </div>

                    <div class="form-group">
                        <label for="formGroupExampleInput">Index length (columns):</label>
                        <input type="text" name="index" class="form-control" id="indexLength" value="<?php echo $index ?>">
                    </div>

                    <div class="form-group">
                        <label for="formGroupExampleInput">Group count:</label>
                        <input type="text" name="mat" class="form-control" id="matrix" value="<?php echo $mat ?>">
                    </div>


                    <div class="form-group btn-group btn-group-toggle" data-toggle="buttons">
                        <label class="btn btn-secondary <?php echo $c1 ?>">
                            <input type="radio" name="buttons" id="double" value="2" autocomplete="off" <?php echo $c2 ?>>2 channel
                        </label>
                        <label class="btn btn-secondary <?php echo $c3 ?>">
                            <input type="radio" name="buttons" id="quad" value="4" autocomplete="off" <?php echo $c4 ?>>4 channel
                        </label>
                    </div>

                      <div class="form-group">
                        <input class="upload btn btn-primary btn-block" type="submit" value="Calculate it!" name="submit">
                    </div>

                  <?php if($_SERVER['REQUEST_METHOD'] != 'POST'): ?>
                    <div class="form-group">
                        <a href="./" class="btn btn-secondary btn-block">Back to the homepage</a>
                    </div>

                  <?php else:
                    $command = escapeshellcmd('python3 ../backend/successCalculator.py '
                    . $chan . " " . $index . " " . $seq . " " . $mat);
                    $output = shell_exec($command);
                    $result = explode(" ", $output);
                    ?>
                    <hr>
                    <div class="form-group">
                        <label for="formGroupExampleInput">No error in column probability:</label>
                        <input type="text" class="form-control" id="column" value="<?php echo $result[0]*100 ."%"?>"disabled>
                    </div>

                    <div class="form-group">
                        <label for="formGroupExampleInput">No error in single group probability:</label>
                        <input type="text" class="form-control" id="matrixok" value="<?php echo $result[1]*100 ."%"?>" disabled>
                    </div>

                    <div class="form-group">
                        <label for="formGroupExampleInput">No error in all groups:</label>
                        <input type="text" class="form-control" id="matricesok" value="<?php echo floatval($result[2])*100 . "%"?>" disabled>
                    </div>

                    <div class="form-group">
                        <a href="./" class="btn btn-secondary btn-block">Back to the homepage</a>
                    </div>  
                    
<?php endif; ?>
                </form>
            </div> 
        </div>
    </body>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>