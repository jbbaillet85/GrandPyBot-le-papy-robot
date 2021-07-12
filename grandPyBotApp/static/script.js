document.getElementById("user_question").addEventListener("submit", function(e){
    e.preventDefault();

    var data = new FormData(document)
    console.log(data)

    var httpRequest = new XMLHttpRequest();

    httpRequest.onreadystatechange = function() {
        console.log(httpRequest)
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {console.log(httpRequest.response);}
            else{alert("Une erreure est surevenus")}

    httpRequest.open('POST', "../view.py", true);
    //httpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    httpRequest.send(data);
    return false}}});