import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0

Rectangle {
     width: 1024
     height: 600
     color: "#000000"

    Text {
        text: Math.floor(speedometer.currSpeed) // Display the current value
        font.pixelSize: outerRadius * 0.15 // Adjust the font size as needed
        color: "white" // Choose the color of the text
        anchors.horizontalCenter: parent.horizontalCenter // Center horizontally
        y: 225 // Adjust the vertical position
    }



     CircularGauge {
          //property real gauge_value: 40.0
          anchors.centerIn: parent
          value: speedometer.currSpeed
          maximumValue: speedometer.maxSpeed  // Largest Value
          minimumValue: speedometer.minSpeed       // Smallest Value
          style: CircularGaugeStyle {
               id: style
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
     }

    Labels {
        id: averageSpeedLabel
        label: "Average Speed: 30 mph"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 3 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Labels {
        id: consumption
        label: "Consumption: 0 M/L"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 3 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: averageSpeedLabel.bottom // Anchor to the bottom of the first label
        anchors.topMargin: 10 // Adjust this margin to control spacing between the labels
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Labels {
        id: driveable
        label: "Driveable: 0 M/L"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 3 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.left: consumption.right // Position to the right of the consumption label
        anchors.leftMargin: 20 // Add some space between the labels
        anchors.verticalCenter: consumption.verticalCenter // Align vertically with consumption
    }

    Labels {
        id: odpartial
        label: "Od. Partial: 0 m"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 3 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.right: consumption.left // Position to the right of the consumption label
        anchors.rightMargin: 20 // Add some space between the labels
        anchors.verticalCenter: consumption.verticalCenter // Align vertically with consumption
    }

    BarMeter {
        id: temperatureBar

        mainValue: temperature_meter.mainValue
        maxValue: temperature_meter.maxSpeed

        label_name: "Temperature"
        unitValue: "°F"

        color: "transparent"    // Only changes the background color with the labels

        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

    }

    BarMeter {
        id: batteryBar

        mainValue: battery_capacity.mainValue
        maxValue: battery_capacity.maxSpeed


        label_name: "Battery Capacity"
        unitValue: "%"

        color: "transparent"    // Only changes the background color with the labels

        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

    }
    

}