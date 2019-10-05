<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);
?>

<!DOCTYPE html>
<head>
    <title>Upload Files</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/main.css">
</head>

<body>
    <form class="upload-form" method="post" enctype="multipart/form-data">
        <input class="upload" type="file" name="files[]" multiple>
        <input class="upload" type="submit" value="Upload File" name="submit">
    </form>
</body>

</html>
<script src="js/upload.js"></script>
