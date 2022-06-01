
var initialPrice = document.querySelector("#initial-price");
var stocksQuantity = document.querySelector("#stocks-quantity");
var currentPrice = document.querySelector("#current-price");
var submitBtn = document.querySelector("#submit-btn");
var outputBox = document.querySelector("#output-box");
const outputdiv = document.querySelector(".output");

submitBtn.addEventListener("click", submitHandler);

function submitHandler() {
  var ip = Number(initialPrice.value);
  var qty = Number(stocksQuantity.value);
  var curr = Number(currentPrice.value);

  calculateProfitAndLoss(ip, qty, curr);
}

function calculateProfitAndLoss(initial, quantity, current) {
  if (initial > current) {
    var loss = (initial - current) * quantity;
    var lossPercentage = (loss / initial) * 100;
    showOutput(
      `${loss} RS(${lossPercentage}%) loss `
    );
  } else if (current > initial) {
    var profit = (current - initial) * quantity;
    var profitPercentage = (profit / initial) * 100;
    showOutput(
      `${profit} RS(${profitPercentage}%) profit `
    );
  } else {
    showOutput(`No pain no gain and no gain no pain`);
  }
}

function showOutput(message) {
  outputBox.innerHTML = message;
}
