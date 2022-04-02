import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Window 2.2
import Qt.labs.folderlistmodel 2.15

ApplicationWindow {
    id: window
    width: 1080
    height: 720
    visible: true

    header: TabBar {
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "Home"
          onClicked: stackView.replace(page1)
        }
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "About"
          onClicked: stackView.replace(page2)
        }
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "Connect"
          onClicked: stackView.replace(page3)
        }
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "View"
          onClicked: stackView.replace(page4)
        }
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "Audio"
          onClicked: stackView.replace(page5)
        }
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "Settings"
          onClicked: stackView.replace(page6)
        }

    }
    
    Component {
      id: page1
      Page {
        Label {
          anchors.centerIn: parent
        }
        Item {
          id: button_round
          width: 400
          height: 400
          property alias buttonText: innerText.text;
          property color color: "white"
          property color hoverColor: "#aaaaaa"
          property int fontSize: 10
          property int borderWidth: 1
          property int borderRadius: 2
          scale: state === "Pressed" ? 0.96 : 1.0
          onEnabledChanged: state = ""
          signal clicked
          anchors.centerIn: parent

          //define a scale animation
          Behavior on scale {
            NumberAnimation {
              duration: 100
              easing.type: Easing.InOutQuad
            }
          }

          //Rectangle to draw the button
          Rectangle {
            radius: 400
            id: rectanglebutton_round
            anchors.fill: parent
            color: button_round.enabled ? "#33FF33" : "#006600"

            Text {
                id: innerText
                text: "Start"
                font.pointSize: 20
                color: "#000000"
                anchors.centerIn: parent
            }
          }

          //change the color of the button in differen button states
          states: [
            State {
              name: "Hovering"
              PropertyChanges {
                target: rectanglebutton_round
                color: "#00CC00"
              }
            },
            State {
              name: "Pressed"
              PropertyChanges {
                target: rectanglebutton_round
                color: "#009900"
              }
            }
          ]

          //define transmission for the states
          transitions: [
            Transition {
              from: ""; to: "Hovering"
              ColorAnimation { duration: 10 }
            },
            Transition {
              from: "*"; to: "Pressed"
              ColorAnimation { duration: 10 }
            }
          ]

          //Mouse area to react on click events
          MouseArea {
            hoverEnabled: true
            anchors.fill: button_round
            onEntered: { button_round.state='Hovering'}
            onExited: { button_round.state=''}
            onClicked: {
              button_round.clicked();
              stackView.replace(page1_2)
            }
            onPressed: { button_round.state="Pressed" }
            onReleased: {
              if (containsMouse)
                button_round.state="Hovering";
              else
                button_round.state="";
            }
          }
        }
      }
    }

    Component {
      id: page1_2
      Page {
        Label {
          text: qsTr("Calibration page")
          anchors.centerIn: parent
        }
      }
    }

    Component {
      id: page2
      Page {
        Label {
          text: qsTr("Second page")
          anchors.centerIn: parent
        }
      }
    }

    Component {
      id: page3
      Page {
        Label {
          anchors.centerIn: parent
        }
        // bluetooth box
        Rectangle {
          anchors {
            top: parent.top
            topMargin: 50
            left: parent.left
            leftMargin: 40
          }
          width: 1000
          height: 100
          border.color: "black"
          border.width: 5
          radius: 10
          Text {
            anchors {
              top: parent.top
              topMargin: 25
              left: parent.left
              leftMargin: 40
            }
            id: myText
            font.family: "Helvetica"
            font.pointSize: 30
            text:  qsTr("Bluetooth")
          }
          Switch {
            anchors {
              top: parent.top
              topMargin: 30
              left: parent.left
              leftMargin: 900
            }
          }
          // device box
          Rectangle {
          anchors {
            top: parent.top
            topMargin: 120
            left: parent.left
            leftMargin: 0
          }
          width: 1000
          height: 400
          border.color: "black"
          border.width: 5
          radius: 10
          Text {
            anchors {
              top: parent.top
              topMargin: 25
              left: parent.left
              leftMargin: 40
            }
            font.family: "Helvetica"
            font.pointSize: 30
            text:  qsTr("Devices")
          }
          }
        }
      }
    }

    Component {
      id: page4
      Page {
        Label {
          anchors.centerIn: parent
        }
        Image {
            source: "images/legs.png"
            anchors {
              top: parent.top
              topMargin: 25
              left: parent.left
              leftMargin: 40
            }
        }
        Rectangle {
          anchors {
            top: parent.top
            topMargin: 75
            left: parent.left
            leftMargin: 600
          }
          Text {
            text: "Left Knee Angle:"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 20
                left: parent.left
                leftMargin: 30
            }
          }
          Text{
            text: "Right Knee Angle:"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 80
                left: parent.left
                leftMargin: 30
            }
          }
          Text{
            text: "Paces per Minute:"
            font.pointSize: 20
            anchors {
              top: parent.top
              topMargin: 140
              left: parent.left
              leftMargin: 30
            }
          }
          width: 400
          height: 200
          border.color: "black"
          border.width: 5
          radius: 10
        }

        Item {
          id: button_1
          width: 170
          height: 70
          property alias buttonText: innerText.text;
          property color color: "white"
          property color hoverColor: "#aaaaaa"
          property int fontSize: 10
          property int borderWidth: 1
          property int borderRadius: 2
          scale: state === "Pressed" ? 0.96 : 1.0
          onEnabledChanged: state = ""
          signal clicked

          anchors {
            top: parent.top
            topMargin: 450
            left: parent.left
            leftMargin: 350
          }

          //define a scale animation
          Behavior on scale {
            NumberAnimation {
              duration: 100
              easing.type: Easing.InOutQuad
            }
          }

          //Rectangle to draw the button
          Rectangle {
            id: rectangleButton_1
            anchors.fill: parent
            radius: borderRadius
            color: button_1.enabled ? "#FF3333" : "#660000"

            Text {
                id: innerText
                text: "Stop"
                font.pointSize: 20
                color: "#000000"
                anchors.centerIn: parent
            }
          }

          //change the color of the button in differen button states
          states: [
            State {
              name: "Hovering"
              PropertyChanges {
                target: rectangleButton_1
                color: "#CC0000"
              }
            },
            State {
              name: "Pressed"
              PropertyChanges {
                target: rectangleButton_1
                color: "#990000"
              }
            }
          ]

          //define transmission for the states
          transitions: [
            Transition {
              from: ""; to: "Hovering"
              ColorAnimation { duration: 10 }
            },
            Transition {
              from: "*"; to: "Pressed"
              ColorAnimation { duration: 10 }
            }
          ]

          //Mouse area to react on click events
          MouseArea {
            hoverEnabled: true
            anchors.fill: button_1
            onEntered: { button_1.state='Hovering'}
            onExited: { button_1.state=''}
            onClicked: { button_1.clicked();}
            onPressed: { button_1.state="Pressed" }
            onReleased: {
              if (containsMouse)
                button_1.state="Hovering";
              else
                button_1.state="";
            }
          }
        }

        Item {
          id: button_2
          width: 170
          height: 70
          property alias buttonText: innerText.text;
          property color color: "white"
          property color hoverColor: "#aaaaaa"
          property int fontSize: 10
          property int borderWidth: 1
          property int borderRadius: 2
          scale: state === "Pressed" ? 0.96 : 1.0
          onEnabledChanged: state = ""
          signal clicked

          anchors {
            top: parent.top
            topMargin: 450
            right: parent.right
            rightMargin: 350
          }

          //define a scale animation
          Behavior on scale {
            NumberAnimation {
              duration: 100
              easing.type: Easing.InOutQuad
            }
          }

          //Rectangle to draw the button
          Rectangle {
            id: rectangleButton_2
            anchors.fill: parent
            radius: borderRadius
            color: button_2.enabled ? "#33FF33" : "#006600"

            Text {
                id: innerText_2
                text: "Recalibrate"
                font.pointSize: 20
                color: "#000000"
                anchors.centerIn: parent
            }
          }

          //change the color of the button in differen button states
          states: [
            State {
              name: "Hovering"
              PropertyChanges {
                target: rectangleButton_2
                color: "#00CC00"
              }
            },
            State {
              name: "Pressed"
              PropertyChanges {
                target: rectangleButton_2
                color: "#009900"
              }
            }
          ]

          //define transmission for the states
          transitions: [
            Transition {
              from: ""; to: "Hovering"
              ColorAnimation { duration: 10 }
            },
            Transition {
              from: "*"; to: "Pressed"
              ColorAnimation { duration: 10 }
            }
          ]

          //Mouse area to react on click events
          MouseArea {
            hoverEnabled: true
            anchors.fill: button_2
            onEntered: { button_2.state='Hovering'}
            onExited: { button_2.state=''}
            onClicked: { button_2.clicked();}
            onPressed: { button_2.state="Pressed" }
            onReleased: {
              if (containsMouse)
                button_2.state="Hovering";
              else
                button_2.state="";
            }
          }
        }
      }
    }

    Component {
      id: page5
      Page {
        Label {
            anchors.centerIn: parent
        }
        // music cover image box, but may not used
        Rectangle {
          anchors {
            top: parent.top
            topMargin: 50
            left: parent.left
            leftMargin: 90
          }
          width: 400
          height: 400
          border.color: "black"
          border.width: 5
          radius: 10
        }
        // playlist box
        Rectangle {
          anchors {
            top: parent.top
            topMargin: 50
            left: parent.left
            leftMargin: 550
          }
          width: 400
          height: 570
          border.color: "black"
          border.width: 5
          radius: 10
          ListView {
            width: 380
            height: 450
            FolderListModel {
                    id: folderModel
                    folder: "music/playlists/95-100_bpm"
                    nameFilters: ["*.mp3", "*.wav"]
                }

                Component {
                    id: fileDelegate
                    Text {
                        text: fileName
                        font.pointSize: 13
                    }
                }

                anchors {
                  top: parent.top
                  topMargin: 10
                  left: parent.left
                  leftMargin: 10
                }
                model: folderModel
                delegate: fileDelegate
            }
        }
        // play, pause, next, previous,, control box
        Rectangle {
            anchors {
              top: parent.top
              topMargin: 470
              left: parent.left
              leftMargin: 90
            }
            width: 400
            height: 150
            border.color: "black"
            border.width: 5
            radius: 10
        }
      }
    }


    Component {
      id: page6
      Page {
        Label {
          text: qsTr("Sixth page")
          anchors.centerIn: parent
        }
      }
    }



    StackView {
        id: stackView
        anchors.fill: parent
        replaceEnter: Transition {
            NumberAnimation { property: "opacity"; to: 1.0; duration: 1 }
        }
        replaceExit: Transition {
            NumberAnimation { property: "opacity"; to: 0.0; duration: 1 }
        }
    }

    Component.onCompleted: stackView.push(page1)
}
