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

/***
 * Prints html table with predefined column names
 * @param $title string containing title for header for table
 * @param $data 2D array with information to fill the table.
 */
function show_2D_table($title, $data)
{

  echo "<h1>". $title . ":</h1>";
  if (empty($data))
  {
    echo "<p>Something went wrong :(</p>";
    return;
  }

  echo "<table>";
  echo "<tr>";
  echo "<th>label</th>";
  echo "<th>i5</th>";
  if (count($data[0]) > 3)
  {
    echo "<th>label</th>";
    echo "<th>i7</th>";
  }
  echo "</tr>";
  for ($row = 0; $row < count($data); $row++) {
    echo "<tr>";
    for ($col = 0; $col < count($data[$row]); $col++) {
      echo "<td>".$data[$row][$col]."</td>";
    }
    echo "</tr>";
  }
  echo "</table>";
}


