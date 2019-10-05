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
  if (empty($title))
  {
    return;
  }

  echo "<p class='h4'>". $title . ":</p>";

  if (empty($data))
  {
    echo "<p>Something went wrong :(</p>";
    return;
  }

  echo "<table class='table table-sm'>";
  echo "<tr>";
  echo "<th scope='col'>label</th>";
  echo "<th scope='col'>i5</th>";

  if (count($data[0]) > 3)
  {
    echo "<th scope='col'>label</th>";
    echo "<th scope='col'>i7</th>";
  }
  echo "</tr>\n";
  for ($row = 0; $row < count($data); $row++) {
    echo "<tr scope='row'>";
    for ($col = 0; $col < count($data[$row]); $col++) {
      echo "<td >".$data[$row][$col]."</td>";
    }
    echo "</tr>\n";
  }
  echo "</table>\n";
}

/***
 * Swaps two values
 * @param $x string first value to swap
 * @param $y string second value to swap
 */

function swap(&$x, &$y) {
  $tmp=$x;
  $x=$y;
  $y=$tmp;
}

