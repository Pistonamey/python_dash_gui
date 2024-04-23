import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

// Transparent Rectangle that holds everything
Rectangle {
    // Size of the widget
    property int widget_width: 325
    property int widget_height: 325

    // Color of the Speedometer
    property string widget_color: "red"
    property string widget_glowColor: "darkred"

    // Color of the Needle
    property string widget_needleColor: "red"


    width: widget_width
    height: widget_height

    color: "transparent"

    // Outer Ring Border
    Rectangle {
        width: widget_width + 15
        height: widget_height + 15
        anchors.centerIn: parent
        radius: 250

        color: "black"
        border.width: 5
        border.color: widget_color

        // Circular Gauge for RPM Meter
        CircularGauge {
            width: widget_width
            height: widget_height

            // Add properties and bindings for RPM values
            value: RPM_Meter.currRPM
            maximumValue: RPM_Meter.maxRPM
            minimumValue: RPM_Meter.minRPM

            anchors {
                centerIn: parent
            }

            style: CircularGaugeStyle {
                tickmarkStepSize: 1.0 // Tick Marks
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
                    color: widget_color
                }

                tickmarkLabel:  Text {
                    font.pixelSize: Math.max(6, outerRadius * 0.1)
                    text: styleData.value
                    color: styleData.value >= 8000 ? widget_color : widget_color
                    antialiasing: true
                }

                needle: Rectangle {
                    y: outerRadius * 0.15
                    implicitWidth: outerRadius * 0.03
                    implicitHeight: outerRadius * 1.1
                    radius: 10
                    antialiasing: true
                    color: widget_needleColor
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

        }

        // Value label for RPM
        Rectangle {
            width: 150
            height: 150
            color: "black"

            anchors.centerIn: parent

            border.width: 2
            border.color: "red"
            radius: 360

            Text {
                text: Math.round(RPM_Meter.currRPM)
                color: "white"
                font.pixelSize: 36
                font.bold: true

                anchors.centerIn: parent
                Text {
                    text: "x1000 rpm"
                    color: "white"
                    font.pixelSize: 12
                    anchors.top: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }


        }

        // Glow Effect
        layer.enabled: true
        layer.effect: Glow {
            radius: 32
            samples: 64
            color: widget_glowColor
        }

    }





}