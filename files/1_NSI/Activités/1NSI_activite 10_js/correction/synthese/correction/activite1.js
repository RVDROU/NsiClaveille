/* ///////////// 1.Boite de dialogue ///////////// */


function boite() {
	x=document.getElementById("texte1");
	let r = prompt("Faites un choix");
	if (r.length <16) {
		x.innerHTML = r;
	} else {
		x.innerHTML = "trop long";
	}
	
}



/* //////////////// 2.Range slider ///////////////// */

function glissiere() {

	let x = document.getElementById("texte2");
	let y = document.getElementById("entree");
	x.innerHTML = y.value;
}



/* /////////// 3.Modifier le style (couleur)  //////// */

function changeCouleur() {
	let x = document.getElementById("texte3");
	x.style.color = "#FFFF00";
	x.style.background = "#0000FF";
}



/* ////////// 4.Modifier le style (taille) ///////// */


function tailleImage(Largeur, hauteur) {
	let x = document.getElementById("image");
	x.style.width = Largeur + "px";
	x.style.height = hauteur + "px";
}


/* //////////////// 5.Nombre entier aléatoire /////////// */


/*  Math.floor(x) retourne le plus grand entier qui est inférieur ou égal à un nombre x   */

function randomNb(max) {
	nb = Math.floor(Math.random() * max);
	return nb;
}

function afficheNb() {
	let x = document.getElementById("texte4");
	x.innerHTML = randomNb(100);
}


/* /////////////////// 6.Couleur de fond /////////////// */

function randomCouleur() {
	let color = "rgb(" + randomNb(256) + "," + randomNb(256) + "," + randomNb(256) + ")";
	return color;
}

function affichage() {
	let x = document.body;
	let y = document.getElementById("texte5");
	let couleur = randomCouleur();
	x.style.background = couleur;
	y.innerHTML = couleur;
}






