<?php

/**
 * Checks for session variable.
 * If user is not logged move to login page
 * Otherwise do nothing
 * @param array $SESSION_VARIABLE associative array with session variables
 */
function move_not_logged_users($SESSION_VARIABLE)
{
  $loginPage = 'LOCATION:login.php';
  if(! isset($SESSION_VARIABLE['login'])) {
    header($loginPage);
    die();
  }
  if($SESSION_VARIABLE['login'] === false) {
    header($loginPage);
    die();
  }
}

function show_2D_table($title, $data)
{
  echo $title;
  echo "<br>";

  echo count($data);
  echo "<br>";
  for ($row = 0; $row < count($data); $row++) {
    echo "<p><b>Row number $row</b></p>";
    echo "<ul>";
    for ($col = 0; $col < 3; $col++) {
      echo "<li>".$data[$row][$col]."</li>";
    }
    echo "</ul>";
  }
}


