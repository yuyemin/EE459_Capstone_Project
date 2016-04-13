<?php
include('lib/forecast.io.php');

$api_key = '9c41787b0de72946392e028d071e96d5';

$latitude = '34.0227';
$longitude = '-118.2798';
$units = 'us';  // Can be set to 'us', 'si', 'ca', 'uk' or 'auto' (see forecast.io API); default is auto
$lang = 'en'; // Can be set to 'en', 'de', 'pl', 'es', 'fr', 'it', 'tet' or 'x-pig-latin' (see forecast.io API); default is 'en'

$forecast = new ForecastIO($api_key, $units, $lang);

$condition = $forecast->getCurrentConditions($latitude, $longitude);

echo "Current Location: Los Angeles, CA<br>";
echo 'Current Weather: '.$condition->getSummary(). "<br>";
echo 'Current Temp: '.$condition->getTemperature(). "(˙F)<br>";

?>

<input type="button" value="All Zones Off" onclick="location='final_main.php'"/>

<?php echo '<br>' ?>

<input type="button" value="Settings" onclick="location='settings.php'"/>