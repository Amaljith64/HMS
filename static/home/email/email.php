<?php
if ($_POST)
{
    #####################################################################################################

    // Email Settings
    $site_title       = "Himara Hotel";
    $to_email         = "noreply@eagle-themes.com";
    $default_subject  = "Himara Hotel - New Message";

    // Output Messages
    $success_mssg   = "Your message has been sent successfully. Thank you.";
    $error_mssg     = "An error has occurred. Please check your PHP email configuration.";
    $short_mssg     = "Message is empty or too short! Please enter something.";
    $empty_subject  = "Subject is empty! Please enter something.";
    $empty_name     = "Name is empty! Please enter something.";
    $empty_phone    = "Phone is empty! Please enter something.";
    $email_mssg     = "Please enter a valid email!";

    //Email Text
    $tr_name    = "Name";
    $tr_email   = "Email";
    $tr_message = "Message";
    $tr_phone   = "Phone Number";

    #####################################################################################################

    //Check if its an ajax request, exit if not
    if (!isset($_SERVER['HTTP_X_REQUESTED_WITH']) AND strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) != 'xmlhttprequest') {

        //Exit script outputting json data
        $output = json_encode(
        array(
            'type'=>'error',
            'text' => 'Request must come from Ajax'
        ));

        die($output);
    }
    //Sanitize input data using PHP filter_var(). *PHP 5.2.0+
    $user_name        = filter_var($_POST["user_name"], FILTER_SANITIZE_STRING);
    $user_email       = filter_var($_POST["user_email"], FILTER_SANITIZE_EMAIL);
    $user_message     = filter_var($_POST["user_message"], FILTER_SANITIZE_STRING);
    $user_phone       = filter_var($_POST["user_phone"], FILTER_SANITIZE_STRING);
    $user_subject     = filter_var($_POST["user_subject"], FILTER_SANITIZE_STRING);

    // To make a field required please remove "//"

    if (empty($user_name)){$output = json_encode(array('type'=>'error', 'text' => $empty_name)); die($output);}
    // if (empty($user_phone)){$output = json_encode(array('type'=>'error', 'text' => $empty_phone)); die($output);}
    //if (empty($user_subject)){$output = json_encode(array('type'=>'error', 'text' => $empty_subject)); die($output);}

    //Check Email
    if (!filter_var($user_email, FILTER_VALIDATE_EMAIL)) {
        $output = json_encode(array('type'=>'error', 'text' => $email_mssg));
        die($output);
    }

    // If Subject is empty and not rquired use default subject
    if (empty($user_subject)) {
        $user_subject = $default_subject;
    }

    //Check Message
    if (strlen($user_message) < 10 ) {
        $output = json_encode(array('type'=>'error', 'text' => $short_mssg));
        die($output);
    }

    //Headers
    $headers = 'From: '.$site_title.' <'.$user_email.'>' . PHP_EOL .
    'Reply-To: '.$user_name.' <'.$user_email.'>' . PHP_EOL .
    'MIME-Version: 1.0' . PHP_EOL .
    'Content-type:text/html;charset=utf-8' . PHP_EOL .
    'X-Mailer: PHP/' . phpversion();
    $message = "-- Name: $user_name <br> -- Email: $user_email <br> -- Phone: $user_phone <br> -- Message: $user_message";
    $sendemail = @mail($to_email, $user_subject, $message, $headers);

    if (!$sendemail) {
        $output = json_encode(array('type'=>'error', 'text' => $error_mssg));
        die($output);
    } else {
        $output = json_encode(array('type'=>'message', 'text' => $success_mssg));
        die($output);
    }
} else {

    header('Location: ../404.html');

}
?>
