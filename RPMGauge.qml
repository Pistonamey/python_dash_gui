import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

Rectangle {
    id: speedometer_gauge
    width: 325
    height: 325
    color: "transparent"


    Rectangle {
        width: 340
        height: 340
        anchors.centerIn: parent
        radius: 250

        color: "black"
        border.width: 5
        border.color: "red"

        // Circular Gauge for RPM Meter
        CircularGauge {
            width: 325
            height: 325
            // Add properties and bindings for RPM values
            value: RPM_Meter.currRPM
            maximumValue: RPM_Meter.maxRPM
            minimumValue: RPM_Meter.minRPM
            style: CircularGaugeStyle {
                tickmarkStepSize: 1.0 // Tick Marks
                   tickmark: Rectangle {
                        visible: styleData.value < 8000 || styleData.value % 1000 == 0
                        implicitWidth: outerRadius * 0.02
                        antialiasing: true
                        implicitHeight: outerRadius * 0.06
                        color: styleData.value >= 8000 ? "#ff0000" : "#ff0000"
                   }

                   minorTickmark: Rectangle {
                        visible: styleData.value < 8000
                        implicitWidth: outerRadius * 0.01
                        antialiasing: true
                        implicitHeight: outerRadius * 0.03
                        color: "#ff0000"
                   }

                   tickmarkLabel:  Text {
                        font.pixelSize: Math.max(6, outerRadius * 0.1)
                        text: styleData.value
                        color: styleData.value >= 8000 ? "#ff0000" : "#ff0000"
                        antialiasing: true
                   }

                   needle: Rectangle {
                        y: outerRadius * 0.15
                        implicitWidth: outerRadius * 0.03
                        implicitHeight: outerRadius * 1.1
                        radius: 10
                        antialiasing: true
                        color: "#ff0000"
                   }

                   foreground: Item {
                        Rectangle {
                             width: outerRadius * 0.2
                             height: width
                             radius: width / 2
                             color: "white"
                             anchors.centerIn: parent
                        }
                   }
            }
            anchors {
                centerIn: parent
            }
        }

        Rectangle {
            width: 100
            height: 50
            color: "transparent"

            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 20

            Text {
                text: Math.round(RPM_Meter.currRPM)
                color: "white"
                font.pixelSize: 24

                anchors.centerIn: parent
                Text {
                    text: "rpm"
                    color: "white"
                    font.pixelSize: 12
                    anchors.top: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }


        }

        layer.enabled: true
        layer.effect: Glow {
            radius: 32
            samples: 64
            color: "darkred"
        }

    }





}