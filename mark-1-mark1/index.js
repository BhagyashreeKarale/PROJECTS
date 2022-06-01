// console.log("Bhagyashree Vitthal Karale")


// const input = require('readline-sync')
// var userName = input.question("Enter your name :\n")
// console.log(userName)


// const input = require('readline-sync')
// var userName = input.question("Enter your name :\n")
// console.log("Welcome " + userName)


// const input = require('readline-sync')
// var userName = input.question("Enter your name :\n")
// console.log(`Welcome ${userName} !`)

// const input = require('readline-sync')
// var userAge = input.questionInt("What is your age? \n")
// if (userAge>25){
//   console.log("You are older than 25")
//   console.log("Right")
// }else{
//   console.log("You aren't older than 25")
//   console.log("Wrong")
// }


// var score=0
// const input = require('readline-sync')
// var userAge = input.questionInt("What is your age? \n")
// if (userAge>25){
//   score+=1
//   console.log("Right! You are older than 25")
//   console.log(`Score is ${score}`)
// }else{
//   score-=1
//   console.log("Wrong! You aren't older than 25")
//   console.log(`Score is ${score}`)
// }


// var score=0
// const input = require('readline-sync')
// var userTown = input.question("Is Bokaro your hometown? (yes/no)\n")
// if (userTown=="yes"){
//   score+=1
//   console.log(`Your score is ${score}`)
// }else{
//   score-=1
//   console.log(`Your score is ${score}`)
// }


// function functionName(num1, num2) {
//   let sum = num1+num2
//   return sum;
// }


// function quesAns(ques,ans){
//   let input=require("readline-sync")
//   var q=input.question(ques)
//   if (q==ans){
//     console.log("You are right!")
//   }else{
//     console.log("Incorrect answer")
//   }
// }

////////////////////////////////////////////////////////////////////////////

// for(var i = 1 ; i<=5 ; i++){
//   console.log(`${i}Bhagyashree`)
// }

/////////////////////////////////////////////////////////////////////////////

// const input=require("readline-sync")
// var row=input.questionInt("Enter number of rows")
// for(var i=0;i<row;i++){
//   var str=""
//   for (var j = 0 ; j<i+1 ; j++){
//     str+="*"
//   }console.log(str)
// }

/////////////////////////////////////////////////////////////////////////////

// const input=require("readline-sync")
// var row=input.questionInt("Enter number of rows")
// for(var i=row;i>0;i--){
//   var str=""
//   for (var j = 0 ; j<i ; j++){
//     str+="*"
//   }console.log(str)
// }

/////////////////////////////////////////////////////////////////////////////

// const input=require('readline-sync')
// let list =[]
// console.log("Enter 5 grocery list items")
// for (var i=1;i<=5;i++){
//   let item=input.question(`Enter item ${i}:`)
//   list.push(item)
// }
// console.log(`${list[0]} is the first item on the list.`)
// console.log(`${list[2]} is the third item on the list.`)
// console.log(`${list[list.length-1]} is the last item on the list.`)

/////////////////////////////////////////////////////////////////////////////

// const input=require('readline-sync')
// let list =[]
// console.log("Enter 5 grocery list items")
// for (var i=1;i<=5;i++){
//   let item=input.question(`Enter item ${i}:`)
//   list.push(item)
// }

/////////////////////////////////////////////////////////////////////////////

// var list=["apple","strawberry","grapes","mango","kiwi"]
// for(item of list){
//   console.log(item)
// }

/////////////////////////////////////////////////////////////////////////////

// var batman={
//   name:"Batman",
//   power:"Genius-level intellect",
//   costumeColor:"Black",
//   health:"good",
//   power:10000
// }

// var superman={
//   name:"Superman",
//   power:"Super power",
//   costumeColor:"Blue",
//   health:"good",
//   power:20000
// }

// let superheroes = [batman,superman]
// for (hero of superheroes){
//   console.log(hero.name)
//   console.log(hero.costumeColor)
//   console.log("________________________________")
// }

const chalk = require('chalk');
const input=require('readline-sync');
var score=0
function play(ques,ans){
  var userAns=input.question(ques+"\n")
  if (userAns.toLowerCase()==ans.toLowerCase()){
    score++
    console.log(chalk.greenBright("Correct"))
  }else{
    console.log(chalk.red("Incorrect"))
  }
  console.log(chalk.blue.bold(`Current score : ${score}`))
  console.log(`_____________________________________________________
  `)

}
var qa=[{question:"What is my nickname?",answer:"manya"},{question:"what is my birthdate?",answer:"17"},{question:"where do i live?",answer:"Pune"},{question:"whhich is my favourite pet?",answer:"dog"},{question:"My favourite cartoon?",answer:"Shinchan"}]
var username = input.question(chalk.bold.whiteBright("What is your name?\n"))
console.log(`${chalk.bold.whiteBright("Welcome")+" "+chalk.yellowBright(username.toUpperCase()) +"!"+"\n"+
chalk.bold.green("Lets see how well you know me!")
}`)
var sr = 1
for (i of qa){
  play(`Q.${sr+". "+chalk.bold(i.question.toUpperCase())}`,i.answer)
  sr++
}
if (score==qa.length){
  console.log(chalk.greenBright.bold("Yay!You won."))
}else{
  if (qa.length-score==1){
    console.log(`You lost by ${qa.length-score} point
Better luck next time`)
  }else{
    console.log(`You lost by ${qa.length-score} points
Better luck next time`)}
}
console.log(chalk.bold("**********************Game Over**********************"))
