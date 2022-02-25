import QtQuick 2.7
import QtQuick.Controls 2.0

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
          text: qsTr("First page")
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
          text: qsTr("Third page")
          anchors.centerIn: parent
        }
      }
    }

    Component {
      id: page4
      Page {
        Label {
          text: qsTr("Fourth page")
          anchors.centerIn: parent
        }
      }
    }

    Component {
      id: page5
      Page {
        Label {
          text: qsTr("Fifth page")
          anchors.centerIn: parent
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
