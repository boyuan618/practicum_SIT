<?php 
 
/* 
 * Helper function to authenticate the login. 
 */ 
function authenticateUser() 
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
        $stmt = $conn->prepare("SELECT * FROM world_of_pets_members WHERE 
email=?"); 
 
        // Bind & execute the query statement: 
        $stmt->bind_param("s", $email); 
        $stmt->execute(); 
        $result = $stmt->get_result(); 
        if ($result->num_rows > 0) 
        { 
            // Note that email field is unique, so should only have 
            // one row in the result set. 
            $row = $result->fetch_assoc(); 
            $fname = $row["fname"]; 
            $lname = $row["lname"]; 
            $pwd_hashed = $row["password"]; 
 

            // Check if the password matches: 
            if (!password_verify($_POST["pwd"], $pwd_hashed)) 
            { 
                // Don't be too specific with the error message - hackers don't 
                // need to know which one they got right or wrong. :) 
                $errorMsg = "Email not found or password doesn't match..."; 
                $success = false; 
            } 
        } 
        else 
        { 
            $errorMsg = "Email not found or password doesn't match..."; 
            $success = false; 
        } 
        $stmt->close(); 
    } 
 

    $conn->close(); 
}


$email = $pwd_hashed = $errorMsg = "";
$success = true;

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

if (empty($_POST["pwd"])) 
{
    $errorMsg .= "Password is required.<br>";
    $success = false; 
}
else {
    $pwd_hashed = password_hash($_POST["pwd"], PASSWORD_DEFAULT);
}

authenticateUser();



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
    echo "<h1>Login successful!</h1>"; 
    echo "<h2>Welcome back, " . $fname . " " . $lname . ".</h2>";
        echo "<p><a href='./'>Return to Home</a></p>";
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
    echo "<h1>Oops!</h1>";
    echo "<h2>The following errors were detected: </h2>";
    echo "<p>" . $errorMsg . "</p>";
    echo "<p><a href='./login.php'>Return to Login</a></p>";
    echo '</main>
    </body>';
    include "footer.inc.php";
    echo '</body>
    </html>';
    }


function sanitize_input($data) 
{ 
   $data = trim($data);
   $data = stripslashes($data); 
   $data = htmlspecialchars($data);
   return $data; 
} 
?> 