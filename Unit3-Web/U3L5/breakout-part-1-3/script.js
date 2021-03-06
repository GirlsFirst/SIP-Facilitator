/* 
breakout-part-1
Facilitator Code
SIP U3L5 

Sample code for Breakout Part 1
by Girls Who Code
March 2020

NOTE: This reflects the code at the end of PART 3: COLLISION

This project is adapted from the 2D breakout game using pure JavaScript
https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript 
created for Mozilla by the amazing MDN contributors.

*/


//Tell the DOM to find the canvas
var canvas = document.getElementById("myCanvas"); 

//Create the 2D drawing object
var ctx = canvas.getContext("2d");

//DEFINE ALL OF YOUR VARIABLES UP HERE
var x = canvas.width/8; //Starts at 60
var y = canvas.height-30; //Starts at 290

var dx = 2; //Value of the distance to move from x after each frame
var dy = -2; //Value of the distance to move from y after each frame

var ballRadius = 10;

//DEFINE YOUR FUNCTIONS HERE
function drawBall() {
    ctx.beginPath();
    ctx.arc(x, y, ballRadius, 0, Math.PI*2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBall();

    //Add collision detection for right and left of canvas
    if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
        dx = -dx;
    }
    //Add collision detection for bottom and top of canvas
    if(y + dy > canvas.height-ballRadius || y + dy < ballRadius) {
        dy = -dy;
    }  

    //Increment to change location of ball
    x += dx; //This is the same as x = x + dx
    y += dy; //This is the same as y = y + dy

    console.log("x = " + x + ", y = " + y);
}

//How often we clear and redraw the canvas
setInterval(draw, 10);

