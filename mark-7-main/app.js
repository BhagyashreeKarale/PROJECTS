var btn=document.querySelector("#translatebtn");
var input=document.querySelector("#input-ctn");
var output=document.querySelector("#output-ctn");

var serverURL = "https://api.funtranslations.com/translate/yoda.json"

function errorHandler(error) {
    console.log("something's wrong?", error);
    alert("Can't connect to groot :(")
}

function convertText(){
    var ipText=input.value;
    if(ipText==""){
        alert("Please enter some text");
        return;
    }

    const url=`${serverURL}?text=${ipText}`;
    fetch(url)
        .then(res => res.json())
        .then(json => {
            var outputText = json.contents.translated;
            output.innerText = outputText;
           })
        .catch(errorHandler)
}

btn.addEventListener('click',convertText);


