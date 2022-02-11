import QtQuick 2.15
import QtQuick.Controls 2.15
ApplicationWindow {
    visible: true
    width: 1080
    height: 720
    title: "HelloApp"
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
        border.width: 1
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
}
