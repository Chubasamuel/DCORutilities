/*
Code written by Jeremiah Chuba Samuel.

*/


/*
function fadeInfadeOut takes 
4 parameters,
>>obj= your HTML DOM containing the text to be animated.
>>interval= the frequency of the fadeInfadeOut in milliseconds
>>burst= whether the fading should be smooth, or in bursts. Value could be zero or one.
>>colors= specific colors to alternate
 in fading the text. each color could be
 in hex or any other css color formats
but make sure you separate each with a "*". If you desire no color change, 
put 0(zero) as your colors parameter.

eg
 var a=document.getElementById("myDiv");
 fadeInfadeOut(a,2000,1, "red*blue*#fde*#9fd4aa" );
 
 OR
 
 fadeInfadeOut(a, 300, 0, 0);
*/

function fadeInfadeOut(obj,interval,burst,colors){
var colorSel=0;
if(colors!=0){
colors=colors.split("*"); }
var startOp=1; var intC;var oper="-";
function doFade(){

if(startOp<=0&&burst==1){startOp=1; 
if(colors!=0){
if(colorSel<colors.length-1){colorSel+=1;}
else if(colorSel>=colors.length-1){colorSel=0;}
else{}
}}


if(burst==0){
if(startOp<=0){
oper="+";}
if(startOp>=1){
oper="-";} }
if(startOp<=0/*||startOp>=1*/){

if(colors!=0){
if(colorSel<colors.length-1){colorSel+=1;}
else if(colorSel>=colors.length-1){colorSel=0;}
else{}
}

}
obj.style.opacity=startOp;
obj.style.color=colors[colorSel];
var startOp2=startOp+""+oper+""+0.02;
startOp=eval(startOp2);
}

intC=setInterval(doFade,interval);
}



/*The 'burst' parameter determines whether the pattern of fading should be something like   012345>>543210. OR 012345>>012345.. */