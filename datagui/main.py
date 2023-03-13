"""
Copyright (C) 2018 IAIK TU Graz (data@iaik.tugraz.at)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

@version 1.2

"""

import argparse
import sys
from PyQt5.QtWidgets import QApplication
from datagui.package.ui.MainWindow import MainWindow


parser = argparse.ArgumentParser(prog="DATAgui", description="GUI for the DATA results")
parser.add_argument(
    "pickle_path",
    default="",
    type=str,
    help="Default DATA naming: result_phaseX.pickle",
)
parser.add_argument(
    "zip_path", default="", type=str, help="Default DATA naming: framework.zip"
)
args = parser.parse_args()


def main():
    app = QApplication(sys.argv)
    MainWindow(args.pickle_path, args.zip_path)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
