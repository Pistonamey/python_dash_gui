import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12

Rectangle { // This is the main background

    MouseArea {
        anchors.fill: parent
            onClicked: {
            console.log("Button clicked")
            // Add any actions you want the button to perform here
            ld.source = ""
        }
    }

    width: 1024
    height: 600 // Adjusted to accommodate 2x2 grid
    color: "black"

    property double boost: Math.random() * 40 - 20 // Random number between -20 and 20
    property double afr: 10 + Math.random() * 10 // Random number between 10 and 20

    GridLayout {
        columns: 4
        rows: 4
        anchors.fill: parent
        rowSpacing: 0
        columnSpacing: 0


        SecondPanels {
            title: "Coolant Temperature"
            currValue: temperature.currValue
            units: "°C"
        }

        SecondPanels {
            title: "Intake Pressure"
            currValue: intakePressureLabel.currValue
            units: "%"
        }

        SecondPanels {
            title: "Intake Temperature"
            currValue: intakeTempLabel.currValue
            units: "°C"
        }

        StringPanels {
            title: "Run Time"
            currValue: runtimeLabel.currValue
        }

        SecondPanels {
            title: "Fuel Level"
            currValue: fuelLevelLabel.currValue
            units: "%"
        }

        StringPanels {
            title: "Fuel Type"
            currValue: fuelTypeLabel.currValue
        }

        SecondPanels {
            title: "Speed"
            currValue: Math.round(speedometer.currSpeed)
            units: "mph"
        }

        SecondPanels {
            title: "Speed"
            currValue: Math.round(speedometer.currSpeed * 1.60934)
            units: "kmh"
        }

        SecondPanels {
            title: "RPM"
            currValue: Math.round(RPM_Meter.currRPM)
            units: " x 1000 revs"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            units: "Unit"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            units: "Unit"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            units: "Unit"
        }

    }
}
