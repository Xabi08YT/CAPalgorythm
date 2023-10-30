let sendToBackend = function() {
    let form = document.getElementById("mainform");
    let mode = form.getElementsByTagName("select")[1].value;
    let name = form.getElementsByTagName("input")[0].value;
    let surname = form.getElementsByTagName("input")[1].value;
    let group = form.getElementsByTagName("select")[0].value;
    let subjects = [];
    let matiere = false;
    for(var i=2; i<21; ++i) {
        subjects.push(form.getElementsByTagName("input")[i].checked);
        if(form.getElementsByTagName("input")[i].checked===true) {
            matiere = true;
        }
    }

    let freetime = [];
    let creneaux = false;

    for(var i=21; i<44; ++i) {
        freetime.push(form.getElementsByTagName("input")[i].checked)
        if(form.getElementsByTagName("input")[i].checked===true) {
            creneaux = true;
        }
    } 
    

    if(name == null || surname == null || ((matiere===false || creneaux===false) && mode != "Rem")) {
        alert("Des entrées sont manquantes. Opération annulée.")
        return;
    }


    let toSend = "mode="+mode+"&name="+name+"&surname="+surname+"&group="+group+"&subjects="+subjects.toString()+"&freetime"+freetime.toString();

    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function() {
        if(xml.status == 200) {
            console.log(xml.response);
            console.log("Opération effectuée avec succès.")
        }
    };

    xml.open("POST","/");
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send(toSend);
};