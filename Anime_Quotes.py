from UI import *
import requests

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


def quote1():
    url = "https://animechan.vercel.app/api/random"
    params = {"key": "value"}
    response = requests.get(url, params = params).json()
    global anime
    global character
    global quote
    anime = response["anime"]
    character = response["character"]
    quote = response["quote"]
    ui.character.setText(QCoreApplication.translate("MainWindow", character, None))
    ui.anime.setText(QCoreApplication.translate("MainWindow", anime, None))
    ui.quote.setText(QCoreApplication.translate("MainWindow", quote, None))

quote1()

ui.button.clicked.connect(quote1)
MainWindow.show()
sys.exit(app.exec_())
