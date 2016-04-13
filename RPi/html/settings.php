<html>
<head>
<title>Group 15 Sprinkler Project</title>
<link rel="stylesheet" type="text/css" href="settings_style.css">
<style>
input[type='text'] { font-size: 36px; }
input[type='submit'] { font-size: 40px; }
input[type='button'] { font-size: 40px; }
</style>
</head>

<body>

<?php
    ini_set('display_errors', '1');
    
    // VARIABLES
    
    // default variable names (overwritten by what is taken in from mysql)
    $s1 = $s2 = $s3 = $s4 = $s5 = $s6 = $s7 = "0"; // no schedule on each day
    
    $p11 = $p12 = $p13 = $p14 = $p15 = $p16 = "0"; // all zones run for 0 minutes
    $p17 = "0500"; // program starts at 5am
    
    $p21 = $p22 = $p23 = $p24 = $p25 = $p26 = "0"; // all zones run for 0 minutes
    $p27 = "0500"; // program starts at 5am
    
    $p31 = $p32 = $p33 = $p34 = $p35 = $p36 = "0"; // all zones run for 0 minutes
    $p37 = "0500"; // program starts at 5am
    
    // MYSQL
    
    $username="group15";
    $password="finalproject";
    $database="finalproject";
    mysql_connect("localhost",$username,$password);
    mysql_select_db($database) or die( "Unable to select database");
    
    // SCHEDULE
    $query= "SELECT * FROM Schedule";
    $result=mysql_query($query);
    while($row = mysql_fetch_array($result))
    {
        if ($row['Day'] == "1") {
            $s1 = $row['Time'];
        }
        else if ($row['Day'] == "2") {
            $s2 = $row['Time'];
        }
        else if ($row['Day'] == "3") {
            $s3 = $row['Time'];
        }
        else if ($row['Day'] == "4") {
            $s4 = $row['Time'];
        }
        else if ($row['Day'] == "5") {
            $s5 = $row['Time'];
        }
        else if ($row['Day'] == "6") {
            $s6 = $row['Time'];
        }
        else if ($row['Day'] == "7") {
            $s7 = $row['Time'];
        }
    }
    
    // PROGRAM 1
    $query= "SELECT * FROM Program1";
    $result=mysql_query($query);
    while($row = mysql_fetch_array($result))
    {
        if ($row['Day'] == "1") {
            $p11 = $row['Time'];
        }
        else if ($row['Day'] == "2") {
            $p12 = $row['Time'];
        }
        else if ($row['Day'] == "3") {
            $p13 = $row['Time'];
        }
        else if ($row['Day'] == "4") {
            $p14 = $row['Time'];
        }
        else if ($row['Day'] == "5") {
            $p15 = $row['Time'];
        }
        else if ($row['Day'] == "6") {
            $p16 = $row['Time'];
        }
        else if ($row['Day'] == "7") {
            $p17 = $row['Time'];
        }
    }
    
    // PROGRAM 2
    $query= "SELECT * FROM Program2";
    $result=mysql_query($query);
    while($row = mysql_fetch_array($result))
    {
        if ($row['Day'] == "1") {
            $p21 = $row['Time'];
        }
        else if ($row['Day'] == "2") {
            $p22 = $row['Time'];
        }
        else if ($row['Day'] == "3") {
            $p23 = $row['Time'];
        }
        else if ($row['Day'] == "4") {
            $p24 = $row['Time'];
        }
        else if ($row['Day'] == "5") {
            $p25 = $row['Time'];
        }
        else if ($row['Day'] == "6") {
            $p26 = $row['Time'];
        }
        else if ($row['Day'] == "7") {
            $p27 = $row['Time'];
        }
    }
    
    // PROGRAM 3
    $query= "SELECT * FROM Program3";
    $result=mysql_query($query);
    while($row = mysql_fetch_array($result))
    {
        if ($row['Day'] == "1") {
            $p31 = $row['Time'];
        }
        else if ($row['Day'] == "2") {
            $p32 = $row['Time'];
        }
        else if ($row['Day'] == "3") {
            $p33 = $row['Time'];
        }
        else if ($row['Day'] == "4") {
            $p34 = $row['Time'];
        }
        else if ($row['Day'] == "5") {
            $p35 = $row['Time'];
        }
        else if ($row['Day'] == "6") {
            $p36 = $row['Time'];
        }
        else if ($row['Day'] == "7") {
            $p37 = $row['Time'];
        }
    }
    
    // SAVE CHANGES
    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // saves the new variables to the mysql database
        $s1 = $_POST["s1"];
        $s2 = $_POST["s2"];
        $s3 = $_POST["s3"];
        $s4 = $_POST["s4"];
        $s5 = $_POST["s5"];
        $s6 = $_POST["s6"];
        $s7 = $_POST["s7"];
        
        $p11 = $_POST["p11"];
        $p12 = $_POST["p12"];
        $p13 = $_POST["p13"];
        $p14 = $_POST["p14"];
        $p15 = $_POST["p15"];
        $p16 = $_POST["p16"];
        $p17 = $_POST["p17"];
        
        $p21 = $_POST["p21"];
        $p22 = $_POST["p22"];
        $p23 = $_POST["p23"];
        $p24 = $_POST["p24"];
        $p25 = $_POST["p25"];
        $p26 = $_POST["p26"];
        $p27 = $_POST["p27"];
        
        
        // here we want to save the variables to Mysql (baby steps)
        
        $query= "UPDATE Schedule SET Time={$s1} WHERE Day=1";
        $result=mysql_query($query);
        $query= "UPDATE Schedule SET Time={$s2} WHERE Day=2";
        $result=mysql_query($query);
        $query= "UPDATE Schedule SET Time={$s3} WHERE Day=3";
        $result=mysql_query($query);
        $query= "UPDATE Schedule SET Time={$s4} WHERE Day=4";
        $result=mysql_query($query);
        $query= "UPDATE Schedule SET Time={$s5} WHERE Day=5";
        $result=mysql_query($query);
        $query= "UPDATE Schedule SET Time={$s6} WHERE Day=6";
        $result=mysql_query($query);
        $query= "UPDATE Schedule SET Time={$s7} WHERE Day=7";
        $result=mysql_query($query);
        
        $query= "UPDATE Program1 SET Time={$p11} WHERE Day=1";
        $result=mysql_query($query);
        $query= "UPDATE Program1 SET Time={$p12} WHERE Day=2";
        $result=mysql_query($query);
        $query= "UPDATE Program1 SET Time={$p13} WHERE Day=3";
        $result=mysql_query($query);
        $query= "UPDATE Program1 SET Time={$p14} WHERE Day=4";
        $result=mysql_query($query);
        $query= "UPDATE Program1 SET Time={$p15} WHERE Day=5";
        $result=mysql_query($query);
        $query= "UPDATE Program1 SET Time={$p16} WHERE Day=6";
        $result=mysql_query($query);
        $query= "UPDATE Program1 SET Time={$p17} WHERE Day=7";
        $result=mysql_query($query);
        
        $query= "UPDATE Program2 SET Time={$p21} WHERE Day=1";
        $result=mysql_query($query);
        $query= "UPDATE Program2 SET Time={$p22} WHERE Day=2";
        $result=mysql_query($query);
        $query= "UPDATE Program2 SET Time={$p23} WHERE Day=3";
        $result=mysql_query($query);
        $query= "UPDATE Program2 SET Time={$p24} WHERE Day=4";
        $result=mysql_query($query);
        $query= "UPDATE Program2 SET Time={$p25} WHERE Day=5";
        $result=mysql_query($query);
        $query= "UPDATE Program2 SET Time={$p26} WHERE Day=6";
        $result=mysql_query($query);
        $query= "UPDATE Program2 SET Time={$p27} WHERE Day=7";
        $result=mysql_query($query);
        
        $query= "UPDATE Program3 SET Time={$p31} WHERE Day=1";
        $result=mysql_query($query);
        $query= "UPDATE Program3 SET Time={$p32} WHERE Day=2";
        $result=mysql_query($query);
        $query= "UPDATE Program3 SET Time={$p33} WHERE Day=3";
        $result=mysql_query($query);
        $query= "UPDATE Program3 SET Time={$p34} WHERE Day=4";
        $result=mysql_query($query);
        $query= "UPDATE Program3 SET Time={$p35} WHERE Day=5";
        $result=mysql_query($query);
        $query= "UPDATE Program3 SET Time={$p36} WHERE Day=6";
        $result=mysql_query($query);
        $query= "UPDATE Program3 SET Time={$p37} WHERE Day=7";
        $result=mysql_query($query);
        
        
        echo "Saved changes.";
        
        
    }
    
    mysql_close();
?>
<center>
<div class="datagrid">
<h1>Sprinkler Settings</h1>

<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
</div>

    <input type="submit" value="Save Changes">
    <input input type="button" value="Home Page" onclick="location='index.php'">
    <div class="datagrid">
    <h2>Schedule</h2>
    <table>
    <thead>
    <tr>
    <th>Day</th> <th>Program(s)</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Monday</td> 
        <td> <input type="text" name="s1" value = "<?php echo htmlspecialchars($s1); ?>" /> </td>
    </tr>
    <tr>
        <td>Tuesday</td> 
        <td> <input type="text" name="s2" value = "<?php echo htmlspecialchars($s2); ?>" /> </td>
    </tr>
    <tr>
        <td>Wednesday</td> 
        <td> <input type="text" name="s3" value = "<?php echo htmlspecialchars($s3); ?>" /> </td>
    </tr>
    <tr>
        <td>Thursday</td> 
        <td> <input type="text" name="s4" value = "<?php echo htmlspecialchars($s4); ?>" /> </td>
    </tr>
    <tr>
        <td>Friday</td> 
        <td> <input type="text" name="s5" value = "<?php echo htmlspecialchars($s5); ?>" /> </td>
    </tr> 
    <tr>
        <td>Saturday</td> 
        <td> <input type="text" name="s6" value = "<?php echo htmlspecialchars($s6); ?>" /> </td>
    </tr>
    <tr>
        <td>Sunday</td> 
        <td> <input type="text" name="s7" value = "<?php echo htmlspecialchars($s7); ?>" /> </td>
    </tr>
    </tbody>      
    </table>
    </div>
    
    <div class="datagrid">
    <h2>Program 1</h2>
    Time of Day (HHMM) <input type="text" name="p17" value = "<?php echo htmlspecialchars($p17); ?>" />
    
    
    <table>
    <thead>
    <tr>
    <th>Zone</th> <th>Run Time (min.)</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td> 
        <td> <input type="text" name="p11" value = "<?php echo htmlspecialchars($p11); ?>" /> </td>
    </tr>
    <tr>
        <td>2</td> 
        <td> <input type="text" name="p12" value = "<?php echo htmlspecialchars($p12); ?>" /> </td>
    </tr>
    <tr>
        <td>3</td> 
        <td> <input type="text" name="p13" value = "<?php echo htmlspecialchars($p13); ?>" /> </td>
    </tr>
    <tr>
        <td>4</td> 
        <td> <input type="text" name="p14" value = "<?php echo htmlspecialchars($p14); ?>" /> </td>
    </tr>
    <tr>
        <td>5</td> 
        <td> <input type="text" name="p15" value = "<?php echo htmlspecialchars($p15); ?>" /> </td>
    </tr> 
    <tr>
        <td>6</td> 
        <td> <input type="text" name="p16" value = "<?php echo htmlspecialchars($p16); ?>" /> </td>
    </tr>  
    </tbody>   
    </table>
    </div>
    
    <div class="datagrid">
    <h2>Program 2</h2>
    Time of Day (HHMM) <input type="text" name="p27" value = "<?php echo htmlspecialchars($p27); ?>" />
    
    <table>
    <thead>
    <tr>
    <th>Zone</th> <th>Run Time (min.)</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td> 
        <td> <input type="text" name="p21" value = "<?php echo htmlspecialchars($p21); ?>" /> </td>
    </tr>
    <tr>
        <td>2</td> 
        <td> <input type="text" name="p22" value = "<?php echo htmlspecialchars($p22); ?>" /> </td>
    </tr>
    <tr>
        <td>3</td> 
        <td> <input type="text" name="p23" value = "<?php echo htmlspecialchars($p23); ?>" /> </td>
    </tr>
    <tr>
        <td>4</td> 
        <td> <input type="text" name="p24" value = "<?php echo htmlspecialchars($p24); ?>" /> </td>
    </tr>
    <tr>
        <td>5</td> 
        <td> <input type="text" name="p25" value = "<?php echo htmlspecialchars($p25); ?>" /> </td>
    </tr> 
    <tr>
        <td>6</td> 
        <td> <input type="text" name="p26" value = "<?php echo htmlspecialchars($p26); ?>" /> </td>
    </tr>    
    </tbody> 
    </table>
    </div>
    
    <div class="datagrid">
    <h2>Program 3</h2>
    Time of Day (HHMM) <input type="text" name="p37" value = "<?php echo htmlspecialchars($p37); ?>" />
    
    <table>
    <thead>
    <tr>
    <th>Zone</th> <th>Run Time (min.)</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td> 
        <td> <input type="text" name="p31" value = "<?php echo htmlspecialchars($p31); ?>" /> </td>
    </tr>
    <tr>
        <td>2</td> 
        <td> <input type="text" name="p32" value = "<?php echo htmlspecialchars($p32); ?>" /> </td>
    </tr>
    <tr>
        <td>3</td> 
        <td> <input type="text" name="p33" value = "<?php echo htmlspecialchars($p33); ?>" /> </td>
    </tr>
    <tr>
        <td>4</td> 
        <td> <input type="text" name="p34" value = "<?php echo htmlspecialchars($p34); ?>" /> </td>
    </tr>
    <tr>
        <td>5</td> 
        <td> <input type="text" name="p35" value = "<?php echo htmlspecialchars($p35); ?>" /> </td>
    </tr> 
    <tr>
        <td>6</td> 
        <td> <input type="text" name="p36" value = "<?php echo htmlspecialchars($p36); ?>" /> </td>
    </tr>  
    </tbody>   
    </table>
    </div>
    
    
    

</form>

</body>
</html>