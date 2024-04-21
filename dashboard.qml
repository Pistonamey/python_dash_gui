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
        label: "Engine Load"
        currValue: engineLoadLabel.currValue
        unit: "%"
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
        label: "Coolant Temp"
        currValue: coolantTempLabel.currValue
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
        label: "Short Fuel Trim"
        currValue: shortTermFuelTrimLabel.currValue
        unit: "%"
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
        label: "Long Fuel Trim"
        currValue: longTermFuelTrimLabel.currValue
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
        label: "Throttle Pos."
        currValue: throttlePosLabel.currValue
        unit: "m"
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
        label: "Bank Sensor"
        currValue: bankSensorLabel.currValue
        unit: "V"
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
        label: "Dist w/ MIL"
        currValue: distWithMILabel.currValue
        unit: "km"
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
        label: "Dist DTC Clear"
        currValue: distDTCClearLabel.currValue
        unit: "km"
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
        label: "Evap Vapr pres."
        currValue: evapVaporPressureLabel.currValue
        unit: "pascal"
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
        label: "Place Holder"
        currValue: tire_pressures.currValue
        unit: "mph"
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
        maxValue: 100

        label_name: "Fuel"
        unitValue: "%"

        color: "transparent"    // Only changes the background color with the labels

        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

    }

    property bool messageTextVisible: false

    Text {
        id: messageText
        text: "Timer Ready"
        visible: messageTextVisible // Bind visibility to the property
        anchors {
            horizontalCenter: parent.horizontalCenter
            bottom: parent.bottom
            bottomMargin: 100 // Adjust margin as needed (e.g. 20% of screen height)
        }
        font {
            pointSize: 20
            bold: true
        }
        color: "white"
    }

    Button {
        id: greenButton
        text: messageTextVisible ? "Cancel" : "0-60 Timer"
        width: 100 // Adjust the width of the button
        height: 40 // Adjust the height of the button
        anchors {
            horizontalCenter: parent.horizontalCenter
            bottom: messageText.top // Anchor the button to the top of the text
            bottomMargin: 10 // Adjust this value to control the distance between the button and text
        }
        onClicked: {
            // Toggle the visibility of messageText and change button text accordingly
            messageTextVisible = !messageTextVisible
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