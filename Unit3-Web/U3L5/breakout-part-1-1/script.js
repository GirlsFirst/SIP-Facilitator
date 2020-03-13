/* 
breakout-part-1
Facilitator Code
SIP U3L5 

Sample code for Breakout Part 1
by Girls Who Code
March 2020

NOTE: This reflects the code at the end of PART 1: CANVAS

This project is adapted from the 2D breakout game using pure JavaScript
https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript 
created for Mozilla by the amazing MDN contributors.

*/


//Tell the DOM to find the canvas
var canvas = document.getElementById("myCanvas"); 

//Create the 2D drawing object
var ctx = canvas.getContext("2d");

/* 
Draw a rectangle - This is just an example of how to draw a shape
in Step 3. Move the * and / after the .closePath to comment it out or
delete it.
*/

ctx.beginPath();
ctx.rect(20, 40, 50, 50);
ctx.fillStyle = "#FF0000";
ctx.fill();
ctx.closePath();