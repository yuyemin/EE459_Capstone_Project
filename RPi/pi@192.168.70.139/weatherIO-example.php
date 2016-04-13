<?php
include('lib/forecast.io.php');

$api_key = '9c41787b0de72946392e028d071e96d5';

$latitude = '34.0227';
$longitude = '-118.2798';
$units = 'us';  // Can be set to 'us', 'si', 'ca', 'uk' or 'auto' (see forecast.io API); default is auto
$lang = 'en'; // Can be set to 'en', 'de', 'pl', 'es', 'fr', 'it', 'tet' or 'x-pig-latin' (see forecast.io API); default is 'en'

$forecast = new ForecastIO($api_key, $units, $lang);

// all default will be
// $forecast = new ForecastIO($api_key);


/*
 * GET CURRENT CONDITIONS
 */
$condition = $forecast->getCurrentConditions($latitude, $longitude);

echo 'Current temperature: '.$condition->getTemperature(). "\n";


/*
 * GET HOURLY CONDITIONS FOR TODAY
 */
$conditions_today = $forecast->getForecastToday($latitude, $longitude);

echo "\n\nTodays temperature:\n";

foreach($conditions_today as $cond) {

    echo $cond->getTime('H:i:s') . ': ' . $cond->getTemperature(). "\n";

}

/*
 * GET DAILY CONDITIONS FOR NEXT 7 DAYS
 */
$conditions_week = $forecast->getForecastWeek($latitude, $longitude);

echo "\n\nConditions this week:\n";

foreach($conditions_week as $conditions) {

    echo $conditions->getTime('Y-m-d') . ': ' . $conditions->getMaxTemperature() . "\n";

}

/*
 * GET HISTORICAL CONDITIONS
 */
$condition = $forecast->getHistoricalConditions($latitude, $longitude, '2010-10-10T14:00:00-0700');

echo "\n\nTemperatur 2010-10-10: ". $condition->getMaxTemperature(). "\n";


