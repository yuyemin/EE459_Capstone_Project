<?php
        echo "SPRINKLER SETTINGS<br>";
        
        ini_set('display_errors', '1');
        $username="group15";
        $password="finalproject";
        $database="finalproject";
        mysql_connect("localhost",$username,$password);
        mysql_select_db($database) or die( "Unable to select database");

        // SCHEDULE
            
        $query= "SELECT * FROM Schedule";
        $result=mysql_query($query);

        echo "Weekly Schedule<br>";
        
        echo "<table border='1' cellpadding='10'>";
        echo "<tr><th>Day</th><th>Program(s)</th></tr>";

        while($row = mysql_fetch_array($result))
         {
          echo '<td>' . $row['Day'] . '</td>';
          echo '<td>' . $row['Time'] . '</td>';
          echo "</tr>"; 
          }
         echo "</table>";
         
         // PROGRAM 1
            
        $query= "SELECT * FROM Program1";
        $result=mysql_query($query);

        echo "Program 1<br>";
        
        echo "<table border='1' cellpadding='10'>";
        echo "<tr><th>Zone</th><th>Time(minutes)</th></tr>";

        while($row = mysql_fetch_array($result))
         {
          echo '<td>' . $row['Day'] . '</td>';
          echo '<td>' . $row['Time'] . '</td>';
          echo "</tr>"; 
          }
         echo "</table>";

    mysql_close();

?>