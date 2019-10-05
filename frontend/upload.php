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

<body class="green">
    <h1 class="upload">File Upload</h1>
    <form class="upload-form" method="post" enctype="multipart/form-data">
        <input class="upload" type="file" name="files[]" id="file" multiple
               onchange="javascript:updateList()" />
        <br/>
        <div class="upload">
            Selected files:
        </div>
        <div class="upload" id="fileList">
        </div>
        <div class="upload">
            Runs:
        </div>
        <input id= "runs" class="upload" value="4">
        <div class="upload">
            Samples:
        </div>
        <input id = "samples" class="upload" value="6">
        <div class="upload">
            i7 column:
        </div>
        <input id = "i7" class="upload" value="0">
        <div class="upload">
            i5 column:
        </div>
        <input id = "i5" class="upload" value="1">
        <div class="upload">
        <input id="single" type="radio">Single &nbsp;Indexing
        </div>
        <div class="upload">
            <input type="radio">Double Indexing
        </div>
        <input class="upload" type="submit" value="Upload File" name="submit">
    </form>
</body>

</html>
<script src="js/upload.js"></script>
