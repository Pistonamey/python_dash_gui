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

    /*Left_arrow {
        x: 50
        y: 50
        anchors {
            top: parent.top
        }
    }*/

    CenterScreenWidget {
        anchors {
            centerIn: parent
        }
    }

    Button {
        id: switchButton
        property string color: "black" // Text color
        Rectangle {
            property string color: "red" // Button background color
            border.color: "white" // Button border color
            border.width: 2 // Button border width
            radius: 10 // Rounded corners
        }
        width: 40 // Adjust the width of the button
        height: 40 // Adjust the height of the button
        
        onClicked: {
            console.log("Button clicked")
            // Add any actions you want the button to perform here
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
        anchors.topMargin: 30
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
        anchors.left: averageSpeedLabel.right // Anchor to the bottom of the first label
        anchors.leftMargin: 10 // Adjust this margin to control spacing between the labels
        anchors.verticalCenter: averageSpeedLabel.verticalCenter
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
        anchors.leftMargin: 10 // Add some space between the labels
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
        anchors.right: averageSpeedLabel.left // Position to the right of the consumption label
        anchors.rightMargin: 10 // Add some space between the labels
        anchors.verticalCenter: consumptionLabel.verticalCenter // Align vertically with consumption
    }

    Labels {
        id: place_holder
        label: "Miles Driven"
        currValue: 0
        unit: "m"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.right: odpartialLabel.left // Position to the right of the consumption label
        anchors.rightMargin: 10 // Add some space between the labels
        anchors.verticalCenter: odpartialLabel.verticalCenter // Align vertically with consumption
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

        label_name: "Fuel"
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