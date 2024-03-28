import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

Item {
    id: root

    // Default size can be overridden as needed
    width: 170
    height: 50

    // Customizable properties for the label
    property string label: "Timer"
    property int currValue: 0
    property string unit: "unit"

    property int fontSize: 20
    property string color: "white"
    property color borderColor: "#FFFFFF" // Default border color
    property int borderWidth: 2 // Default border width
    property int borderRadius: 5 // Default border radius for rounded corners

    // Border Rectangle
    Rectangle {
        id: borderRect
        width: root.width
        height: root.height
        anchors.fill: parent // Make the rectangle fill the parent Item
        border.color: root.borderColor
        border.width: root.borderWidth
        radius: root.borderRadius // Adjust for rounded corners
        color: "black" // Background color of the rectangle, set to transparent to only show the border

        // Text item for the label
        Text {
            id: titleText
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent
            text: root.label
            font.pixelSize: root.fontSize
            //font.bold: true
            color: root.color

            layer.enabled: true
            layer.effect: DropShadow {
                horizontalOffset: 2
                verticalOffset: 2
                radius: 5
                samples: 64
                color: "gray"
            }
        }

        Text {
            anchors.top: titleText.bottom
            anchors.horizontalCenter: titleText.horizontalCenter
            text: currValue
            font.pixelSize: root.fontSize
            font.bold: true
            color: root.color

            layer.enabled: true
            layer.effect: DropShadow {
                horizontalOffset: 2
                verticalOffset: 2
                radius: 5
                samples: 64
                color: "#b50000"
            }
        }

    }

}