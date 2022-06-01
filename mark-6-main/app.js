//first we'll get the input , button and the output
var btnTranslate = document.querySelector('#btn-translate');
var txtInput = document.querySelector('#input');
var outputDiv = document.querySelector('#output');

//Now we'll build a URL
var url = "https://api.funtranslations.com/translate/minion.json"

function getTranslationURL(text) {
    return `${url}?text=${text}`
}


//Now we'll define the main function which is the aim of the program
//this function is about what needs to be done when the translate button is clicked
function clickHandler() {
    // outputDiv.innerText = "sjgdukfa" +txtInput.value
    //we don't need return function clickEventHandler() so cut it off
    // return function clickEventHandler() { 
    // console.log('clicked'); 
    // };
    // console.log("input", txtInput.value);

    var text_input = txtInput.value; //here we are collecting the user inputed text

    //calling server for processing
    fetch(getTranslationURL(text_input)) //we are sending requesting
        .then(response => response.json()) //converting it in json format
        .then(json => {
            var output_text = json.contents.translated //this is what we need specifically-only the translated text from the data recieved after sending request
            outputDiv.innerText = output_text
        }) //output the output
        // console.log(json.contents.translated)})
        .catch(err8 => {
            console.log('somethings broken:(') //error
            alert('browser gone mad')
        })
}

btnTranslate.addEventListener('click', clickHandler)

//note we don't need parenthesis along with funciton when we are passing a funciton as an callback function

//we have to define the callback funciton before using it, so move the callback funciton declaration above btnTranslate.addEventListener('click',clickHandler)


// function clickHandler() {
//     //we don't need return function clickEventHandler() so cut it off
//     // return function clickEventHandler() { 
//         console.log('clicked'); 
//     // };
// }