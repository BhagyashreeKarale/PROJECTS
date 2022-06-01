const chalk = require('chalk');
const input=require('readline-sync');
var score=0
var highScores = [
  {
    name: "Sandhya",
    score: 4,
  },

  {
    name: "Aarti",
    score: 3,
  },
]

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
var qa=[{question:"What is the full name of Shinchan?",answer:"Shin Chan Nohara"},{question:"What is the color of Shinchan's dog Shiro",answer:"White"},{question:" What is the vegetable that Shinchan hates to eat?",answer:"Capsicum"},{question:"Who is Shinchan's favourite action hero?",answer:"Action Kamen"},{question:"What is the name of Shinchan's only female friend",answer:"Nene"}]
var username = input.question(chalk.bold.whiteBright("What is your name?\n"))
console.log(`${chalk.bold.whiteBright("Welcome")+" "+chalk.yellowBright(username.toUpperCase()) +"!"+"\n"+
chalk.bold.green("Lets start with the quiz")
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
console.log("Check out the high scores, if you should be there ping me and I'll update it");

highScores.map(score => console.log(score.name, " : ", score.score))

console.log(chalk.bold("**********************Game Over**********************"))
