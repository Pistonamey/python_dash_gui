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
            ratio1: 2
            ratio2: 3
            units: "°C"
        }

        SecondPanels {
            title: "Intake Pressure"
            currValue: afr_ratio.currValue
            ratio1: 2
            ratio2: 3
            units: "%"
        }

        SecondPanels {
            title: "Intake Temperature"
            currValue: intakePressureLabel.currValue
            ratio1: 2
            ratio2: 3
            units: "°C"
        }

        SecondPanels {
            title: "Run Time"
            currValue: runtimeLabel.currValue
            ratio1: 2
            ratio2: 3
            units: "sec"
        }

        SecondPanels {
            title: "Fuel Level"
            currValue: fuelLevelLabel.currValue
            ratio1: 2
            ratio2: 3
            units: "%"
        }

        SecondPanels {
            title: "Fuel Type"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: fuelTypeLabel.stringValue
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }


        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }

        SecondPanels {
            title: "Default"
            currValue: 1
            ratio1: 2
            ratio2: 3
            units: "Unit"
        }


    }
}