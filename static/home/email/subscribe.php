<?php

	include("inc/MailChimp.php");
	use \DrewM\MailChimp\MailChimp;

if($_POST)
{
  #####################################################################################################

    // Mailchimp settings
    $api_key = "9a206975bc491e90253b1dd8ffb0f2a3-us10"; // API Key
    $list_id = "ea7b16d0a9"; // List ID

    // Output Messages
    $success_mssg   = "Thank you, you have been added to our mailing list.";

  #####################################################################################################

	$MailChimp = new MailChimp($api_key);

	$result = $MailChimp->post("lists/$list_id/members", [
							'email_address' => $_POST["subscribe_email"],
							'status'        => 'subscribed',
						]);

	if ($MailChimp->success()) {
         $output = json_encode(array('type'=>'message', 'text' => $success_mssg));
        die($output);

	} else {
		$error_mssg = $MailChimp->getLastError();
        $output = json_encode(array('type'=>'error', 'text' => $error_mssg));
        die($output);
	}
}else{

    header('Location: ../404.html');

}
?>
