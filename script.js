document.getElementById("chat-button").addEventListener("click", function() {
    var input = document.getElementById("chat-input").value;

    // Aquí deberías enviar el mensaje al servidor y recibir la respuesta
    if (input.trim() !== "") {
        var chatlogs = document.getElementById("chatlogs");
        chatlogs.innerHTML += '<div class="user-message">' + input + '</div>';
        
        // Simulación de respuesta del chatbot
        setTimeout(() => {
            var botResponse = "Respuesta del bot a tu mensaje: " + intents_spanish.json; // Reemplaza esto con tu lógica de chatbot
            chatlogs.innerHTML += '<div class="bot-message">' + botResponse + '</div>';
            chatlogs.scrollTop = chatlogs.scrollHeight; // Desplazar hacia abajo
        }, 1000);

        document.getElementById("chat-input").value = ''; // Limpiar el campo de entrada
        chatlogs.scrollTop = chatlogs.scrollHeight; // Desplazar hacia abajo
    }
});











    //\\//\\

   //______\\

  //|||||||||\\

 // ||     || \\