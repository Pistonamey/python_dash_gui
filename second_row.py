from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

if __name__ == '__main__':
    import sys

    # Create an instance of the application
    app = QApplication(sys.argv)

    # Create a QML viewer
    view = QQuickView()

    # Set the path to the QML file
    # Ensure this is the correct path to your QML file
    qml_file_path = 'dashboard.qml'

    # Set the QML file as the source for the viewer
    view.setSource(QUrl.fromLocalFile(qml_file_path))

    # Show the view
    view.show()

    # Exit the application when the view is closed
    sys.exit(app.exec_())
