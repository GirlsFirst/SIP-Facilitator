/* 
intro-js
Facilitator Code
SIP U3L2 

All of the exercises in the Intro to JavaScript activity
by Girls Who Code
March 2020
*/

// prints "hi" in the browser's dev tools console
console.log("hi");

console.log('Girls Who Code!');


//PART 2: SYNTAX
var myName = 'Liza';
console.log(myName);


//PART 3: DATA TYPES
//String
var favIceCream = 'Ample Hills'
console.log(favIceCream);

//Number
var timesConsumedPerWeek = 2;
console.log(timesConsumedPerWeek);

//Boolean
var eatToday = false;
console.log(eatToday);

//Addition
var val1 = 3;
var val2 = 6;
var valTotal = val1 + val2;
console.log(valTotal);


//PART 4: THE DOM
//Find the element you want to change using getElementById
var headerGreeting = document.getElementById('greeting');

//Manipulate the HTML header element
headerGreeting.innerHTML = 'Oh, hello there!';

//Change CSS using the DOM
headerGreeting.style.color = 'blue';


//PART 5: EVENTS
//Create an event listener
headerGreeting.addEventListener("click", myFunction);

//Add the function 
function myFunction() {
    //Add a debugger
    debugger;
    console.log('you clicked!');
    //Change the color of the header when clicked
    headerGreeting.style.color = 'red';
}

//PART 6: USER INPUT
var submitButton = document.getElementById("submit");
  submitButton.addEventListener("click", nameDisplay);

  function nameDisplay() {
     var nameValue = document.getElementById("name").value;
     var nameContainer = document.getElementById("name-container");
     nameContainer.innerHTML = "I like your name, " + nameValue + "!";
  }