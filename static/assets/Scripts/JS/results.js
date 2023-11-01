function addRel(clicked_btn) {
    clicked_btn = clicked_btn.split("_")
    let form = document.getElementById(clicked_btn[0]+"_"+clicked_btn[2]);
    let values = [];
    for(var i=1; i<form.getElementsByTagName("input").length;++i) {
        values.push(form.getElementsByTagName("input")[i].value);
    }

    if(!window.confirm("Voulez-vous ajouter cette relation ?")) {
        window.alert("Operation annulee")
        return;
    }

    let toSend = "Add&"+values.toString();

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