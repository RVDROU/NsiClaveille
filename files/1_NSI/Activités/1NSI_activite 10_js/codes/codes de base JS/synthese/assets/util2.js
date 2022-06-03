






/* ------------ GESTION DU MENU NE PAS MODIFIER ------------ */

function recharge() {
  location.reload(true);
}
function openNav() {
  document.getElementById("leMenu").style.width = "100%";
}

function closeNav() {
  document.getElementById("leMenu").style.width = "0%";
}
function montre() {
    document.getElementById('code_hexadecimal').innerHTML = "id='code_hexadecimal'";
    document.getElementById('code_decimal').innerHTML = "id='code_decimal'";
    document.getElementById('valeur_r').innerHTML = "'id=valeur_r'";
    document.getElementById('valeur_g').innerHTML = "id='valeur_g'";
    document.getElementById('valeur_b').innerHTML = "id='valeur_b'";

}
