import QtQuick 2.7
import QtQuick.Controls 2.15
import QtQuick.Controls.Styles 1.4
import QtQuick.Window 2.2
import Qt.labs.folderlistmodel 2.15
import Signal 1.0

ApplicationWindow {
    id: window
    width: 1080
    height: 720
    visible: true

    Calibration {
      id: calibration
    }

    // indicator for a program starting
    property int starting: 0

    // indicator for a current calibrated angle
    property int ninetyturn: 0

    // 6 base pages
    // but we use only 3 pages - home, about, view
    header: TabBar {
        TabButton {
          id: home
          implicitHeight: 70
          font.pixelSize: 30
          text: "Home"
          onClicked: starting ? stackView.replace(page1_2) : stackView.replace(page1)
        }
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "About"
          onClicked: stackView.replace(page2)
        }
        /*
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "Connect"
          onClicked: stackView.replace(page3)
        }
        */
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "View"
          onClicked: stackView.replace(page4)
        }
        /*
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "Audio"
          onClicked: stackView.replace(page5)
        }
        */
        /*
        TabButton {
          implicitHeight: 70
          font.pixelSize: 30
          text: "Settings"
          onClicked: stackView.replace(page6)
        }
        */
    }

    /* home page
       only have start button for stating app*/
    Component {
      id: page1
      Page {
        Label {
          anchors.centerIn: parent
        }
        // 'Start' button on first home page
        Item {
          id: button_round
          width: 300
          height: 300
          property alias buttonText: innerText.text;
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
              starting = 1

              // move on the calibrating page
              stackView.replace(page1_2)

              // this will run the desktop.py
              //calibration.cmdline("python ./bluetooth_comms/desktop.py")
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

    /* calibration page
       When user presses 'space bar', it shows whether calibrating is succeesful or not
       by colored circle*/
    Component {
      id: page1_2
      Page {
        Label {
          anchors.centerIn: parent
        }
        // calibrate at 0 box
        Rectangle {
          anchors {
            top: parent.top
            topMargin: 150
            left: parent.left
            leftMargin: 340
          }
          Text {
             anchors {
              top: parent.top
              topMargin: 25
              left: parent.left
              leftMargin: 30
            }
            text: "Calibrating at 0"
            font.pointSize: 20
          }
          width: 400
          height: 80
          color: "#E0E0E0"
        }
        // colored indicator for 0 degree
        Rectangle {
          id: zerorec
          anchors {
            top: parent.top
            topMargin: 165
            left: parent.left
            leftMargin: 675
          }
          width: 50
          height: width
          color: "red"
          radius: width*0.5
        }
        // calibrate at 90 box
        Rectangle {
          anchors {
            top: parent.top
            topMargin: 250
            left: parent.left
            leftMargin: 340
          }
          Text {
             anchors {
              top: parent.top
              topMargin: 25
              left: parent.left
              leftMargin: 30
            }
            text: "Calibrating at 90"
            font.pointSize: 20
          }
          width: 400
          height: 80
          color: "#E0E0E0"
        }
        // colored indicator for 90 degrees
        Rectangle {
          id: ninetyrec
          anchors {
            top: parent.top
            topMargin: 265
            left: parent.left
            leftMargin: 675
          }
          width: 50
          height: width
          color: "red"
          radius: width*0.5
        }
        // running box
        Rectangle {
          anchors {
            top: parent.top
            topMargin: 350
            left: parent.left
            leftMargin: 340
          }
          Text {
             anchors {
              top: parent.top
              topMargin: 25
              left: parent.left
              leftMargin: 30
            }
            text: "Running..."
            font.pointSize: 20
          }
          width: 400
          height: 80
          color: "#E0E0E0"
        }
        // key event for indicator of calibration of each degree
        Item {
          focus: true
          Keys.onPressed: {
            if (event.key == Qt.Key_Space && ninetyturn == 0)
            {
              console.log("calibrating 0 degree")
              zerorec.color = 'green'
              ninetyturn = 1;
              event.accepted = true;
            }
            else if (event.key == Qt.Key_Space && ninetyturn == 1){
              console.log("calibrating 90 degree")
              ninetyrec.color = 'green'
              event.accepted = true;
            }
            else if (event.key == Qt.Key_R){
              console.log("recablirate")
              zerorec.color = 'red'
              ninetyrec.color = 'red'
              ninetyturn = 0;
              event.accepted = true;
            }
          }
        }
      }
    }

    /* About page
       This page says how to use this app to user */
    Component {
      id: page2
      Page {
        Label {
          anchors.centerIn: parent
        }
        Text {
            text: "How to Use"
            font.pointSize: 40
            anchors {
                top: parent.top
                topMargin: 25
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "1. Band a strap with main component above the knee"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 100
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "2. Band an another strap below the knee"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 140
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "3. Make sure it is tied tightly"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 180
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "4. Open the App"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 220
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "5. Click start button"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 260
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "6. Straighten out both legs, then press space bar"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 300
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "7. Fold both legs until 90°, then press space bar"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 340
                left: parent.left
                leftMargin: 30
            }
        }
        Text {
            text: "8. Walk around with your preferred gait speed"
            font.pointSize: 20
            anchors {
                top: parent.top
                topMargin: 380
                left: parent.left
                leftMargin: 30
            }
        }
      }
    }

    /* Connect page (UNUSED)
       This page turns on and off bluetooth and shows available devices */
/*
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
*/

    /* view page
       This page shows current angles and tempo. And, user can stop and recalibrate */
    Component {
      id: page4
      Page {
        Label {
          anchors.centerIn: parent
        }
        // image of legs
        Image {
            source: "images/legs.png"
            anchors {
              top: parent.top
              topMargin: 25
              left: parent.left
              leftMargin: 40
            }
        }
        // the box for showing current left and right angle, and pace/s
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

        // Stop button
        Item {
          id: button_1
          width: 170
          height: 70
          property alias buttonText: innerText.text;
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
            radius: 2
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

        // Recalibrate button
        Item {
          id: button_2
          width: 170
          height: 70
          property alias buttonText: innerText.text;
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
            radius: 2
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
            onPressed: {
                button_2.state="Pressed"
                home.clicked();
            }
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

    /* audio page (UNUSED)
       This page shows the list of songs and cover image
       User can choose the songs and adjust the volumes */
/*
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
                    folder: "music/playlists/90-100_bpm"
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

*/

    // setting page (UNUSED)
    // currently does not have any items. This page will be used when it needs
    // such as the imporing and exporing of user's information
    // i.e. music list
/*
    Component {
      id: page6
      Page {
        Label {
          text: qsTr("Sixth page")
          anchors.centerIn: parent
        }
      }
    }
*/

    /* adjust animation of stackview and showing page by stack */
    StackView {
        id: stackView
        focus: true
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
