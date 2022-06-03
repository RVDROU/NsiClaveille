
/////////////////////////////////////////////////////////////

function changement() {
    var r=document.getElementById("slider_red")
    var val_r=r.value
    var valhex_r=pad(parseInt(r.value).toString(16).toUpperCase());
    affichage_rouge()
    var g=document.getElementById("slider_green")
    var val_g=g.value
    var valhex_g= pad(parseInt(g.value).toString(16).toUpperCase())
    affichage_vert()
    var b=document.getElementById("slider_blue")
    var val_b=b.value
    var valhex_b= pad(parseInt(b.value).toString(16).toUpperCase())
    affichage_bleu()
    
    var x=document.getElementById("code_decimal")
    x.innerHTML="rgb(" + val_r + "," + val_g + "," + val_b + ")"
    var y=document.body;
    y.style.background="rgb(" + val_r + "," + val_g + "," + val_b + ")";
    
    var z=document.getElementById("code_hexadecimal")
    z.innerHTML="#"+valhex_r+valhex_g+valhex_b
}



function affichage_rouge() {
    var x=document.getElementById("slider_red")
    var y=document.getElementById("valeur_r")
    var val=x.value
    y.innerHTML=val
}

function affichage_vert() {
    var x=document.getElementById("slider_green")
    var y=document.getElementById("valeur_g")
    var val=x.value
    y.innerHTML=val
}

function affichage_bleu() {
    var x=document.getElementById("slider_blue")
    var y=document.getElementById("valeur_b")
    var val=x.value
    y.innerHTML=val
}
/*Fonction de padding: Affiche par exemple "0F" à la place de "F"*/
function pad(n) {
		   if (n.length < 2) {return '0'+n}
		   else{return n;}
		}

////////////////////////////////////////////////////////////
