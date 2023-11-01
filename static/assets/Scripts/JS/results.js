function addRel(clicked_btn) {
    clicked_btn = clicked_btn.split("_")
    let form = document.getElementById(clicked_btn[0]+"_"+clicked_btn[2]);
    let tuteurid = form.getElementsByTagName("input")[1].value;
    let tutoreid = form.getElementsByTagName("input")[4].value;
    let subject = form.getElementsByTagName("input")[7].value;
    let time = form.getElementsByTagName("input")[8].value;

    if(!window.confirm("Voulez-vous ajouter cette relation ?")) {
        window.alert("Operation annulee")
        return;
    }

    let saisie;
    do {
        saisie = window.prompt("Entrez le nombre de séances à effectuer. PS: le nombre par défaut correspond à un nombre de séances infini.","32768");
    } while(saisie === null || saisie === "" || saisie === " ");

    let toSend = "tuteurid="+tuteurid+"&tutoreid="+tutoreid+"&subject="+subject+"&time="+time+"&lessons="+saisie;

    xml = new XMLHttpRequest();

    xml.onreadystatechange = function() {
        if(xml.status == 200) {
            console.log(xml.response);
        }
    };

    xml.open("POST","/results");
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send(toSend);
    window.alert("Operation executee avec succes")
}

function moreOnRel(currentid) {
    window.alert("Erreur: pas implémenté.")
}