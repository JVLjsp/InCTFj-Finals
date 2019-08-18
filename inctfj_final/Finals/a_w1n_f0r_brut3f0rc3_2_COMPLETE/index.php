<?php
error_reporting(0);
include "./flag.php";
include "./config.php";
 
$black_list = "/union|0x|<|>|_|as|in|information|substr|mid|like| |user|if|select|limit|by|\`|or|admin|guest|\.|\(\)|and|if|database|concat|insert|having|sleep|benchmark/i"; 

if(preg_match($black_list, $_GET['user'])) exit(":P");
if(preg_match($black_list, $_GET['pass'])) exit(":P");

$query  = "select user from sqlauth where user={$_GET['user']} and # pw={$_GET['pass']}";
echo "<h2> query : ".$query."</h2>";
$result = @mysql_fetch_array(mysql_query($query)); 
if($result['user']) echo "<h2>Welcome {$result['user']}</h2>"; 

$admin_info =  @mysql_fetch_array(mysql_query('select * from sqlauth where user="admin"')); 

if(($admin_info['pw']) && ($admin_info['pw']===$_GET['pass'])){ 
    echo $flag; 
    } 
highlight_file(__FILE__)
?>
