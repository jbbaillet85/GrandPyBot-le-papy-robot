console.log("teste JS")

var user_question = document.getElementById("user_question");

user_question.addEventListener("change", senddata('GET', 'http://127.0.0.1:5000/','user_question=ou+est+openclassrooms'))


senddata = function (method, url, params) {
    let httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                console.log(httpRequest.responseText);
            } else {
                // il y a eu un problème avec la requête,
                // par exemple la réponse peut être un code 404 (Non trouvée)
                // ou 500 (Erreur interne au serveur)
            }
        } else {
            // pas encore prête
        }
        // instructions de traitement de la réponse
    };
    httpRequest.open(method, url + "?" + params, true);
    httpRequest.setRequestHeader("Content-Type", "application/json");
    httpRequest.send();
}
