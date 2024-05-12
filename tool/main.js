const { app, BrowserWindow } = require('electron')
const path = require('node:path')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 1200,
    height: 600
  })

  win.loadFile('index.html')
}

app.on('ready', () => {
  createWindow()

})