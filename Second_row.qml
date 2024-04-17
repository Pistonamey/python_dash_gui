import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12

Rectangle { // This is the main background

    MouseArea {
        anchors.fill: parent
            onClicked: {
            console.log("Button clicked")
            // Add any actions you want the button to perform here
            ld.source = ""
        }
    }

    width: 420
    height: 280 // Adjusted to accommodate 2x2 grid
    color: "black"

    property double boost: Math.random() * 40 - 20 // Random number between -20 and 20
        property double afr: 10 + Math.random() * 10 // Random number between 10 and 20

            GridLayout {
                columns: 2
                rows: 3
                anchors.fill: parent
                rowSpacing: 5
                columnSpacing: 2

                // Box for Boost
                Rectangle {
                    color: "black"
                    border.color: "white"
                    border.width: 1
                    radius: 15
                    Layout.preferredWidth: parent.width / 2 - 5
                    Layout.preferredHeight: parent.height / 2 - 5

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

                    // Content for Boost...
                }

                // Box for AF Sens 1 Ratio
                Rectangle {
                    color: "black"
                    border.color: "white"
                    border.width: 1
                    radius: 15
                    Layout.preferredWidth: parent.width / 2 - 5
                    Layout.preferredHeight: parent.height / 2 - 5

                    // Content for AF Sens 1 Ratio...
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

                // Placeholder for a third box (customize as needed)
                Rectangle {
                    color: "black"
                    border.color: "white"
                    border.width: 1
                    radius: 15
                    Layout.preferredWidth: parent.width / 2 - 5
                    Layout.preferredHeight: parent.height / 2 - 5

                    // Content for third box...
                    Column {
                        anchors.fill: parent
                        spacing: 8
                        Item {
                            width: parent.width
                            height: childrenRect.height // Adjust the height based on the text item height

                            Text {
                                text: "Battery Level"
                                font.pixelSize: 20
                                color: "white"
                                anchors.top: parent.top
                                anchors.left: parent.left
                                anchors.margins: 10
                            }
                        }

                        Text {
                            text: "85%"
                            font.pixelSize: 40
                            color: "white"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }

                        Text {
                            text: "250 mi"
                            font.pixelSize: 20
                            color: "white"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        Item {
                            width: parent.width
                            height: childrenRect.height

                            Text {
                                text: "Est. Range"
                                font.pixelSize: 20
                                color: "white"
                                anchors.bottom: parent.bottom
                                anchors.right: parent.right
                                anchors.margins: 10
                            }
                        }
                    }
                }

                // Placeholder for a fourth box (customize as needed)
                Rectangle {
                    color: "black"
                    border.color: "white"
                    border.width: 1
                    radius: 15
                    Layout.preferredWidth: parent.width / 2 - 5
                    Layout.preferredHeight: parent.height / 2 - 5

                    // Content for fourth box...
                    Column {
                        anchors.fill: parent
                        spacing: 8
                        Item {
                            width: parent.width
                            height: childrenRect.height // Adjust the height based on the text item height

                            Text {
                                text: "Energy use"
                                font.pixelSize: 20
                                color: "white"
                                anchors.top: parent.top
                                anchors.left: parent.left
                                anchors.margins: 10
                            }
                        }

                        Text {
                            text: "24 kWh"
                            font.pixelSize: 40
                            color: "white"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }

                        Text {
                            text: "26 kWh/100mi"
                            font.pixelSize: 20
                            color: "white"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        Item {
                            width: parent.width
                            height: childrenRect.height

                            Text {
                                text: "Trip Avg."
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