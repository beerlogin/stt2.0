const { app, BrowserWindow } = require('electron');

function createWindow () {
    const win = new BrowserWindow({
        width: 500,
        height: 600,
        resizable: false, // Запретить изменение размера окна
        autoHideMenuBar: true, // Скрываем строку меню
        webPreferences: {
            nodeIntegration: true
        }
    });

    // Загружаем URL вашего локального сервера
    win.loadURL('http://localhost:5000');
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});