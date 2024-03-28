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
        width: 330
        height: 330
        anchors.centerIn: parent
        radius: 250

        color: "transparent"
        border.width: 2
        border.color: "red"

        // Circular Gauge for Speedometer
        CircularGauge {
            width: 325
            height: 325
            value: speedometer.currSpeed
            maximumValue: speedometer.maxSpeed
            minimumValue: speedometer.minSpeed
            style: CircularGaugeStyle {
                tickmarkStepSize: 10.0 // Tick Marks
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
                        antialiasing: true
                        color: "#ff0000"
                   }

                   foreground: Item {
                        Rectangle {
                             width: outerRadius * 0.2
                             height: width
                             radius: width / 2
                             color: "#b2b2b2"
                             anchors.centerIn: parent
                        }
                   }
            }

            anchors {
                centerIn: parent
            }

        }
    }





}