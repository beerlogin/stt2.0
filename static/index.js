const socket = io();

socket.on('update', function(data) {
    let listeningMessage;

    // Условная логика для выбора сообщения
    if (data.is_listening == "True") {
        listeningMessage = "Я вас слушаю, сэр";
    } else if (data.is_listening == "False") {
        listeningMessage = "Позовите меня, чтобы я вас слушал";
    } else {
        listeningMessage = "Произошла ошибка, я не понимаю.";
    }

    // Обновление содержимого элемента с id 'status'
    document.getElementById('status').innerHTML = `
        <p>${data.action}</p>
        <p>${listeningMessage}</p>
    `;
});

socket.on('connect', function() {
    console.log("Socket.IO соединение установлено.");
});

socket.on('disconnect', function() {
    console.log("Socket.IO соединение закрыто.");
});
