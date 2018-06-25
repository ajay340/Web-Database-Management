<?php
$name = filter_input(INPUT_POST, 'first_name');
$salary = filter_input(INPUT_POST, 'salary');
$country = filter_input(INPUT_POST, 'country');
$city = filter_input(INPUT_POST, 'city');

if (!empty($name)){
if (!empty($salary)){
if (!empty($country)){
if (!empty($city)){
$host = "192.168.1.12";
$dbusername = "root";
$dbpassword = "admin123";
$dbname = "userdb";

// Create connection
$conn = new mysqli($host, $dbusername, $dbpassword, $dbname);

if (mysqli_connect_error()){
 die('Connect Error ('. mysqli_connect_errno() .') '
   . mysqli_connect_error());
}
else{
 $sql = "insert into userdb.materialdb_userdb (name,country,city,salary ) values ('$name', '$country', '$city', $salary);";

 if ($conn->query($sql)){
   echo "New record is inserted sucessfully";
 }
 else{
   echo "Error: ". $sql ."
". $conn->error;
 }
 $conn->close();
}
}
else{
 echo "Password should not be empty";
 die();
}
}
else{
 echo "Username should not be empty";
 die();
}
 ?>
