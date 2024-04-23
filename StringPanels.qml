import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12

Rectangle {

    property string currValue: "Name"
    property string title: "Place holder"

    color: "black"
    border.color: "white"
    border.width: 1
    radius: 15
    Layout.preferredWidth: parent.width / 4 - 5
    Layout.preferredHeight: parent.height / 4 - 5

    Column {
        anchors.fill: parent
        spacing: 8
        Item {
            width: parent.width
            height: childrenRect.height // Adjust the height based on the text item height

            Text {
                text: title
                font.pixelSize: 20
                color: "white"
                anchors.top: parent.top
                anchors.left: parent.left
                anchors.margins: 10
            }
        }

        Text {
            text: currValue
            font.pixelSize: 40
            color: "white"
            anchors.horizontalCenter: parent.horizontalCenter
        }
        Item {
            width: parent.width
            height: childrenRect.height

            Text {
                text: units
                font.pixelSize: 20
                color: "white"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.margins: 10
            }
        }
    }
}