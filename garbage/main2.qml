import QtQuick 2.6
import QtQuick.Controls 2.1

ApplicationWindow {
    width: 400
    height: 400
    visible: true

    Button {
      anchors {
        top: parent.top
        topMargin: 50
        left: parent.left
        leftMargin: 50
      }
        id: button
        text: "Settings"
        font.pixelSize: 30
        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            color: button.down ? "#d6d6d6" : "#f6f6f6"
        }
    }
}
