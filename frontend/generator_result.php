<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);

$command = escapeshellcmd('python3 ../backend/excerciseGenerator.py '
. $_POST['grp'] . " " . $_POST['row'] . " " . $_POST['col']);

$output = shell_exec($command);
$result = explode(" ", $output);

//echo $output;

echo $result[0];
for ($i = 1; $i < count($result); $i++)
{
  echo "<br>";
  echo $result[$i];

}
/*
*/


