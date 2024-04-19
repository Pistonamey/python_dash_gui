import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

Button {
    id: switchButton
    text: "Switch View" // The text displayed on the button
    font.pixelSize: 18 // Adjust the font size as needed
    color: "black" // Text color
    background: Rectangle {
        color: "#FF0000" // Button background color
        border.color: "black" // Button border color
        border.width: 2 // Button border width
        radius: 10 // Rounded corners
    }
    width: 120 // Adjust the width of the button
    height: 40 // Adjust the height of the button
    
    // Add an onClicked signal handler if you want the button to perform an action when clicked
    onClicked: {
        console.log("Button clicked")
        // Add any actions you want the button to perform here
    }
}