function openTicket() {
    let form = document.getElementById("github");
    if(window.confirm("Voulez vous vraiment ouvrir un ticket ? Les développeurs seront averti et des informations sur l'exécution telles que les composant de la machine, le répertoire d'exécution ou les logs seront alors rendus publics.")) {
        let title = form.getElementsByTagName("input")[0].value;
        let body = form.getElementsByTagName("textarea")[0].value;
        let labels = [];
        for(var i=1; i<form.getElementsByTagName("input").length-1;++i) {
            labels.push(form.getElementsByTagName("input")[i].value);
        }
        let toSend = "title="+title+"&body="+body+"&labels="+labels.toString();

        let xml = new XMLHttpRequest();
        xml.onreadystatechange = function() {
            if(xml.status == 200) {
                console.log(xml.response);
            }
        };
    
        xml.open("POST","/ticket");
        xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        xml.send(toSend);
    }
}