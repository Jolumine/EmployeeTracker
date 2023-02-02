from PyQt5.QtWidgets import QApplication

from emptrk.templates.Home import Home

from emptrk.setup import prepare

import sys

def main() -> None:
	app = QApplication(sys.argv)

	prepare()
	home = Home()

	sys.exit(app.exec_())