import "."
import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtGraphicalEffects 1.0

// Holds all the bar meter and all text labels
Rectangle {

    // Customize the size and radius of the bar_meter:
    property int bar_meter_width: 400     // Width of the entire bar meter
    property int bar_meter_height: 20     // Height of the entire bar meter
    property int bar_meter_radius: 20      // Radius of the entire bar meter. Does affect inner bars.

    // Customize the inner bar meter colors how ever you like here:
    property string value_bar_color: "red"         // Color of main bar
    property string empty_bar_color: "white"       // Color of empty bar

    property string border_colors: "black"                  // Specifically the border around the bar meter

    // Customize the title label here:
    property string label_name: "Example"
    property string label_color: "white"
    property int label_size: 15

    // Customize the text labels how ever you like here:
    property double mainValue: 100.0                // Current Value. Anything will do.
    property double maxValue: 100.0                 // Max value possible ex: max mph
    property double minValue: 0.0                   // Min value possible ex: mph=0
    property string unitValue: "F"                // Units for the value ex: mph, mi

    property int main_text_size: 15                 // Size of the text displaying main value
    property int unit_text_size: 15                 // Size of the text displaying units

    property string main_text_color: "white"        // Color of text displaying main value
    property string unit_text_color: "white"         // Color of text displaying units

    // Other information of the bar_meter
    id: bar_meter
    width: bar_meter_width
    height: bar_meter_height + main_text_size + 5       // Adjust if needed
    radius: bar_meter_radius

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

            color: empty_bar_color
            gradient: Gradient {
                GradientStop { position: 0.0; color: "white" }
                GradientStop { position: 0.33; color: "white" }
            }

            // Value Bar: Displaying the current value
            Rectangle {

                id: valueBar
                width: parent.width * (mainValue/maxValue)
                height: parent.height
                radius: parent.radius
                clip: true


                anchors.left: parent

                color: value_bar_color

                gradient: Gradient {
                    GradientStop { position: 0.0; color: "red" }
                    GradientStop { position: 0.33; color: "red" }
                    GradientStop { position: 1.0; color: "red" }
                }

                layer.enabled: true
                layer.effect: Glow {
                    radius: 8
                    samples: 64
                    color: "transparent"
                }


            }
        }

    }

    Text {  // Text labeling what the bar is about ex: temp, mph
        id: textLabel
        text: label_name
        font.pixelSize: label_size
        //font.bold: true

        anchors.bottom: mainBar.top
        anchors.left: mainBar.left
        anchors.leftMargin: 10

        color: label_color


        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 2
            verticalOffset: 2
            radius: 5
            samples: 64
            color: "transparent"
        }

    }

    Text {  // Text for displaying unitValue or units
        id: textUnit
        text: unitValue
        font.pixelSize: unit_text_size
        color: unit_text_color


        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 0
            samples: 64
            color: "red"
        }

        anchors.bottom: mainBar.top
        anchors.right: mainBar.right
        anchors.rightMargin: 10

    }

    Text {  // Text for mainValue or numbers
        id: textValue
        text: mainValue
        font.pixelSize: main_text_size
        color: label_color

        font.bold: true

        anchors.right: textUnit.left
        anchors.bottom: textUnit.bottom

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 0
            samples: 64
            color: "#b50000"
        }


    }



}