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
  <title>NGS indexing tool</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
<?php
//display result.
//TODO: convert to 2D array
for ($i = 0; $i < count($result); $i++)
{
  echo $result[$i];
  echo "<br>";
}
?>
</body>
</html>

