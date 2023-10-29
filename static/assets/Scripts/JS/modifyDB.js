function updateinfo(clicked_btn) {
    clicked_btn = clicked_btn.split("_")
    let form = document.getElementById(toString(clicked_btn[0])+"_"+toString(clicked_btn[2]));
    let finalcontent = "";
    for(var i=0; i<form.getElementsByTagName("input").length-1;++i) {
        finalcontent += "&"+form.getElementsByTagName("input")[i].id.split('_')[1]+"+"+form.getElementsByTagName("input")[i].id.split('_')[2]+"="+form.getElementsByTagName("input")[i].value;
    }
    let tableToEdit;
    switch(clicked_btn[0]) {
        case 1:
            tableToEdit = "tuteur";
            break;
        case 2:
            tableToEdit = "tutore";
            break;
        case 3:
            tableToEdit = "relation";
            break;
        case 4:
            tableToEdit = "group";
            break;
        case 5:
            tableToEdit = "retour";
            break;
        default:
            alert("ERROR: INVALID HTML ID FORMAT ! ABORT !")
            return;
    }
    finalcontent = "table="+tableToEdit+finalcontent;

    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function() {
        if(xml.status == 200) {
            console.log(xml.response);
        }
    };

    xml.open("POST","/modifyDB");
    xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xml.send(finalcontent);
}