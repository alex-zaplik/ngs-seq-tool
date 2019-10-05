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
    <title>NGS indexing tool</title>
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