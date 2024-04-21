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
            title: "Boost"
            currValue: 0
            ratio1: 2
            ratio2: 3
            units: "PSI"
        }

        SecondPanels {
            title: "AF Sens 1 Ratio"
            currValue: afr_ratio.currValue
            ratio1: 2
            ratio2: 3
            units: "AFR"
        }

        SecondPanels {
            title: "Battery Level"
            currValue: 0
            ratio1: 2
            ratio2: 3
            units: "%"
        }

        SecondPanels {
            title: "Energy use"
            currValue: 0
            ratio1: 2
            ratio2: 3
            units: "kWh"
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