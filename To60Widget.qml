import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

Rectangle {
    width: 300
    height: 340
    color: "black"
    property bool messageTextVisible: false

    Rectangle {
        width: parent.width - 300
        height: 80
        color: "white"

        gradient: Gradient {
            GradientStop { position: 0.0; color: "red" }
            GradientStop { position: 0.4; color: Qt.rgba(255, 0, 0, .5) }
        }

        border.width: 2
        border.color: "red"

        radius: 5

        anchors {
            bottom: parent.bottom
            horizontalCenter: parent.horizontalCenter
        }

        

        Text {
            id: messageText
            text: to60widget.messageText
            visible: messageTextVisible // Bind visibility to the property
            anchors {
                horizontalCenter: parent.horizontalCenter
                bottom: parent.bottom
            }
            font {
                pointSize: 20
                bold: true
            }
            color: "white"
        }

        Button {
            id: greenButton
            text: to60widget.messageTextVisible ? "Cancel" : "0-60 Timer"
            width: 100 // Adjust the width of the button
            height: 40 // Adjust the height of the button
            anchors {
                horizontalCenter: parent.horizontalCenter
                bottom: messageText.top // Anchor the button to the top of the text
            }
            onClicked: {
                // Toggle the visibility of messageText and change button text accordingly
                if (!messageTextVisible) {
                    to60timer.time()
                }
                messageTextVisible = !messageTextVisible
            }
        }

    }
}