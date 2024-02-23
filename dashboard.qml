import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0

Rectangle {
     width: 1024
     height: 600
     color: "#000000"

     CircularGauge {
          //property real gauge_value: 40.0
          anchors.centerIn: parent
          value: speedometer.currSpeed
          maximumValue: speedometer.maxSpeed  // Largest Value
          minimumValue: speedometer.minSpeed       // Smallest Value
          style: CircularGaugeStyle {
               id: style
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
     }

     // Customize the size and radius of the bar_meter:
     property int bar_meter_width: 480     // Width of the entire bar meter
     property int bar_meter_height: 30     // Height of the entire bar meter
     property int bar_meter_radius: 15      // Radius of the entire bar meter. Does affect inner bars.

     property string border_colors: "black"                  // Specifically the border around the bar meter

     // Customize the text labels how ever you like here:
     property double mainValue: 100.0                // Current Value. Anything will do.
     property double maxValue: 300.0                 // Max value possible ex: max mph
     property double minValue: 0.0                   // Min value possible ex: mph=0
     property string unitValue: "°F"                // Units for the value ex: mph, mi

     property int main_text_size: 20                 // Size of the text displaying main value
     property int unit_text_size: 15                 // Size of the text displaying units

     property string main_text_color: "white"        // Color of text displaying main value
     property string unit_text_color: "gray"         // Color of text displaying units

     // Customize the title label here:
     property string label_name: "Temperature"
     property string label_color: "white"
     property int label_size: 15

     // Main Bar: Border housing the whole bar containing the value
     Rectangle {
          id: mainBar
          width: bar_meter_width
          height: bar_meter_height

          radius: bar_meter_radius
          color: border_colors


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
        text: label_name
        font.pixelSize: label_size

        anchors.bottom: mainBar.top
        //anchors.left: mainBar.left
        x: 30


        color: label_color

    }

    Text {  // Text for mainValue or numbers
        id: textValue
        text: temperature_meter.mainValue
        font.pixelSize: label_size
        color: label_color

        anchors.bottom: mainBar.top
        //anchors.right: mainBar.right
        x: bar_meter_width - 30


        Text {  // Text for displaying unitValue or units
            id: textUnit
            text: unitValue
            font.pixelSize: unit_text_size
            color: label_color

            anchors.left: parent.right
            anchors.bottom: parent.bottom

        }

    }

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

}