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
