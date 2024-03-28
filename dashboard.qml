import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

Rectangle {
    width: 1024
    height: 600
    color: "#000000"

    // Define an enumeration for the car states
    enum CarState {
        Drive,
        Reverse,
        Neutral,
        Parked
    }

    SpeedometerGauge {
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 20
            bottom: parent.bottom
        }
    }



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
            top: parent.top
            verticalCenter: parent.verticalCenter
            right: parent.right
            rightMargin: 20
        }
    }

    Labels {
        id: averageSpeedLabel
        label: "Average Speed"
        currValue: avg_speed.currValue
        unit: "mph"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Labels {
        id: consumptionLabel
        label: "Consumption"
        currValue: consumption.currValue
        unit: "M/L"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: averageSpeedLabel.bottom // Anchor to the bottom of the first label
        anchors.topMargin: 10 // Adjust this margin to control spacing between the labels
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Labels {
        id: driveableLabel
        label: "Driveable"
        currValue: driveable.currValue
        unit: "M/L"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.left: consumptionLabel.right // Position to the right of the consumption label
        anchors.leftMargin: 20 // Add some space between the labels
        anchors.verticalCenter: consumptionLabel.verticalCenter // Align vertically with consumption
    }

    Labels {
        id: odpartialLabel
        label: "Od. Partial"
        currValue: od_partial.currValue
        unit: "m"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.right: consumptionLabel.left // Position to the right of the consumption label
        anchors.rightMargin: 20 // Add some space between the labels
        anchors.verticalCenter: consumptionLabel.verticalCenter // Align vertically with consumption
    }

    BarMeter {
        id: temperatureBar

        mainValue: temperature.currValue
        maxValue: temperature.maxSpeed



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

        mainValue: battery_capacity.currValue
        maxValue: battery_capacity.maxSpeed


        label_name: "Battery Capacity"
        unitValue: "%"

        color: "transparent"    // Only changes the background color with the labels

        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

    }
    

    // Function to get text representation of car state
    function getStateText(state) {
        switch(state) {
            case CarState.Drive: return "Drive";
            case CarState.Reverse: return "Reverse";
            case CarState.Neutral: return "Neutral";
            case CarState.Parked: return "Parked";
        }
    }



}