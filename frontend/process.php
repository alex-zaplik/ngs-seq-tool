<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  if (isset($_FILES['files'])) {
    $path = 'uploads/';
    $all_files = count($_FILES['files']['tmp_name']);

    $date = date('m:d:Y-h:i:s_', time());
    $prefix = $_POST['prefix'];

    for ($i = 0; $i < $all_files; $i++) {
      $file_name = $_FILES['files']['name'][$i];
      $file_tmp = $_FILES['files']['tmp_name'][$i];
      $file_type = $_FILES['files']['type'][$i];
      $file_size = $_FILES['files']['size'][$i];
      $file_ext = strtolower(end(explode('.', $_FILES['files']['name'][$i])));
      $file = $path . $date  . $file_name;
      move_uploaded_file($file_tmp, $file);
    }


  }
}