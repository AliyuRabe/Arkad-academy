<?php
$name = $_POST[ 'name'];
$visitor_email = $_POST[ 'email'];
$subject = $_POST[ 'subject'];
$message = $_POST[ 'message'];

$email_from = 'aalinks1111@gmail.com';

$email_subject = 'New Form Submission';

 = "User Name: $name.\n".
            = "User email: $Visitor_email.\n".
            = "Subject: $subject.\n".
            = "User message: $message.\n";


$to = 'prince1stace@gmail.com';

$headers = "from: $email_from \r\n";
$headers .= "Reply-To: $visitor_email \r\n";

mail($to,$email_subject,$email_body,$headers)

header("location: contact.html")
?>