<?php
$servername = "localhost";
$username = "group15";
$password = "finalproject";

ini_set('display_errors', '1');

// Create connection
$conn = mysql_connect($servername, $username, $password);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?>