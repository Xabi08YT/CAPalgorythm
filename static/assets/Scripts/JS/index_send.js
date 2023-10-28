let sendToBackend = function() {
    let form = document.getElementById("mainform");
    let mode = form.getElementsByTagName("select")[1].value;
    let name = form.getElementsByTagName("input")[0].value;
    let surname = form.getElementsByTagName("input")[1].value;
    let group = form.getElementsByTagName("select")[0].value;
    let subjects = [];
    
    for(var i=2; i<21; ++i) {
        subjects.push(form.getElementsByTagName("input")[i].checked);
    }

    let freetime = [];

    for(var i=21; i<44; ++i) {
        freetime.push(form.getElementsByTagName("input")[i].checked)
    } 
    
    let toSend = "mode="+mode+"&name="+name+"&surname="+surname+"&group="+group+"&subjects="+subjects.toString()+"&freetime"+freetime.toString();

    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function() {
        if(xml.status == 200) {
            console.log(xml.response);
        }
    };

    xml.open("POST","/");
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send(toSend);
};