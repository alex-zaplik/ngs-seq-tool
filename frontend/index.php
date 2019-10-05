<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);

?>
<html>
<head>
    <meta http-equiv='content-type' content='text/html;charset=utf-8' />
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
</head>
<body class="hider">
    <div class="container">
        <div class="leftpane">
            <div class="centered">
                <h1>Upload</h1>
                    <a href="upload.php" class="big">
                        <i class="fas fa-file-upload"></i>
                    </a>
            </div>
        </div>
        <div class="middlepane">
            <div class="centered">
                <h1>Calculate</h1>
                    <a href="calc.php" class="big">
                        <i class="fas fa-calculator"></i>
                    </a>
            </div>
        </div>
        <div class="rightpane">
            <div class="centered">
                <h1>Generate</h1>
                    <a href="generate.php" class="big">
                        <i class="fas fa-dna"></i>
                    </a>
            </div>
        </div>
    </div>
</body>
</html>