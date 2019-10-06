<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
set_time_limit(0);

//post value with files must be set
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  if (isset($_FILES['files'])) {
    //init variables
    $path = 'uploads/';
    $all_files = count($_FILES['files']['tmp_name']);
    $date = date('m:d:Y-h:i:s_', time());
    $prefix = $_POST['buttons'];
    $runs = $_POST['runs'];
    $samples = $_POST['samples'];
    $i7 = $_POST['i7'];
    $i5 = $_POST['i5'];
    $total = "";

    //prepare output files
    $commandFile = fopen('generated/command.txt', 'w');
    $outputFile = fopen('generated/tmp.txt', 'w');

    for ($i = 0; $i < $all_files; $i++) {
      //saves the file
      $file_name = $_FILES['files']['name'][$i];
      $file_tmp = $_FILES['files']['tmp_name'][$i];
      $file = $path . $date  . $file_name;
      move_uploaded_file($file_tmp, $file);

      $command = escapeshellcmd('python3 ../backend/main.py --path '. $file . " --indexing ". $prefix
      . " --runs ". $runs . " --samples " . $samples . " --i5 " . $i5 . " --i7 " . $i7);

      //append result to files
      fwrite($commandFile, $command);
      fwrite($commandFile, "\n");

      $output = shell_exec($command);
      $total = $total ."FILE:\n". $file_name . "\n" . $output;
    }

    //close result file
    fwrite($outputFile, $total);
    fclose($outputFile);
    fclose($commandFile);
    header('Location:solver_result.php');
  }
}

