console.log("teste JS")

var user_question = document.getElementById("user_question");

user_question.addEventListener("change", new XMLHttpRequest())

var httpRequest = new XMLHttpRequest();

httpRequest.onreadystatechange = function() 
    {
    if (httpRequest.readyState === XMLHttpRequest.DONE)
        {
        if (httpRequest.status === 200) {console.log(httpRequest.response)}
        else {console.log("page non trouvé ou serveur indisponible")}
        }
    else {console.log("pas prêt")}
    };

httpRequest.open('GET', 'https://my-json-server.typicode.com/typicode/demo/posts', true);
httpRequest.send();
