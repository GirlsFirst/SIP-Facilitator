/* 
breakout-part-1
Facilitator Code
SIP U3L5 

Sample code for Breakout Part 1
by Girls Who Code
March 2020

This reflects the code at the end of Lesson 5, Part 1.

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

ctx.beginPath();
ctx.rect(20, 40, 50, 50);
ctx.fillStyle = "#FF0000";
ctx.fill();
ctx.closePath();
*/

var x = canvas.width/2; //Starts at 240
var y = canvas.height-30; //Starts at 290

var dx = 2; //Value of the distance to move from x after each frame
var dy = -2; //Value of the distance to move from y after each frame

//The main loop
function draw(){
    ctx.clearRect(0, 0, canvas.width, canvas.height); //Clears the canvas
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI*2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
    x += dx; //This is the same as x = x + dx
    y += dy; //This is the same as y = y + dy
    console.log("x = " + x + ", y = " + y);

}
//How often we clear and redraw the canvas
setInterval(draw, 10);

/*

Here is the tidy code from step 6. It breaks the 
draw() function into two parts.

function drawBall() {
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI*2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBall();

    x += dx;
    y += dy;
}

*/
