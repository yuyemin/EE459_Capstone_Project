<html>
<head>
<title>Sprinkler Project Group 15</title>
<style>
div.content { width: 320px } 
body { font-family: Verdana, Geneva, sans-serif; }
</style>
</head>

<body>


<?php
// sets up MYSQL
    
    $username="group15";
    $password="finalproject";
    $database="finalproject";
    mysql_connect("localhost",$username,$password);
    mysql_select_db($database) or die( "Unable to select database");
    
    $curday = ((date("w") + 6) % 7) + 1;
    
    // SCHEDULE
    $query= "SELECT * FROM Schedule";
    $result=mysql_query($query);
    $schedNumbers = "0";
    while($row = mysql_fetch_array($result))
    {
        if ($row['Day'] == (string)$curday) {
            $schedNumbers = $row['Time'];
        }
    }
    
    $schedStr = "No Program";
    
    if ((int)$schedNumbers == 0) {
        $schedStr = "No Program";
    }
    else if ((int)$schedNumbers < 4){
        $schedStr = "Program {$schedNumbers}";
    }
    else {
        $schedStr = "Programs ";
        $strlen = strlen($schedNumbers);
        for ($i = 0; $i < ($strlen - 1); $i++) {
            $schedStr .= $schedNumbers[$i].",";
        }
        $schedStr .= $schedNumbers[$i];
    }
        
    

// sets up weather forecast information

include('lib/forecast.io.php');

$api_key = '9c41787b0de72946392e028d071e96d5';
$latitude = '34.0227';
$longitude = '-118.2798';
$units = 'us';  // Can be set to 'us', 'si', 'ca', 'uk' or 'auto' (see forecast.io API); default is auto
$lang = 'en'; // Can be set to 'en', 'de', 'pl', 'es', 'fr', 'it', 'tet' or 'x-pig-latin' (see forecast.io API); default is 'en'

$forecast = new ForecastIO($api_key, $units, $lang);

$condition = $forecast->getCurrentConditions($latitude, $longitude);

//echo 'Current Weather: '.$condition->getSummary(). "<br>";
//echo 'Current Temp: '.$condition->getTemperature(). "(˙F)<br>";

?>

<div class="content">
<div style="float:left; width:35%;border-right: 1px solid #888888;">
<center>
<img src="Climacons/SVG/Sun.svg" alt="Weather.img" style="width:110px;height:110px;"><br>
<?php echo htmlspecialchars($condition->getSummary()); ?> <br>
<?php echo htmlspecialchars($condition->getTemperature()); ?> (˙F) <br>
Soil: Dry <br>
<input type="button" value="Settings" onclick="location='settings.php'"/>
<br>
<br>
</center>
</div>
<div style="float:right; width:63%; margin-left:2px;">

<div style="color:#008ae6"><center><strong><u>SPRINKLER - GROUP 15</u></strong></center></div>
<br>
<b> Today: </b> <?php echo htmlspecialchars($schedStr); ?> <br>
<hr>
<center><b>Website</b></center>
http://<?php echo exec('hostname -I'); ?>/
<br>
<hr>
<center>
<strong><u> Manual Zone Controls </u></strong>
<input type="button" value="Skip Today" onclick="location='main_pretty.php'"/>
<input type="button" value="All Off" onclick="location='main_pretty.php'"/>
<br>
<input type="button" value="1" onclick="location='main_pretty.php'"/>
<input type="button" value="2" onclick="location='main_pretty.php'"/>
<input type="button" value="3" onclick="location='main_pretty.php'"/>
<input type="button" value="4" onclick="location='main_pretty.php'"/>
<input type="button" value="5" onclick="location='main_pretty.php'"/>
<input type="button" value="6" onclick="location='main_pretty.php'"/>
</center>
</div>
</div>


</body>

</html>