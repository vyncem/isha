<?php
$servername = "127.0.0.1";
$username = "root";
$password = "12345678";
$dbname = "ishaoffering";

try {
    $pdo = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully"; 

    $sql = "SELECT id, name, status FROM EVENTBRITE_CONFIG where status='ACTIVE'";
    $stmt = $pdo->query($sql);
    echo "<table><tr><th>ID</th><th>Name</th><th>Status</th></tr>";
	while ($row = $stmt->fetch()){
		echo "<tr><td>".$row["id"]."</td><td>".$row["name"]."</td><td>".$row["status"]."</td></tr>";
		$command = escapeshellcmd('/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/shaktikumar/projects/isha-offering-sessions/schedule.py');
		// echo $command;
		$output = shell_exec($command);
		if (strcmp($output,'1') != 0){
			echo "Job sceduling failed. Please see scheduler.log for more info.";
		}
	}
}
catch(PDOException $e){
    echo "Connection failed: " . $e->getMessage();
}
?>