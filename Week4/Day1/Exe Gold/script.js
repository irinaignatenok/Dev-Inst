let i = 0;

function playTheGame(){
  let rand = 0;
  if (confirm("Are you sure that you want to play a game?")){
    let x = prompt("enter a number between 1 and 10");
    if (isNaN(x)){
      alert("Sorry Not a number, Goodbye");
    }
    else{
      x = Number(x);
      if (x < 0 || x>10){
          alert("Sorry it's not a good number,Goodbye");
      }
      else{
        rand = Math.round((Math.random()*10));
        test(rand,x)
        }
    }
  }
  else alert("No problem, Goodbye");
}
function test(compNumber, myNumber){
  if (i==3){
    alert ("you can't try again, the numbe was: "+ compNumber);
  }
  else if (myNumber == compNumber){
    alert("you have won!");
    i=0;
    return;
  }
    else if(myNumber != compNumber ){
      alert("your number is bigger, guess again");
      i++;
    }
}
