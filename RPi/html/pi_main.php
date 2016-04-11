<?php
include('lib/forecast.io.php');

// basic cs setup

echo "<body style='background-color:#f0f5f5'>";
echo "<div style='text-align:center'>";

$api_key = '9c41787b0de72946392e028d071e96d5';

$latitude = '34.0227';
$longitude = '-118.2798';
$units = 'us';  // Can be set to 'us', 'si', 'ca', 'uk' or 'auto' (see forecast.io API); default is auto
$lang = 'en'; // Can be set to 'en', 'de', 'pl', 'es', 'fr', 'it', 'tet' or 'x-pig-latin' (see forecast.io API); default is 'en'

$forecast = new ForecastIO($api_key, $units, $lang);

$condition = $forecast->getCurrentConditions($latitude, $longitude);

echo "<strong>SENIOR PROJECT GROUP 15</strong><br>";

echo 'Current Weather: '.$condition->getSummary(). "<br>";
echo 'Current Temp: '.$condition->getTemperature(). " (˙F)<br>";

?>

<input type="button" value="All Zones On" onclick="location='allOn.php'"/>
<input type="button" value="All Zones Off" onclick="location='allOff.php'"/>
<input type="button" value="Resume Normal Schedule" onclick="location='resume.php'"/>

<?php echo "<br>To use the full interface, type this address into a web browser:<br>http://", exec('hostname -I'),"/"; ?>