/****

Written by Jeremiah Chuba Samuel.

This script resizes images. JPG,PNG,GIF,BMP.

>>resizeImg($filename,$savePath,$new_width,$new_height)
>>Use same value for $savePath and $filename, if you wish to overwrite original file



****/


<?php
function resizeImg($filename,$savePath,$new_width,$new_height){
$ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));


if(!list($width,$height) = getimagesize($filename)){die("Unsupported picture type"); }

//$new_width = $width * $percent;
//$new_height = $height * $percent;

$image_p = imagecreatetruecolor($new_width,$new_height);

switch($ext){
case 'bmp':
$img = imagecreatefromwbmp($filename);
break;
case 'gif':
$img = imagecreatefromgif($filename);
break;
case 'jpg': 
$img = imagecreatefromjpeg($filename);
break;
case 'jpeg': 
$img = imagecreatefromjpeg($filename);
break;
case 'png': 
$img = imagecreatefrompng($filename);
break;
default : die("Unsupported picture type!");
}

if($ext== "gif"||$ext== "png"){
imagecolortransparent($image_p, imagecolorallocatealpha($image_p, 0, 0, 0, 127));
imagealphablending($image_p, false);
imagesavealpha($image_p, true);
}
imagecopyresampled($image_p,$img,0,0,0,0,$new_width,$new_height,$width,$height);

imagepng($image_p,$savePath); 
echo "SUCCESS"; }

/*if(isset($_GET["img"])){
resizeImg($_GET["img"],$_GET["img"],100,150);*/
}
?>