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

     // Define an enumeration for the car states
    enum CarState {
        Drive,
        Reverse,
        Neutral,
        Parked
    }

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
            top: parent.top
            verticalCenter: parent.verticalCenter
            left: parent.left
            leftMargin: 20
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


    // Main Bar: Border housing the whole bar containing the value
    Rectangle {
        // Customize the text labels how ever you like here:
        property double mainValue: 100.0                // Current Value. Anything will do.
        property double maxValue: 300.0                 // Max value possible ex: max mph
        property double minValue: 0.0                   // Min value possible ex: mph=0
        property string unitValue: "°F"                // Units for the value ex: mph, mi

        id: mainBar
        width: 400          // Width of the entire bar meter
        height: 20          // Height of the entire bar meter

        radius: 15          // Radius of the entire bar meter. Does affect inner bars.
        color: "black"      // Border Colors


        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

        clip: true

        // Empty Bar: Housing the value bar
        Rectangle {
            id: emptyBar
            width: parent.width - 6
            height: parent.height - 6
            radius: parent.radius

            anchors.centerIn: parent
            anchors.bottom: parent.bottom

            // Value Bar: Displaying the current value
            Rectangle {

                id: valueBar
                width: parent.width * (temperature_meter.mainValue/temperature_meter.maxValue)
                height: parent.height
                radius: parent.radius
                clip: true
                color: "red"
                anchors.left: parent.left
            }
        }

    }

    Text {  // Text labeling what the bar is about ex: temp, mph
        id: textLabel
        text: "Temperature"
        font.pixelSize: 15

        anchors.bottom: mainBar.top
        anchors.left: mainBar.left
        anchors.leftMargin: 10

        color: "white"
    }

    Text {  // Text for mainValue or numbers
        id: textValue
        text: temperature_meter.mainValue
        font.pixelSize: 15
        color: "white"

        anchors.bottom: mainBar.top
        anchors.right: mainBar.right
        anchors.rightMargin: 25


        Text {  // Text for displaying unitValue or units
            id: textUnit
            text: "°F"
            font.pixelSize: 15
            color: "white"

            anchors.left: parent.right
            anchors.bottom: parent.bottom

        }

    }

    // Main Bar: Border housing the whole bar containing the value
    Rectangle {
        
        // Customize the text labels how ever you like here:
        property double mainValue: 50.0                // Current Value. Anything will do.
        property double maxValue: 100.0                 // Max value possible ex: max mph
        property double minValue: 0.0                   // Min value possible ex: mph=0
        property string unitValue: "%"                // Units for the value ex: mph, mi

        id: batteryMainBar
        width: 400          // Width of the entire bar meter
        height: 20          // Height of the entire bar meter

        radius: 15          // Radius of the entire bar meter. Does affect inner bars.
        color: "black"      // Border Colors


        anchors.right: parent.right
        anchors.rightMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

        clip: true

        // Empty Bar: Housing the value bar
        Rectangle {
            id: batteryEmptyBar
            width: parent.width - 6
            height: parent.height - 6
            radius: parent.radius

            anchors.centerIn: parent
            anchors.bottom: parent.bottom

            // Value Bar: Displaying the current value
            Rectangle {

                id: batteryValueBar
                width: parent.width * (battery_capacity.mainValue/battery_capacity.maxValue)
                height: parent.height
                radius: parent.radius
                clip: true
                color: "red"
                anchors.left: parent.left
            }
        }

    }

    Text {  // Text labeling what the bar is about ex: temp, mph
        id: batteryTextLabel
        text: "Battery Capacity"
        font.pixelSize: 15

        anchors.bottom: batteryMainBar.top
        anchors.left: batteryMainBar.left
        anchors.leftMargin: 10

        color: "white"
    }

    Text {  // Text for mainValue or numbers
        id: batteryTextValue
        text: battery_capacity.mainValue
        font.pixelSize: 15
        color: "white"

        anchors.bottom: batteryMainBar.top
        anchors.right: batteryMainBar.right
        anchors.rightMargin: 25


        Text {  // Text for displaying unitValue or units
            id: batteryTextUnit
            text: "%"
            font.pixelSize: 15
            color: "white"

            anchors.left: parent.right
            anchors.bottom: parent.bottom

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