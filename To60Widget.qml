import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

Rectangle {
    width: 300
    height: 300
    color: "black"
    property bool messageTextVisible: false
    property bool isTiming: false
    property double elapsedTime: 0
    property double currentSpeed: 0
    property double targetSpeed: 60

    Timer {
        id: accelerationTimer
        interval: 10  
        repeat: true
        running: isTiming
        onTriggered: {
            console.log("TIMING")
            // Simulate speed increase (e.g., from a car accelerating)
            if (speedometer.currSpeed < targetSpeed && speedometer.currSpeed > 0) {
                elapsedTime += interval / 1000  // Update elapsed time in seconds
                messageText.text = "Timing..."
            } else if (speedometer.currSpeed >= 60){
                isTiming = false
                elapsedTime += 0.2
                messageText.text = `0-60 time: ${elapsedTime.toFixed(2)} seconds`
            }
        }
    }

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
            text: isTiming ? "Timing..." : "Timer Ready"
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
            id: toggleButton
            text: messageTextVisible ? "Cancel" : "0-60 Timer"
            width: 100
            height: 40
            anchors {
                horizontalCenter: parent.horizontalCenter
                bottom: messageText.top
            }
            onClicked: {
                messageTextVisible = !messageTextVisible
                if (isTiming) {
                    isTiming = false
                    accelerationTimer.stop()
                    messageText.text = "Timer Ready"
                } else {
                    isTiming = true
                    elapsedTime = 0
                    accelerationTimer.start()
                    messageText.text = "Timer Set"
                }
            }
        }

    }
}