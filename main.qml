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
      topMargin: 48
      left: parent.left
      leftMargin: 148
    }
      width: 904
      height: 54
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
        text: "Home"
        font.pixelSize: 30
        background: Rectangle {
          implicitWidth: 150
          implicitHeight: 50
                color: parent.down ? "#E0E0E0" :
                        (parent.hovered ? "#FFFFFF" : "#FFFFFF")
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
        text: "About"
        font.pixelSize: 30
        background: Rectangle {
          implicitWidth: 150
          implicitHeight: 50
                color: parent.down ? "#E0E0E0" :
                        (parent.hovered ? "#FFFFFF" : "#FFFFFF")
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
        text: "Connect"
        font.pixelSize: 30
        background: Rectangle {
          implicitWidth: 150
          implicitHeight: 50
                color: parent.down ? "#E0E0E0" :
                        (parent.hovered ? "#FFFFFF" : "#FFFFFF")
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
        text: "View"
        font.pixelSize: 30
        background: Rectangle {
          implicitWidth: 150
          implicitHeight: 50
                color: parent.down ? "#E0E0E0" :
                        (parent.hovered ? "#FFFFFF" : "#FFFFFF")
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
        text: "Audio"
        font.pixelSize: 30
        background: Rectangle {
          implicitWidth: 150
          implicitHeight: 50
                color: parent.down ? "#E0E0E0" :
                        (parent.hovered ? "#FFFFFF" : "#FFFFFF")
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
      text: "Settings"
      font.pixelSize: 30
      background: Rectangle {
        implicitWidth: 150
        implicitHeight: 50
              color: parent.down ? "#E0E0E0" :
                      (parent.hovered ? "#FFFFFF" : "#FFFFFF")
      }
  }
}
