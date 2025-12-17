function checkquestion(){
    if (document.getElementById("question").value==="correct"){
        document.getElementById("result").innerHTML = "<h2> yes</h2>";
    } else if (document.getElementById("question").value==="incorrect"){
        document.getElementById("result").innerHTML = "<h2> no</h2>";
    } else {
        document.getElementById("result").innerHTML = "<h2> </h2>";
    }
}



document.getElementById("question").addEventListener("change", checkquestion);
