import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.0

ApplicationWindow {
    width: 1080
    height: 720
    visible: true
    title: qsTr("Hello World")

    id: page

    SwipeView {
        id: swipeView

        anchors.fill: parent
        currentIndex: 0
        Page {
          Label {
            text: qsTr("First page")
            anchors.centerIn: parent
          }
        }
        Page {
          Label {
            text: qsTr("Second page")
            anchors.centerIn: parent
          }
        }
        Page {
          Label {
            text: qsTr("Third page")
            anchors.centerIn: parent
          }
        }
        Page {
          Label {
            text: qsTr("Fourth page")
            anchors.centerIn: parent
          }
        }
        Page {
          Label {
            text: qsTr("Fifth page")
            anchors.centerIn: parent
          }
        }
        Page {
          Label {
            text: qsTr("Sixth page")
            anchors.centerIn: parent
          }
        }
    }


        TabBar {
            TabButton {
                implicitWidth: 180
                implicitHeight: 70
                text: qsTr("Home")
                font.pixelSize: 30
                onClicked: {
                  swipeView.currentIndex = 0;
                }
            }
            TabButton {
                implicitWidth: 180
                implicitHeight: 70
                text: qsTr("About")
                font.pixelSize: 30
                onClicked: {
                  swipeView.currentIndex = 1;
                }
            }
            TabButton {
                implicitWidth: 180
                implicitHeight: 70
                text: qsTr("Connect")
                font.pixelSize: 30
                onClicked: {
                  swipeView.currentIndex = 2;
                }
            }
            TabButton {
                implicitWidth: 180
                implicitHeight: 70
                text: qsTr("View")
                font.pixelSize: 30
                onClicked: {
                  swipeView.currentIndex = 3;
                }
            }
            TabButton {
                implicitWidth: 180
                implicitHeight: 70
                text: qsTr("Audio")
                font.pixelSize: 30
                onClicked: {
                  swipeView.currentIndex = 4;
                }
            }
            TabButton {
                implicitWidth: 180
                implicitHeight: 70
                text: qsTr("Settings")
                font.pixelSize: 30
                onClicked: {
                  swipeView.currentIndex = 5;
                }
            }
        }

}
