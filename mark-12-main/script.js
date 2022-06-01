const angles = document.querySelectorAll('.angle-input');
const sides = document.querySelectorAll('.side-input');
const isTriangleBtnA = document.querySelector('#is-triangle-btn-angles');
const isTriangleBtnS = document.querySelector('#is-triangle-btn-sides');
const isTriangleOutputA = document.querySelector('#is-triangle-output-angles');
const isTriangleOutputS = document.querySelector('#is-triangle-output-sides');


function calculateSumOfAngles() {
	const sumOfAngles =
		Number(angles[0].value) + Number(angles[1].value) + Number(angles[2].value);
	console.log(sumOfAngles);
	return sumOfAngles;
}

function isTriangleA() {
	if (calculateSumOfAngles() === 180) {
		console.log('Yayy, the angles form a triangle');
		isTriangleOutputA.innerText = 'Yayy, the angles form a triangle';
	} else {
		console.log('Oh Oh!, the angles do not form a triangle');
		isTriangleOutputA.innerText = 'Oh Oh!, the angles do not form a triangle';
	}
}
isTriangleBtnA.addEventListener('click', isTriangleA);


//Triangle inequality Theorem
function isTriangleS() {
    let A = Number(sides[0].value),B=Number(sides[1].value),C=Number(sides[2].value);
    if (A+B>C && B+C>A && C+A>B){
        console.log('Yayy, the sides form a triangle');
		isTriangleOutputS.innerText = 'Yayy, the sides form a triangle';
    }else {
		console.log('Oh Oh!, the sides do not form a triangle');
		isTriangleOutputS.innerText = 'Oh Oh!, the sides do not form a triangle';
	}

}
isTriangleBtnS.addEventListener('click', isTriangleS);
