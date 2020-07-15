<?php
// Include config file
require_once "config.php";
 
// Define variables and initialize with empty values
$Bezeichnung = $Label = $FSK = "";
$Bezeichnung_err = $Label_err = $FSK_err = "";
 
// Processing form data when form is submitted
if(isset($_POST["id"]) && !empty($_POST["id"])){
    // Get hidden input value
    $id = $_POST["id"];
    
    // Validate name
    $input_Bezeichnung = trim($_POST["Bezeichnung"]);
    if(empty($input_Bezeichnung)){
        $Bezeichnung_err = "Bitte eine Bezeichnung eintragen";
    } elseif(!filter_var($input_Bezeichnung, FILTER_VALIDATE_REGEXP, array("options"=>array("regexp"=>"/^[a-zA-Z\s]+$/")))){
        $Bezeichnung_err = "Bitte eine Bezeichnung eintragen";
    } else{
        $Bezeichnung = $input_Bezeichnung;
    }
    
    // Validate address address
    $input_Label = trim($_POST["Label"]);
    if(empty($input_Label)){
        $Label_err = "Bitte einen Label eintragen";     
    } else{
        $Label = $input_Label;
    }
    
    // Validate salary
    $input_FSK = trim($_POST["FSK"]);
    if(empty($input_FSK)){
        $FSK_err = "Bitte eine Zahl eingeben.";     
    } elseif(!ctype_digit($input_FSK)){
        $FSK_err = "Bitte eine positive Zahl eingeben";
    } else{
        $FSK = $input_FSK;
    }
    
    // Check input errors before inserting in database
    if(empty($Bezeichnung_err) && empty($Label_err) && empty($FSK_err)){
        // Prepare an update statement
        $sql = "UPDATE Computerspiel SET Bezeichnung=?, Label=?, FSK=? WHERE ID=?";
         
        if($stmt = mysqli_prepare($link, $sql)){
            // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, "sssi", $param_Bezeichnung, $param_Label, $param_FSK, $param_id);
            
            // Set parameters
            $param_Bezeichnung = $Bezeichnung;
            $param_Label = $Label;
            $param_FSK = $FSK;
            $param_id = $id;
            
            // Attempt to execute the prepared statement
            if(mysqli_stmt_execute($stmt)){
                // Records updated successfully. Redirect to landing page
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
} else{
    // Check existence of id parameter before processing further
    if(isset($_GET["id"]) && !empty(trim($_GET["id"]))){
        // Get URL parameter
        $id =  trim($_GET["id"]);
        
        // Prepare a select statement
        $sql = "SELECT * FROM Computerspiel WHERE ID = ?";
        if($stmt = mysqli_prepare($link, $sql)){
            // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, "i", $param_id);
            
            // Set parameters
            $param_id = $id;
            
            // Attempt to execute the prepared statement
            if(mysqli_stmt_execute($stmt)){
                $result = mysqli_stmt_get_result($stmt);
    
                if(mysqli_num_rows($result) == 1){
                    /* Fetch result row as an associative array. Since the result set
                    contains only one row, we don't need to use while loop */
                    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
                    
                    // Retrieve individual field value
                    $Bezeichnung = $row["Bezeichnung"];
                    $Label = $row["Label"];
                    $FSK = $row["FSK"];
                } else{
                    // URL doesn't contain valid id. Redirect to error page
                    header("location: error.php");
                    exit();
                }
                
            } else{
                echo "Ups! Etwas ist schief gelaufen. Bitte versuchen sie es später noch einmal.";
            }
        }
        
        // Close statement
        mysqli_stmt_close($stmt);
        
        // Close connection
        mysqli_close($link);
    }  else{
        // URL doesn't contain id parameter. Redirect to error page
        header("location: error.php");
        exit();
    }
}
?>
 
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Update Record</title>
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
                        <h2>Eintrag aktualisieren</h2>
                    </div>
                    <p>Bitte ändere die Werte und bestätige um den Eintrag zu aktualisieren</p>
                    <form action="<?php echo htmlspecialchars(basename($_SERVER['REQUEST_URI'])); ?>" method="post">
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
                        <input type="hidden" name="id" value="<?php echo $id; ?>"/>
                        <input type="submit" class="btn btn-primary" value="Bestätigen">
                        <a href="index.php" class="btn btn-default">Abbrechen</a>
                    </form>
                </div>
            </div>        
        </div>
    </div>
</body>
</html>