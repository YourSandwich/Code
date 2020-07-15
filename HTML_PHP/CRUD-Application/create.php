<?php
// Include config file
require_once "config.php";
 
// Define variables and initialize with empty values
$Bezeichnung = $Label = $FSK = "";
$Bezeichnung_err = $Label_err = $FSK_err = "";
 
// Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){
    // Validate Bezeichnung
    $input_Bezeichnung = trim($_POST["Bezeichnung"]);
    if(empty($input_Bezeichnung)){
        $Bezeichnung_err = "Bitte einen Bezeichnung angeben.";
    } elseif(!filter_var($input_Bezeichnung, FILTER_VALIDATE_REGEXP, array("options"=>array("regexp"=>"/^[a-zA-Z\s]+$/")))){
        $Bezeichnung_err = "Bitte eine gültige Bezeichnung eintragen.";
    } else{
        $Bezeichnung = $input_Bezeichnung;
    }
    
    // Validate Label
    $input_Label = trim($_POST["Label"]);
    if(empty($input_Label)){
        $Label_err = "Bitte einen Label angeben.";     
    } else{
        $Label = $input_Label;
    }
    
    // Validate FSK
    $input_FSK = trim($_POST["FSK"]);
    if(empty($input_FSK)){
        $FSK_err = "Bitte eine FSK angeben.";     
    } elseif(!ctype_digit($input_FSK)){
        $FSK_err = "Bitte eine positive Zahl eintragen";
    } else{
        $FSK = $input_FSK;
    }
    
    // Check input errors before inserting in database
    if(empty($Bezeichnung_err) && empty($Label_err) && empty($FSK_err)){
        // Prepare an insert statement
        $sql = "INSERT INTO Computerspiel (Bezeichnung, Label, FSK) VALUES (?, ?, ?)";
         
        if($stmt = mysqli_prepare($link, $sql)){
            // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, "sss", $param_Bezeichnung, $param_Label, $param_FSK);
            
            // Set parameters
            $param_Bezeichnung = $Bezeichnung;
            $param_Label = $Label;
            $param_FSK = $FSK;
            
            // Attempt to execute the prepared statement
            if(mysqli_stmt_execute($stmt)){
                // Records created successfully. Redirect to landing page
                header("location: index.php");
                exit();
            } else{
                echo "Etwas ist schief gelaufen. Versuchen sie bitte nochmal.";
            }
        }
         
        // Close statement
        mysqli_stmt_close($stmt);
    }
    
    // Close connection
    mysqli_close($link);
}
?>
 
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Eintrag erstellen</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
    <style type="text/css">
        .wrapper{
            width: 500px;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="page-header">
                        <h2>Neuer Eintrag</h2>
                    </div>
                    <p>Bitte fühle diesen Formular aus um die Daten in die Datenbank einzutragen.</p>
                    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
                        <div class="form-group <?php echo (!empty($Bezeichnung_err)) ? 'has-error' : ''; ?>">
                            <label>Bezeichnung</label>
                            <input type="text" name="Bezeichnung" class="form-control" value="<?php echo $Bezeichnung; ?>">
                            <span class="help-block"><?php echo $Bezeichnung_err;?></span>
                        </div>
                        <div class="form-group <?php echo (!empty($Label_err)) ? 'has-error' : ''; ?>">
                            <label>Label</label>
                            <textarea name="Label" class="form-control"><?php echo $Label; ?></textarea>
                            <span class="help-block"><?php echo $Label_err;?></span>
                        </div>
                        <div class="form-group <?php echo (!empty($FSK_err)) ? 'has-error' : ''; ?>">
                            <label>FSK</label>
                            <input type="text" name="FSK" class="form-control" value="<?php echo $FSK; ?>">
                            <span class="help-block"><?php echo $FSK_err;?></span>
                        </div>
                        <input type="submit" class="btn btn-primary" value="Bestätigen">
                        <a href="index.php" class="btn btn-default">Abbrechen</a>
                    </form>
                </div>
            </div>        
        </div>
    </div>
</body>
</html>