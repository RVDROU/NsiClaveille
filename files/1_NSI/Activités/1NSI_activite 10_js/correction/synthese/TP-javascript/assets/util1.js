







/* ////////GESTION DU MENU ----- NE PAS MODIFIER */
function recharge() {
  location.reload(true);
}
function ecran() {
  document.body.style.transition='background-color 1.5s ease-in-out';
}


function openNav() {
  document.getElementById("leMenu").style.width = "100%";
}

function closeNav() {
  document.getElementById("leMenu").style.width = "0%";
}
function montre() {
	
    document.getElementById('texte1').innerHTML = "id='texte1'";
    document.getElementById('texte2').innerHTML = "id='texte2'";
	document.getElementById('texte3').innerHTML = "id='texte3'";
	document.getElementById('texte4').innerHTML = "id='texte4'";
	document.getElementById('texte5').innerHTML = "id='texte5'";
}