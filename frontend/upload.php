<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require_once 'php/utils.php';
session_start();
move_not_logged_users($_SESSION);
?>

<!DOCTYPE html>
<html class="h-100">
    <head>
        <title>Upload Files</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/mainn.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>

    <body class="h-100"  style="background-color: #baed91;">
        <div class="container h-100">
            <div class="row h-100 justify-content-center align-items-center">
                <form class="col-4 card" method="post" enctype="multipart/form-data">
                    <h1 class="my-3">File Upload</h1>

                    <div class="form-group">
                        <input class="upload" type="file" name="files[]" id="file" multiple
                            onchange="javascript:updateList()" />
                    </div>



                    <div class="form-group">
                        <label for="formGroupExampleInput">Runs:</label>
                        <input type="text" class="form-control" id="runs" placeholder="Example input" value="4">
                    </div>

                    <div class="form-group">
                        <label for="formGroupExampleInput">Samples:</label>
                        <input type="text" class="form-control" id="samples" placeholder="Example input" value="6">
                    </div>


                    <div class="form-group">
                        <label for="formGroupExampleInput">i7 column:</label>
                        <input type="text" class="form-control" id="i7" placeholder="Example input" value="0">
                    </div>

                    <div class="form-group">
                        <label for="formGroupExampleInput">i5 column:</label>
                        <input type="text" class="form-control" id="i5" placeholder="Example input" value="1">
                    </div>      


                    <div class="form-group btn-group btn-group-toggle" data-toggle="buttons">
                        <label class="btn btn-secondary active">
                            <input type="radio" name="buttons" id="single" autocomplete="off" checked> Single Indexing
                        </label>
                        <label class="btn btn-secondary">
                            <input type="radio" name="buttons" id="double" autocomplete="off"> Double Indexing
                        </label>
                    </div>

                    <div class="form-group">
                        <input class="upload btn btn-primary btn-block" type="submit" value="Upload File" name="submit">
                    </div>      
                    

                </form> 
            </div>  
        </div>


    </body>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>
<script src="js/upload.js"></script>
