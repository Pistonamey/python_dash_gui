import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Effects


// Holds all the bar meter and all text labels
Rectangle {

    // Customize the size and radius of the bar_meter:
    property int bar_meter_width: 480     // Width of the entire bar meter
    property int bar_meter_height: 40     // Height of the entire bar meter
    property int bar_meter_radius: 20      // Radius of the entire bar meter. Does affect inner bars.

    // Customize the inner bar meter colors how ever you like here:
    property string value_bar_gradiant_left: "red"         // Color of main bar, left side.
    property string value_bar_gradiant_right: "pink"      // Color of main bar, right side

    property string empty_bar_gradiant_left: "#2E2E2E"         // Color of empty bar, left side.
    property string empty_bar_gradiant_right: "gray"       // Color of empty bar, right side

    property string border_colors: "black"                  // Specifically the border around the bar meter

    // Customize the title label here:
    property string label_name: "Example"
    property string label_color: "white"
    property int label_size: 20

    // Customize the text labels how ever you like here:
    property double mainValue: 100.0                // Current Value. Anything will do.
    property double maxValue: 300.0                 // Max value possible ex: max mph
    property double minValue: 0.0                   // Min value possible ex: mph=0
    property string unitValue: "F"                // Units for the value ex: mph, mi

    property int main_text_size: 30                 // Size of the text displaying main value
    property int unit_text_size: 20                 // Size of the text displaying units

    property string main_text_color: "white"        // Color of text displaying main value
    property string unit_text_color: "gray"         // Color of text displaying units

    // Other information of the bar_meter
    id: bar_meter
    width: bar_meter_width
    height: bar_meter_height + main_text_size - 5
    x: 0
    y: 0
    color: "#2E2E2E"                                   // Change this to "transparent" when you put this on the GUI

    // Main Bar: Border housing the whole bar containing the value
    Rectangle {
        id: mainBar
        width: bar_meter_width
        height: bar_meter_height

        radius: bar_meter_radius
        color: border_colors

        anchors.bottom: parent.bottom
        clip: true

        // Empty Bar: Housing the value bar
        Rectangle {
            id: emptyBar
            width: parent.width - 6
            height: parent.height - 6
            radius: parent.radius

            anchors.centerIn: parent

            gradient: Gradient {
                orientation: Gradient.Horizontal
                GradientStop { position: 0.0; color: empty_bar_gradiant_left }
                GradientStop { position: 0.7; color: empty_bar_gradiant_right }
            }

            // Value Bar: Displaying the current value
            Rectangle {

                id: valueBar
                width: parent.width * (mainValue/maxValue)
                height: parent.height
                radius: parent.radius
                clip: true


                anchors.left: parent

                gradient: Gradient {
                    orientation: Gradient.Horizontal
                    GradientStop { position: 0.0; color: value_bar_gradiant_left }
                    GradientStop { position: 0.7; color: value_bar_gradiant_right }
                }
            }
        }

    }

    Text {  // Text labeling what the bar is about ex: temp, mph
        id: textLabel
        text: label_name
        font.pixelSize: label_size

        anchors.bottom: mainBar.top
        anchors.left: mainBar.left

        bottomPadding: 0
        leftPadding: 20

        color: label_color

    }

    Text {  // Text for mainValue or numbers
        id: textValue
        text: mainValue
        font.pixelSize: label_size
        color: label_color

        anchors.bottom: mainBar.top
        anchors.right: mainBar.right

        bottomPadding: 0
        rightPadding: 30

        Text {  // Text for displaying unitValue or units
            id: textUnit
            text: "<b>" + unitValue + "</b>"
            font.pixelSize: unit_text_size
            color: unit_text_color

            anchors.left: parent.right
            anchors.bottom: parent.bottom

            bottomPadding: 0
            rightPadding: 15
        }

    }

}