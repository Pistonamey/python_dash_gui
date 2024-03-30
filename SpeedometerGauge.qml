import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

// Transparent Rectangle that holds everything
Rectangle {
    property int widget_width: 325
    property int widget_height: 325

    property string widget_color: "red"

    width: widget_height
    height: widget_height

    color: "transparent"

    // Outer Ring Border
    Rectangle {
        width: widget_width + 15 // Customizable
        height: widget_height + 15 // Customizable
        radius: 250

        color: "black"
        border.width: 5
        border.color: widget_color // Customizable

        anchors.centerIn: parent

        // Circular Gauge for Speedometer
        CircularGauge {
            width: widget_width
            height: widget_height

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
                        color: styleData.value >= 8000 ? widget_color : widget_color
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
                        color: styleData.value >= 8000 ? widget_color : widget_color
                        //font.bold: true
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

        // Inter-Circular Gauge for Speedometer in km
        CircularGauge {
            width: widget_width - 125
            height: widget_height - 125
            //value: speedometer.currSpeed
            maximumValue: 260
            minimumValue: 0
            style: CircularGaugeStyle {
                tickmarkStepSize: 20.0 // Tick Marks
                   tickmark: Rectangle {
                        visible: styleData.value < 8000 || styleData.value % 1000 == 0
                        implicitWidth: outerRadius * 0.02
                        antialiasing: true
                        implicitHeight: outerRadius * 0.06
                        color: "darkred"
                   }

                   minorTickmark: Rectangle {
                        visible: styleData.value < 8000
                        implicitWidth: outerRadius * 0.01
                        antialiasing: true
                        implicitHeight: outerRadius * 0.03
                        color: "darkred"
                   }

                   tickmarkLabel:  Text {
                        font.pixelSize: Math.max(6, outerRadius * 0.1)
                        text: styleData.value
                        color: "darkred"
                        //font.bold: true
                        antialiasing: true
                   }

                   needle: Rectangle {
                        y: outerRadius * 0.15
                        implicitWidth: outerRadius * 0.03
                        implicitHeight: outerRadius * 1.1
                        radius: 20
                        antialiasing: true
                        color: "transparent"
                   }

                   foreground: Item {
                        Rectangle {
                             width: outerRadius * 0.2
                             height: width
                             radius: width / 2
                             color: "transparent"
                             anchors.centerIn: parent
                        }
                   }

            }

            anchors {
                centerIn: parent
            }

        }

        // Value label for Speedometer
        Rectangle {
            width: 100
            height: 50
            color: "transparent"

            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 20

            Text {
                text: Math.round(speedometer.currSpeed)
                color: "white"
                font.pixelSize: 24

                anchors.centerIn: parent
                Text {
                    text: "mph"
                    color: "white"
                    font.pixelSize: 12
                    anchors.top: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }


        }

        // Glow effect
        layer.enabled: true
        layer.effect: Glow {
            radius: 32
            samples: 64
            color: "darkred"
        }


    }





}