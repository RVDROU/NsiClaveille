/* ///////////// 1.Boite de dialogue ///////////// */


function boite() {
	var x = document.getElementById("texte1");
	var texte = prompt("Saississez votre texte");
	/* à compléter */
	
}

/* //////////////// 2.Range slider ///////////////// */

function glissiere() {
    let x = document.getElementById("texte2");
    let y = document.getElementById("entree");
    x.innerHTML=y.value;
    document.body.style.background="rgb(" + y.value + "," + 0 + "," + 0 + ")";











}



function affichage() {
	var x = document.body;
	var y = document.getElementById("texte5");
    document.body.style.background="rgb(" + y.value + "," + 0 + "," + 0 + ")";
}






