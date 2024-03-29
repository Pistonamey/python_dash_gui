import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12

Rectangle { // This is the main background
    width: 420
    height: 140
    color: "black"

    property double boost: Math.random() * 40 - 20 // Random number between -20 and 20
    property double afr: 10 + Math.random() * 10 // Random number between 10 and 20

    GridLayout {
        columns: 2
        anchors.fill: parent
        rowSpacing: 5
        columnSpacing: 2

        // Box for Boost
        Rectangle {
            color: "black"
            border.color: "white"
            border.width: 1
            radius: 15
            Layout.preferredWidth: parent.width / 2 - 5 // Take half the parent width minus spacing
            Layout.preferredHeight: parent.height

            Column {
                anchors.fill: parent
                spacing: 8

                Item {
                    width: parent.width
                    height: childrenRect.height // Adjust the height based on the text item height

                    Text {
                    text: "Boost"
                    font.pixelSize: 20
                    color: "white"
                    anchors.top: parent.top
                    anchors.left: parent.left
                    anchors.margins: 10
                }
                }

                    Text {
                        text: boost.toFixed(2) + " PSI"
                        font.pixelSize: 40
                        color: "white"
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    Text {
                        text: (boost - Math.random()).toFixed(2) + "/" + (boost + Math.random()).toFixed(2) 
                        font.pixelSize: 20
                        color: "white"
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    Item {
            width: parent.width
            height: childrenRect.height

            Text {
                text: "PSI"
                font.pixelSize: 20
                color: "white"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.margins: 10
            }
        }
                }

        }

        // Box for AF Sens 1 Ratio
        Rectangle {
            color: "black"
            border.color: "white"
            border.width: 1
            radius: 15
            Layout.preferredWidth: parent.width / 2 - 5 // Take half the parent width minus spacing
            Layout.preferredHeight: parent.height

            Column {
                anchors.fill: parent
                spacing: 8
                    Item {
                    width: parent.width
                    height: childrenRect.height // Adjust the height based on the text item height

                Text {
                    text: "AF Sens 1 Ratio"
                    font.pixelSize: 20
                    color: "white"
                    anchors.top: parent.top
                    anchors.left: parent.left
                    anchors.margins: 10
                }
                    }

                Text {
                    text: afr.toFixed(2)
                    font.pixelSize: 40
                    color: "white"
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Text {
                    text: (afr - Math.random()).toFixed(2) + "/" + (afr + Math.random()).toFixed(2) + " AFR"
                    font.pixelSize: 20
                    color: "white"
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                Item {
            width: parent.width
            height: childrenRect.height

            Text {
                text: "AFR"
                font.pixelSize: 20
                color: "white"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.margins: 10
            }
        }
            }
        }
    }
}
