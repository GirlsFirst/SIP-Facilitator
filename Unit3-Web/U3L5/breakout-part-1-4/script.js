/* 
breakout-part-1
Facilitator Code
SIP U3L5 

Sample code for Breakout Part 1
by Girls Who Code
March 2020

NOTE: This reflects the code at the end of LESSON 5, PART 4

This project is adapted from the 2D breakout game using pure JavaScript
https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript 
created for Mozilla by the amazing MDN contributors.

*/


//Tell the DOM to find the canvas
var canvas = document.getElementById("myCanvas"); 

//Create the 2D drawing object
var ctx = canvas.getContext("2d");

var x = canvas.width/8; //Starts at 60
var y = canvas.height-30; //Starts at 290

var dx = 2; //Value of the distance to move from x after each frame
var dy = -2; //Value of the distance to move from y after each frame

var ballRadius = 10;

var paddleHeight = 10;
var paddleWidth = 75;
var paddleX = (canvas.width-paddleWidth) / 2;

//Booleans that store key presses for the paddle
var rightPressed = false;
var leftPressed = false;


function drawBall() {
    ctx.beginPath();
    ctx.arc(x, y, ballRadius, 0, Math.PI*2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function drawPaddle() {
    ctx.beginPath();
    ctx.rect(paddleX, canvas.height-paddleHeight, paddleWidth, paddleHeight);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBall();
    drawPaddle();

    //Add collision detection for right and left of canvas and reverse ball direction
    if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
        dx = -dx;
    }

    //Add collision detection for top of canvas and reverse the ball direction
    if(y + dy < ballRadius) {
    dy = -dy;
    //Add collision detection for top of canvas to end the game
    } else if(y + dy > canvas.height-ballRadius) { 
    //Add your if statement here to test if the ball and paddle have intersected
        if(x > paddleX && x < paddleX + paddleWidth) {
        dy = -dy;
        }
        else {
         alert("GAME OVER");
         document.location.reload();
         clearInterval(interval);
        }
    }


    //Increment to change location of ball
    x += dx; //This is the same as x = x + dx
    y += dy; //This is the same as y = y + dy

    console.log("x = " + x + ", y = " + y);

    if(rightPressed) {
        paddleX += 7;
        if (paddleX + paddleWidth > canvas.width){
            paddleX = canvas.width - paddleWidth;
        }
    }
    else if(leftPressed) {
        paddleX -= 7;
        if (paddleX < 0){
            paddleX = 0;
        }
    }
}

//Event listeners for keys that control the paddle
document.addEventListener("keydown", keyDownHandler);
document.addEventListener("keyup", keyUpHandler);

//Function for the keydown event listener
function keyDownHandler(e) {
    if(e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = true;
    }
    else if(e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = true;
    }
}
//Function for the keyup event listener
function keyUpHandler(e) {
    if(e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = false;
    }
    else if(e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = false;
    }
}

//How often we clear and redraw the canvas
var interval = setInterval(draw,10)
//setInterval(draw, 10);
