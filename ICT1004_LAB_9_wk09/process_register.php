<?php

/* 
 * Helper function to write the member data to the DB 
 */ 
function saveMemberToDB() 
{ 
    global $fname, $lname, $email, $pwd_hashed, $errorMsg, $success; 
 

    // Create database connection. 
    $config = parse_ini_file('../../private/db-config.ini'); 
    $conn = new mysqli($config['servername'], $config['username'], 
            $config['password'], $config['dbname']); 
 
    // Check connection 
    if ($conn->connect_error) 
    { 
        $errorMsg = "Connection failed: " . $conn->connect_error; 
        $success = false; 
    } 
    else 
    { 
        // Prepare the statement: 
        $stmt = $conn->prepare("INSERT INTO world_of_pets_members (fname, lname, 
email, password) VALUES (?, ?, ?, ?)"); 
 
        // Bind & execute the query statement: 
        $stmt->bind_param("ssss", $fname, $lname, $email, $pwd_hashed); 
        if (!$stmt->execute()) 
        { 
            $errorMsg = "Execute failed: (" . $stmt->errno . ") " . $stmt->error; 
            $success = false; 
        } 
        $stmt->close(); 
    } 
 
    $conn->close(); 
} 


$email = $fname = $lname = $pwd = $pwd_confirm = $errorMsg = ""; 
$success = true; 
//First name
if (empty($_POST["fname"])) 
{
;
}
else
{
    $fname = sanitize_input($_POST["fname"]);
}

//Last name
if (empty($_POST["lname"])) 
{
    $errorMsg .= "Last name is required.<br>";
    $success = false; 
}
else {
    $lname = sanitize_input($_POST["lname"]);
}

//Email
if (empty($_POST["email"])) 
{ 
    $errorMsg .= "Email is required.<br>";
    $success = false; 
} 
else
{ 
    $email = sanitize_input($_POST["email"]); 
    // Additional check to make sure e-mail address is well  -formed.
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) 
    { 
    $errorMsg .= "Invalid email format."; 
    $success = false;
    } 

} 

//Password
if (empty($_POST["pwd"])) 
{
    $errorMsg .= "Password is required.<br>";
    $success = false; 
}
else {
    $pwd = password_hash($_POST["pwd"], PASSWORD_DEFAULT);
}

//Password Confirmed
if (empty($_POST["pwd_confirm"])) 
{
    $errorMsg .= "Password confirmation is required.<br>";
    $success = false; 
}
else {
    $pwd_confirm = password_hash($_POST["pwd_confirm"], PASSWORD_DEFAULT);
}

//Check password == password_confirm
if ($_POST["pwd"] !== $_POST["pwd_confirm"]) {
    $errorMsg .= "Password and password confirmation do not match.<br>";
    $success = false;
} else {
    $pwd_hashed = $pwd;
}


saveMemberToDB();



if ($success) 
    { 
    echo '<!DOCTYPE html><html><head>
    <title>World of Pets</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet"
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity=
        "sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css">
    <script defer src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous">
    </script>
    <script defer src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"
        integrity="sha384-6khuMg9gaYr5AxOqhkVIODVIvm9ynTT5J4V1cfthmT+emCG6yVmEZsRHdxlotUnm"
        crossorigin="anonymous">
    </script>
    <script defer src="js/main.js"></script>
    </head>
    <body>';
    include "nav.inc.php";
    echo '<main class="container">';
    echo "<h4>Registration successful!</h4>"; 
    echo "<p>Email: " . $email;
    echo '</main>
    </body>';
    include "footer.inc.php";
    echo '</body>
    </html>';
    } 
    else
    { 
    echo '<!DOCTYPE html><html><head>
    <title>World of Pets</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet"
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity=
        "sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css">
    <script defer src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous">
    </script>
    <script defer src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"
        integrity="sha384-6khuMg9gaYr5AxOqhkVIODVIvm9ynTT5J4V1cfthmT+emCG6yVmEZsRHdxlotUnm"
        crossorigin="anonymous">
    </script>
    <script defer src="js/main.js"></script>
    </head>
    <body>';
    include "nav.inc.php";
    echo '<main class="container">';
    echo "<h4>The following input errors were detected:</h4>"; 
    echo "<p>" . $errorMsg . "</p>";
    echo '</main>
    </body>';
    include "footer.inc.php";
    echo '</body>
    </html>';
    }

//Helper function that checks input for malicious or unwanted content. 
function sanitize_input($data) 
{ 
   $data = trim($data);
   $data = stripslashes($data); 
   $data = htmlspecialchars($data);
   return $data; 
} 
?>