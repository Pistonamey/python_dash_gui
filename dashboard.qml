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

    To60Widget {
        anchors {
            horizontalCenter: parent.horizontalCenter
            bottom: parent.bottom
            bottomMargin: 100
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
        id: label1
        label: "Intake Pressure"
        currValue: intakePressureLabel.currValue
        unit: "kPa"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.right: label2.left
        anchors.rightMargin: 10
        anchors.verticalCenter: label2.verticalCenter
    }

    Labels {
        id: label2
        label: "Intake Temp"
        currValue: intakeTempLabel.currValue
        unit: "°C"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.right: label3.left
        anchors.rightMargin: 10
        anchors.verticalCenter: label3.verticalCenter
    }

    Labels {
        id: label3
        label: "Run Time"
        currValue: runtimeLabel.currValue
        unit: "sec"
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
        id: label4
        label: "Fuel Level"
        currValue: fuelLevelLabel.currValue
        unit: "%"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.left: label3.right
        anchors.leftMargin: 10
        anchors.verticalCenter: label3.verticalCenter
    }

    Labels {
        id: label5
        label: "Fuel Type"
        currValue: 1
        unit: fuelTypeLabel.stringValue
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.left: label4.right
        anchors.leftMargin: 10
        anchors.verticalCenter: label4.verticalCenter
    }

    Labels {
        id: label6
        label: "Engine Load"
        currValue: engineLoadLabel.currValue
        unit: "%"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: label1.bottom
        anchors.topMargin: 5
        anchors.horizontalCenter: label1.horizontalCenter
    }

    Labels {
        id: label7
        label: "Throttle Position"
        currValue: throttlePosLabel.currValue
        unit: "%"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: label2.bottom
        anchors.topMargin: 5
        anchors.horizontalCenter: label2.horizontalCenter
    }

    Labels {
        id: label8
        label: "Barometric Pres"
        currValue: barometricPressureLabel.currValue
        unit: "kPa"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: label3.bottom
        anchors.topMargin: 5
        anchors.horizontalCenter: label3.horizontalCenter
    }

    Labels {
        id: label9
        label: "Throttle Accel"
        currValue: throttleAcceleratorLabel.currValue
        unit: "%"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: label4.bottom
        anchors.topMargin: 5
        anchors.horizontalCenter: label4.horizontalCenter
    }

    Labels {
        id: label10
        label: "Absolute Load"
        currValue: absoluteLoadLabel.currValue
        unit: "%"
        fontSize: 18
        color: "white"
        borderColor: "#FF0000" // Example border color
        borderWidth: 2 // Example border width
        borderRadius: 10 // Example border radius for rounded corners
        anchors.top: label5.bottom
        anchors.topMargin: 5
        anchors.horizontalCenter: label5.horizontalCenter
    }

    BarMeter {
        id: temperatureBar

        mainValue: temperature.currValue
        maxValue: 200

        label_name: "Temperature(Coolant)"
        unitValue: "°C"

        color: "transparent"    // Only changes the background color with the labels

        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

    }

    BarMeter {
        id: batteryBar

        mainValue: battery_capacity.currValue
        maxValue: 100

        label_name: "Fuel"
        unitValue: "%"

        color: "transparent"    // Only changes the background color with the labels

        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

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

        MouseArea {
            anchors.fill: parent
                onClicked: {
                console.log("Button clicked")
                // Add any actions you want the button to perform here
                ld.source = "Second_row.qml"
            }
        }

        Loader{
            id: ld
            anchors.centerIn: dashboardGUI
        }
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
