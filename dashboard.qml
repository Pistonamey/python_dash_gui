import "."
import QtQuick 2
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

    CenterScreenWidget {
        anchors {
            centerIn: parent
        }
    }

    SpeedometerGauge {
        anchors {
            top: parent.top
            right: parent.right
            rightMargin: 32
            bottom: parent.bottom
        }
    }

    RPMGauge {
        anchors {
            top: parent.top
            left: parent.left
            leftMargin: 32
            bottom: parent.bottom
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
        anchors.topMargin: 10
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