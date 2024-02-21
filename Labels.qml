import QtQuick 2.0

Item {
    id: root

    // Default size can be overridden as needed
    width: 200
    height: 50

    // Customizable properties for the label
    property string label: "Default Label"
    property int fontSize: 20
    property string color: "white"
    property color borderColor: "#FFFFFF" // Default border color
    property int borderWidth: 2 // Default border width
    property int borderRadius: 5 // Default border radius for rounded corners

    // Border Rectangle
    Rectangle {
        id: borderRect
        anchors.fill: parent // Make the rectangle fill the parent Item
        border.color: root.borderColor
        border.width: root.borderWidth
        radius: root.borderRadius // Adjust for rounded corners
        color: "transparent" // Background color of the rectangle, set to transparent to only show the border

        // Text item for the label
        Text {
            anchors.centerIn: parent
            text: root.label
            font.pixelSize: root.fontSize
            color: root.color
        }
    }
}
