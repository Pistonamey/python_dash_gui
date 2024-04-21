import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

Rectangle {
    id: center_screen_widget
    width: 600
    height: 340
    color: "black"

    //border.width: 2
    //border.color: "red"
    //radius: 5

    /*Rectangle {
        width: parent.width
        height: 2
        color: "red"

    }*/

    Rectangle {
        width: parent.width - 300
        height: 35
        color: "white"

        gradient: Gradient {
            GradientStop { position: 0.0; color: "red" }
            GradientStop { position: 0.4; color: Qt.rgba(255, 0, 0, .5) }
        }

        border.width: 2
        border.color: "red"

        radius: 5

        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }

        Text {
            text: centerScreen.currTime
            //font.bold: true
            font.pixelSize: 20
            color: "white"

            anchors {
                right: parent.right
                rightMargin: 20
                verticalCenter: parent.verticalCenter
            }

            layer.enabled: true
            layer.effect: DropShadow {
                horizontalOffset: 2
                verticalOffset: 2
                radius: 8
                samples: 64
                color: "black"
            }

        }

        Text {
            text: centerScreen.currDate
            //font.bold: true
            font.pixelSize: 15
            color: "white"

            anchors {
                left: parent.left
                leftMargin: 20
                verticalCenter: parent.verticalCenter
            }

            layer.enabled: true
            layer.effect: DropShadow {
                horizontalOffset: 2
                verticalOffset: 2
                radius: 8
                samples: 64
                color: "black"
            }

        }

    }

/*    Rectangle {
        width: parent
        height: 200
        color: "transparent"

        anchors {
            centerIn: parent
        }

        Text {
            text: "N"
            font.pixelSize: 100
            font.bold: true
            color: "white"

            anchors {
                centerIn: parent
            }

            layer.enabled: true
            layer.effect: DropShadow {
                horizontalOffset: 5
                verticalOffset: 5
                radius: 16
                samples: 64
                color: "#7d0101"
            }
        }
    }*/


}