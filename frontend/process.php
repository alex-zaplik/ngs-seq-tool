<?php
//      $file_type = $_FILES['files']['type'][$i];
//      $file_size = $_FILES['files']['size'][$i];
//      $file_ext = strtolower(end(explode('.', $_FILES['files']['name'][$i])));


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  if (isset($_FILES['files'])) {
    $path = 'uploads/';
    $all_files = count($_FILES['files']['tmp_name']);

    $date = date('m:d:Y-h:i:s_', time());
    $prefix = $_POST['prefix'];
    $runs = $_POST['runs'];
    $samples = $_POST['samples'];
    $i7 = $_POST['i7'];
    $i5 = $_POST['i5'];
    $total = "";

    $fp2 = fopen('generated/command.txt', 'w');

    for ($i = 0; $i < $all_files; $i++) {
      //saves the file
      $file_name = $_FILES['files']['name'][$i];
      $file_tmp = $_FILES['files']['tmp_name'][$i];
      $file = $path . $date  . $file_name;
      move_uploaded_file($file_tmp, $file);

      //calculates the result
      $command = escapeshellcmd('python3 ../backend/main.py --path '. $file . " --indexing ". $prefix
      . " --runs ". $runs . " --samples " . $samples . " --i5 " . $i5 . " --i7 " . $i7);
      fwrite($fp2, $command);
      fwrite($fp2, "\n");
//      $total = $total . $command . "\n";
      $output = shell_exec($command);
      $total = $total ."FILE:\n". $file_name . "\n" . $output;
    }

    $fp = fopen('generated/tmp.txt', 'w');
    fwrite($fp, $total);
    fclose($fp);
    fclose($fp2);
  }
}

