import QtQuick 2.15
import QtQuick.Controls 2.15
//window containing the application
ApplicationWindow {

  visible: true
  width: 1080
  height: 720
  title: "HelloApp"

  // RAS logo
  Rectangle {
    anchors {
      top: parent.top
      topMargin: 25
      left: parent.left
      leftMargin: 25
    }
      width: 100
      height: 100
      color: "white"
      border.color: "black"
      border.width: 2
      radius: width*0.5
      Text {
        anchors {
          top: parent.top
          topMargin: 35
          left: parent.left
          leftMargin: 30
        }
        color: "black"
        text: "RAS"
        font.pixelSize: 24
      }
  }

  // Menu tab
  Rectangle {
    anchors {
      top: parent.top
      topMargin: 40
      left: parent.left
      leftMargin: 140
    }
      width: 920
      height: 70
      color: "white"
      border.color: "black"
      border.width: 2
  }

  // button 1
  Button {
    anchors {
      top: parent.top
      topMargin: 50
      left: parent.left
      leftMargin: 150
    }
        id: button_1
        text: "Home"
        font.pixelSize: 30
        background: Rectangle {
            implicitWidth: 150
            implicitHeight: 50
            color: button.down ? "#d6d6d6" : "#f6f6f6"
        }
    }
  // button 2
  Button {
    anchors {
      top: parent.top
      topMargin: 50
      left: parent.left
      leftMargin: 300
    }
        id: button_2
        text: "About"
        font.pixelSize: 30
        background: Rectangle {
            implicitWidth: 150
            implicitHeight: 50
            color: button.down ? "#d6d6d6" : "#f6f6f6"
        }
    }
  // button 3
  Button {
    anchors {
      top: parent.top
      topMargin: 50
      left: parent.left
      leftMargin: 450
    }
        id: button_3
        text: "Connect"
        font.pixelSize: 30
        background: Rectangle {
            implicitWidth: 150
            implicitHeight: 50
            color: button.down ? "#d6d6d6" : "#f6f6f6"
        }
    }
  // button 4
  Button {
    anchors {
      top: parent.top
      topMargin: 50
      left: parent.left
      leftMargin: 600
    }
        id: button_4
        text: "View"
        font.pixelSize: 30
        background: Rectangle {
            implicitWidth: 150
            implicitHeight: 50
            color: button.down ? "#d6d6d6" : "#f6f6f6"
        }
    }
  // button 5
  Button {
    anchors {
      top: parent.top
      topMargin: 50
      left: parent.left
      leftMargin: 750
    }
        id: button_5
        text: "Audio"
        font.pixelSize: 30
        background: Rectangle {
            implicitWidth: 150
            implicitHeight: 50
            color: button.down ? "#d6d6d6" : "#f6f6f6"
        }
    }
  // button 6
  Button {
    anchors {
      top: parent.top
      topMargin: 50
      left: parent.left
      leftMargin: 900
    }
      id: button
      text: "Settings"
      font.pixelSize: 30
      background: Rectangle {
          implicitWidth: 150
          implicitHeight: 50
          color: button.down ? "#d6d6d6" : "#f6f6f6"
      }
  }
}
