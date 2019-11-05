/***
Code written by Jeremiah Chuba Samuel.

This programme generates unique or duplicate random integers.
>>var resultArray = generateRandom(minimumInteger,maximumInteger,howMany,allowDuplicate);
>> 4 arguments, first 3 should be integers while the fourth is a string with value "true" or "false".

To generate unique Integers, ((maximumInteger-minimumInteger)+1) must not be greater, but rather must be the same as the value provided for howMany OR it could be lesser or equal, but must be greater than 0;

***/
var tempRe=0;

function genRan(a){return Math.floor(Math.random()*a); }
function isDuplicate(element){
return element===this; }

function generateRandom(min,max,howMany,allowDuplicate){
var mi=parseInt(min); var ma= parseInt(max)+1; var ho=parseInt(howMany); var aL=allowDuplicate.toString().toLowerCase();
var count=0;
var result=[];

while(result.length<ho){

if(aL=="true"){
tempRe=genRan(ma);

while(tempRe<mi||tempRe>ma){
tempRe=genRan(ma); }

if(tempRe>=mi||tempRe<=ma){result[count]=tempRe; }

}
else if(aL=="false"){
var tempC=parseInt(max)-parseInt(min);
var tempH=parseInt(howMany);
if((tempC+1===tempH)||((tempH<=tempC)&&tempH>0)){

tempRe=genRan(ma);

while(tempRe<mi||tempRe>ma||result.some(isDuplicate,tempRe) ){
tempRe=genRan(ma);
}
if(tempRe>=mi||tempRe<=ma){result[count]=tempRe; }
}
else{
result="Invalid function arguments provided"; break;}
}
else{
result="Invalid function arguments provided"; break;}

count+=1;

}
return result;
}

module.exports= generateRandom;
//console.log(generateRandom(1,1000,60,"false"))
