function refreshCfg() {
    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function() {
        if(xml.status == 200) {
            console.log(xml.response);
        }
    };

    xml.open("POST","/cfg/refresh");
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send("Refresh");
};

function sendCfg() {
    let form = document.getElementById("settings");
    let enableRel = form.getElementsByTagName("input")[0].checked;
    let enableFeedback = form.getElementsByTagName("input")[1].checked;
    
    let toSend = "enableRel="+enableRel+"&enableFeedback="+enableFeedback;

    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function() {
        if(xml.status == 200) {
            console.log(xml.response);
        }
    };

    xml.open("POST","/cfg/write");
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send(toSend);
};

function resetCfg() {
    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function() {
        if(xml.status == 200) {
            console.log(xml.response);
        }
    };

    xml.open("POST","/cfg/reset");
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send("Reset");
};

function resetDB() {
    if (window.confirm("Souhaitez-vous vraiment effacer les données ? Cette action est irréversible.")) {
        if (window.confirm("Souhaitez-vous vraiment effacer les données ? Cette action est irréversible. (Double vérification)")) {
            const xml = new XMLHttpRequest();

            xml.onreadystatechange = function() {
                if(xml.status == 200) {
                    console.log(xml.response);
                }
            };

            xml.open("POST","/DB/reset");
            xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xml.send("Reset");
            alert("Données effacées avec succès.")
            return;
        };
    };
    alert("Opération annulée.")
};